import requests
import csv
import os
from datetime import date

today_date = str(date.today())
country = "FR"
output_file = f'{country}_{today_date}_weather.csv'


def get_weather_data(station_code, date_str, writer):
    year, month, day = date_str.split('-')
    url = f'https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station={station_code}&data=all&year1={year}&month1={month}&day1={day}&year2={year}&month2={month}&day2={day}&tz=Etc%2FUTC&format=onlycomma&latlon=no&direct=no&report_type=1&report_type=2'
    response = requests.get(url)
    data = response.content.decode('utf-8')

    rows = csv.reader(data.splitlines())
    next(rows)
    for row in rows:
        writer.writerow([station_code] + row)


def read_airport_codes(filename):
    airport_codes = []
    with open(filename, 'r') as file:
        for line in file:
            airport_code = line.strip()
            airport_codes.append(airport_code)
    return airport_codes


airport_codes = read_airport_codes('OACI_FR.txt')

# Check if output file exists, if not create it
if not os.path.isfile(output_file):
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            ['station', 'valid', 'tmpf', 'dwpf', 'relh', 'drct', 'sknt', 'p01i', 'alti', 'mslp', 'vsby', 'gust',
             'skyc1', 'skyc2', 'skyc3', 'skyc4', 'skyl1', 'skyl2', 'skyl3', 'skyl4', 'wxcodes', 'ice_accretion_1hr',
             'ice_accretion_3hr', 'ice_accretion_6hr', 'peak_wind_gust', 'peak_wind_drct', 'peak_wind_time', 'feel',
             'metar', 'snowdepth'])

# Append data for each airport to the output file
with open(output_file, 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for code in airport_codes:
        get_weather_data(code, today_date, writer)
