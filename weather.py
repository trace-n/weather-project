import csv
from datetime import datetime
# import statistics module
from statistics import mean


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

#   convert date string to date type
    date_converted = datetime.strptime(iso_string, '%Y-%m-%dT%H:%M:%S%z')

#   format date 
    date_formatted = date_converted.strftime("%A %d %B %Y")
    # print("date_form",date_formatted)
    return date_formatted


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """

#   convert to float and round to 1 decimal place
    temp_celsius = round(( float(temp_in_farenheit) - 32 ) * 5/9, 1)
    # print(temp_celsius)
    return temp_celsius


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

#   convert the list to float in case there is string supplied in list
    weather_data_converted = [float(item) for  item in weather_data]
    # print(mean(weather_data_converted))
    return mean(weather_data_converted)

    # return mean(weather_data)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    # with open handles file close
    with open(csv_file, mode = 'r', ) as file:

        # skip header line 1
        file = file.readlines()[1:]
        # read file of lists (exclude empty lines)                    
        # lines = list(line for line in l.strip() for l in file) if line)
        csv_file_read = csv.reader(file)
        
        # convert any values to integers
        csv_file_list = []
        for lines in csv_file_read:
            lines[1] = int(lines[1])
            lines[2] = int(lines[2])     
            csv_file_list.append(lines)       
            # print(lines)

        # print("csv file list", csv_file_list)

        # for lines in csv_file_read:
        #     csv_file_list.append([lines.rstrip('\n')])
            # csv_file_list.extend([lines])
            # csv_file = lines.splitlines()

        return csv_file_list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
