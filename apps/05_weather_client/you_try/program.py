#!/usr/bin/env python3
import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport','condition',
                                       'temperature', 'unit', 'location')


def main():
    # print the header
    print_the_header()
    # get zip code from users
    zip_code = input('What ZIP code do you want the weather for (97201)?')
    html = get_html_from_web(zip_code)
    report = get_weather_from_html(html)

    print('The temp in {} is {} and {}'.format(
        report.location,
        report.temperature,
        report.unit,
        report.condition))
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
    response = requests.get(url)

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temperature = soup.find(id='curTemp').find(class_='wx-value').get_text()
    unit = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    location = cleanup_text(location)
    location = find_city_and_state_from_location(location)
    condition = cleanup_text(condition)
    temperature = cleanup_text(temperature)
    unit = cleanup_text(unit)
    
    report = WeatherReport(condition=condition, temperature=temperature,
                           unit=unit, location=location)
    return report


def find_city_and_state_from_location(location):
    parts = location.split('\n')
    return parts[0].strip()


def cleanup_text(text):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
