import datetime


def print_header():
    print('-------------------------------------------')
    print('             BIRTHDAY APP')
    print('-------------------------------------------')
    print()


def get_birthday_from_user():
    print('Tell us when you were born: ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_days_between_dates(original_date, now):
    dt = now - datetime.datetime(now.year, original_date.month,
                                 original_date.day)
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_birthday_information(days):
    if days < 0:
        print('Your birthday is in {} days!'.format(-days + 1))
    elif days > 0:
        print('You had your birthday already this year! {} days ago'.format(
            days))
    else:
        print('Happy birthday!!!')


def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)

main()
