from django import forms


class Auth_Student(forms.Form):
    name = forms.CharField(label='ФИО',max_length=100,min_length=10)
    choice = ((None,None),('Python 1','Python 1'),('Python 2','Python 2'),('Python 3','Python 3'),('Python 4','Python 4'),('Python 5','Python 5'),('Python 6','Python 6'),('Python 7','Python 7'),('Python 8','Python 8'),('Python 9','Python 9'),('Python 10','Python 10'),('Python 11','Python 11'),('Python 12','Python 12'),('Python 13','Python 13'))
    group = forms.ChoiceField(choices=choice,label='Группа Python')
    student = forms.CharField(max_length=100,label='Логин от аккаунта student',min_length=9)
    
    def clean_student(self):
        student_login = self.cleaned_data['student']
        digits = student_login[-3]
        if not str.isdigit(digits) : 
            raise forms.ValidationError("логин должен содержать слово student и число например 001")
        return student_login
    
    def clean_name(self):
        full_name = self.cleaned_data['name']
        if full_name.count(' ') < 2: 
            raise forms.ValidationError("Неверный формат имени. Н-р Иванов Иван Иванович")
        return full_name