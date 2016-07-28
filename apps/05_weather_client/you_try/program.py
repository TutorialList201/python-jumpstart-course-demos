import requests


def main():
    # print the header
    # get zip code from users
    zip_code = input('What ZIP code do you want the weather for (97201)?')
    get_html_from_web(zip_code)
    # get html from web
    # parse the html
    # display for the forcast
    print('hello from main')


def print_the_header():
    print('----------------------------------------------')
    print('                WEATHER APP')
    print('----------------------------------------------')
    print()


def get_html_from_web(zip_code):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zip_code)
    print(url)


if __name__ == '__main__':
    main()
