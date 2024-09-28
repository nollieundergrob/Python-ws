import pandas as pd
import sqlite3
from datetime import datetime
def process_dataframe(df):
    student_records = {}
    for index, row in df.iterrows():
        student_name = row['name']
        time = datetime.strptime(row['time_auth'], '%H:%M')
        date = row['date_auth']

        if student_name not in student_records:
            student_records[student_name] = {'Утро': None, 'Обед': None, 'ГРУППА': row['group'], 'Время утро': None, 'Время обед': None, 'Дата': date}

        if time < datetime.strptime('09:30', '%H:%M'):
            if student_records[student_name]['Утро'] is None:
                student_records[student_name]['Утро'] = 'Пришел во время'
                student_records[student_name]['Время утро'] = row['time_auth']
        elif time >= datetime.strptime('09:30', '%H:%M') and time < datetime.strptime('12:00', '%H:%M'):
            if student_records[student_name]['Утро'] is None:
                student_records[student_name]['Утро'] = 'Опоздание утром'
                student_records[student_name]['Время утро'] = row['time_auth']
        elif time >= datetime.strptime('12:00', '%H:%M') and time < datetime.strptime('12:50', '%H:%M'):
            if student_records[student_name]['Обед'] is None:
                student_records[student_name]['Обед'] = 'Пришел во время'
                student_records[student_name]['Время обед'] = row['time_auth']
        elif time >= datetime.strptime('12:50', '%H:%M') and time < datetime.strptime('15:30', '%H:%M'):
            if student_records[student_name]['Обед'] is None:
                student_records[student_name]['Обед'] = 'Опоздание после обеда'
                student_records[student_name]['Время обед'] = row['time_auth']
        else:
            if student_records[student_name]['Утро'] is None:
                student_records[student_name]['Утро'] = 'Не пришел'
            if student_records[student_name]['Обед'] is None:
                student_records[student_name]['Обед'] = 'Не пришел'

    result_df = pd.DataFrame(list(student_records.items()), columns=['ФИО', 'Записи'])
    result_df = pd.DataFrame(result_df['Записи'].tolist(), index=result_df['ФИО'])
    result_df['Опоздание'] = ''
    for index, row in result_df.iterrows():
        if row['Утро'] == 'Опоздание утром' or row['Утро'] == 'Не пришел':
            result_df.at[index, 'Опоздание'] += '+'
        if row['Обед'] == 'Опоздание после обеда' or row['Обед'] == 'Не пришел':
            result_df.at[index, 'Опоздание'] += '+'

    result_df = result_df.fillna('Не пришел')

    # Добавляем столбец дата в начало DataFrame
    result_df = result_df.reindex(columns=['Дата'] + [col for col in result_df.columns if col != 'Дата'])

    return result_df

# connect = sqlite3.connect('db.sqlite3')
# df = pd.read_sql_query('SELECT * FROM liveStream_attendance',con=connect)
# result= process_dataframe(df)
# result.to_excel('Готовая посещаемость.xlsx')
# # print(result.head(10))