import telebot
import schedule
from security import TOKEN, tg_id
import datetime
bot = telebot.TeleBot(TOKEN)


def my_daily_task1(tg_id):
    bot.send_message(tg_id, "Пора делать утренний пинг")


def my_daily_task2(tg_id):
    bot.send_message(tg_id, "Пора делать вечерний пинг")


def my_daily_task3(tg_id):
    bot.send_message(tg_id, "Настало время проверить очереди задач и пропушить")


def my_daily_task4(tg_id):
    bot.send_message(tg_id, "парни, кажется вам нужен отдых, попейте чаю или покурите")
    

def my_daily_task5(tg_id):
    bot.send_message(tg_id, "Хэй! У меня новый дом и я тут одна!")
if schedule.every().wednesday.at("18:58").do(my_daily_task5, tg_id):
    print('Cообщение для my_daily_task5 отправлено!')


schedule.every().day.at("08:45").do(my_daily_task1, tg_id)
schedule.every().day.at("15:45").do(my_daily_task2, tg_id)
schedule.every().day.at("14:30").do(my_daily_task3, tg_id)
schedule.every().day.at("13:00").do(my_daily_task4, tg_id)


def weekly_task1(tg_id):
    bot.send_message(tg_id, "Пройтись по постмортемам и завести задачи в Jira")


schedule.every().monday.at("10:15").do(weekly_task1, tg_id)


def weekly_task2(tg_id):
    bot.send_message(tg_id, "Пожалуйста, отправьте отчёт по инцидентам, если ещё не сделали это")


schedule.every().tuesday.at("11:15").do(weekly_task2, tg_id)


def weekly_task3(tg_id):
    bot.send_message(tg_id, "Пора составить предварительный график дежурных для IT XO")


schedule.every().wednesday.at("12:05").do(weekly_task3, tg_id)


def weekly_task4(tg_id):
    bot.send_message(tg_id, "Напоминаю, что сегодня нужно опубликовать график дежурных в IT XO")


schedule.every().friday.at("16:10").do(weekly_task4, tg_id)


def weekly_task5(tg_id):
    bot.send_message(tg_id, "Напоминаю, что нужно пройтись по задачам для заполнения error source")


schedule.every().friday.at("16:10").do(weekly_task4, tg_id)

while True:
    schedule.run_pending()


