from subprocess import call
import os
import schedule
import time

def do_work():
    call(['C:/Users/Poornima-2438/PycharmProjects/pythonProject2/venv/Scripts/python.exe','-m', 'robot',
          'C:/Users/Poornima-2438/PycharmProjects/pythonProject2/work/task1.robot'])

schedule.every(10).seconds.do(do_work)
time.sleep(5)

while 1:
    schedule.run_pending()
    time.sleep(5)