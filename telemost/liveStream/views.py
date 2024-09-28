from django.shortcuts import render,HttpResponse,redirect
import datetime
from .models import Attendance
from .forms import Auth_Student
import os,pandas,colorama
import check_pandas




def generate_table(request):
    df = pandas.read_excel('Готовая посещаемость.xlsx')
    today = datetime.date.today()
    # df = df[df['Дата'] == today.strftime('%d-%m-%Y')]
    df = df.sort_values(by='ФИО')
    # Create an HTML table
    html_table = df.to_html(index=False)
    
    # Render the HTML table in a template
    return render(request, 'table.html', {'html_table': html_table})

def check_time(session):
    if 'user' in session:
        current_time = datetime.datetime.now().time()
        if current_time >= datetime.time(12, 10) and current_time < datetime.time(12, 40):
            print(session['user'], ' - Сессия сброшена!')
            session.pop('user')
            return True
        else:
            return False
    else:
        current_time = datetime.datetime.now().time()
        if current_time >= datetime.time(12, 10) and current_time < datetime.time(12, 40):
            return True
        else:
            return False


# Create your views here.
def index(request):
    time_check =  check_time(request.session)
    message = 'Сессия будет доступна в 12:40\n' if time_check else ''
    if not time_check:
        if not 'user' in request.session:
            form = Auth_Student()
            if request.method == 'GET':
                data = {
                    'now': str(datetime.datetime.now().strftime("%d.%m.%Y")),
                    'form': form,
                    'message':message,
                }
                return render(request, 'auth.html', context=data)
            elif request.method == 'POST':
                    form = Auth_Student(request.POST)  # Create a form instance with the POST data
                    if form.is_valid():
                        name = form.cleaned_data['name'].upper()
                        group = form.cleaned_data['group'].upper()
                        student = form.cleaned_data['student'].lower()
                        ip_address = request.META['REMOTE_ADDR']
                        print(f'{colorama.Fore.RED}{name} is сonnected by ip address {colorama.Fore.CYAN}{ip_address}{colorama.Style.RESET_ALL}')
                        date_auth = datetime.datetime.now().strftime("%d.%m.%Y")
                        time_auth = datetime.datetime.now().strftime("%H:%M")
                        request.session['user'] = name
                        request.session['ip'] = ip_address
                        attendance = Attendance(
                            name=name,
                            group=group,
                            student=student,
                            ip=ip_address,
                            date_auth=date_auth,
                            time_auth=time_auth,
                        )
                        attendance.save()
                        
                        return redirect(stream)
                    else:
                        message = 'Введены не корректные значения'
                        data = {
                        'now': str(datetime.datetime.now().strftime("%d.%m.%Y")),
                        'form': form,
                        'message':message
                    }
                        return render(request, 'auth.html', context=data)
        else:
            
            return redirect(stream)
    else:
        form = Auth_Student()
        data = {
              'now': str(datetime.datetime.now().strftime("%d.%m.%Y")),
                    'form': form,
                    'message':message,
                }
        return render(request, 'auth.html', context=data)
    
def generate_list(request):
    df = pandas.DataFrame(list(Attendance.objects.all().values()))
    dfe = check_pandas.process_dataframe(df=df)
    df.to_excel('Посещаемость.xlsx',index=0)
    dfe.to_excel('Готовая посещаемость.xlsx')
    return redirect(stream)

def reset_session(request):
    request.session.pop('user')
    return redirect('index')

def stream(request):
    check_time(request.session)
    iframe = open('iframe.txt','r').read()
    if 'user' in request.session:
        print(f'{colorama.Fore.RED}{request.session["user"]} watching stream by ip - {colorama.Fore.CYAN}{request.session["ip"]}{colorama.Style.RESET_ALL}')
        data = {
            'iframe':iframe}
        return render(request,'stream.html',data)
    else:
        return redirect('index')