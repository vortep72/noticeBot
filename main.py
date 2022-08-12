import telebot
import schedule
from security import TOKEN, tg_id


bot = telebot.TeleBot(TOKEN)

# Ежедневные уведомления


def my_daily_task1(tg_id):
    bot.send_message(tg_id, "Пора делать утренний пинг")


def my_daily_task2(tg_id):
    bot.send_message(tg_id, "Пора делать вечерний пинг")


def my_daily_task3(tg_id):
    bot.send_message(tg_id, "Настало время проверить очереди задач и пропушить")


def my_daily_task4(tg_id):
    bot.send_message(tg_id, "пора пройтись по высокоприоритетным проблемам и актуализировать сроки https://jira.im.perekrestok.ru/issues/?filter=15233")


def my_daily_task5(tg_id):
    bot.send_message(tg_id, "пора пройтись по проблемам 'Передано в команду' и актуализировать сроки https://jira.im.perekrestok.ru/issues/?filter=15910")


def my_daily_task6(tg_id):
    bot.send_message(tg_id, "пора пройтись по топу проблем и актуализировать сроки https://jira.im.perekrestok.ru/issues/?filter=15537")


def my_daily_task7(tg_id):
    bot.send_message(tg_id, "пора пройтись по проблемам, создающим нагрузку на КЦ и актуализировать сроки https://jira.im.perekrestok.ru/issues/?filter=16138")


def my_daily_task8(tg_id):
    bot.send_message(tg_id, "пора пройтись по проблемам в активных статусах и актуализировать сроки https://jira.im.perekrestok.ru/issues/?filter=16159")

schedule.every().day.at("09:00").do(my_daily_task1, tg_id)
schedule.every().day.at("10:00").do(my_daily_task8, tg_id)
schedule.every().day.at("15:45").do(my_daily_task2, tg_id)
schedule.every().day.at("13:00").do(my_daily_task3, tg_id)
schedule.every().day.at("10:30").do(my_daily_task4, tg_id)
schedule.every().day.at("11:45").do(my_daily_task5, tg_id)
schedule.every().day.at("14:30").do(my_daily_task6, tg_id)
schedule.every().day.at("16:30").do(my_daily_task7, tg_id)

# Еженедельные уведомления


def weekly_task1(tg_id):
    bot.send_message(tg_id, "Пройтись по постмортемам и завести задачи в Jira")


schedule.every().monday.at("10:15").do(weekly_task1, tg_id)


def weekly_task2(tg_id):
    bot.send_message(tg_id, "Пожалуйста, отправьте отчёт по инцидентам, если ещё не сделали это")


schedule.every().tuesday.at("11:30").do(weekly_task2, tg_id)


def weekly_task3(tg_id):
    bot.send_message(tg_id, "Пора составить предварительный график дежурных для IT XO")


schedule.every().wednesday.at("12:05").do(weekly_task3, tg_id)


def weekly_task4(tg_id):
    bot.send_message(tg_id, "Напоминаю, что сегодня нужно опубликовать график дежурных в IT XO")


schedule.every().friday.at("16:10").do(weekly_task4, tg_id)


def weekly_task5(tg_id):
    bot.send_message(tg_id, "Напоминаю, что нужно пройтись по закрытым задачам квартала для заполнения error source - https://jira.im.perekrestok.ru/issues/?jql=project%20%3D%20TS3%20AND%20issuetype%20%3D%20Problem%20AND%20status%20%3D%20Закрыта%20AND%20issueLinkType%20not%20in%20(%22error%20source%22)%20AND%20resolutiondate%20%3E%3D%202022-07-01")


schedule.every().monday.at("11:00").do(weekly_task5, tg_id)

while True:
    schedule.run_pending()


