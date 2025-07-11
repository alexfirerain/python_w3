# Периодические задания
import schedule
import datetime

i = 1


def job():
    global i
    print(f'скрипт запущен {i}-й раз')
    i += 1
    t = datetime.datetime.now()
    print(t.strftime('%H:%M:%S'))


schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()


"""
объектная модель документа
DOM
d него входит
"""