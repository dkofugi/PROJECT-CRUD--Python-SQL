import schedule
from interface import notification
from arquivos import verificarCount
import time


total_tarefas= verificarCount()
schedule.every().day.at("21:49").do(lambda: notification(total_tarefas))

while True:
    schedule.run_pending()
    time.sleep(10)

