import requests
import csv
import os


def get_weather_data(station_code, start_date, end_date, writer):
    year, month, day = start_date.split('-')
    year2, month2, day2 = end_date.split('-')
    url = f'https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station={station_code}&data=all&year1={year}&month1={month}&day1={day}&year2={year2}&month2={month2}&day2={day2}&tz=Etc%2FUTC&format=onlycomma&latlon=no&direct=no&report_type=1&report_type=2'
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


def read_parameters(file_name):
    with open(file_name, "r") as file:
        parameters = {}
        for line in file:
            key, value = line.strip().split(":")
            parameters[key.strip()] = value.strip()
    country = parameters.get("country")
    start_date = parameters.get("start date")
    end_date = parameters.get("end date")

    return country, start_date, end_date


if __name__ == "__main__":
    country, start_date, end_date = read_parameters("parameter.txt")
    output_file = f'{country}_{start_date}_{end_date}_weather.csv'
    airport_codes = read_airport_codes(f'OACI_{country}.txt')
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
            get_weather_data(code, start_date, end_date, writer)
