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
        non_blank_lines = (line.rstrip() for line in file) # all lines inlcuding blanks
        # read file of lists (exclude empty lines)        
        # non_blank_lines = list(line for line in non_blank_lines if line) # Non-blank lines an d add to list
        non_blank_lines = (line for line in non_blank_lines if line) # Non-blank lines an d add to list
        # print(non_blank_lines)

            
        # lines = list(line for line in l.strip() for l in file) if line)
        # csv_file_read = csv.reader(file)
        csv_file_read = csv.reader(non_blank_lines)

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

    # handle an empty list
    if len(weather_data) > 0:

    # if strings in list - set the values to float 
        if type(weather_data[0]) == str:
            weather_data = [float(i) for i in weather_data]

    # find min temp 
        min_temp = min(weather_data)
    
    # handle where the min may exist more than once in list
        min_index = [i for i in range(len(weather_data)) if weather_data[i] == min_temp]

    # find the last index where min exists in list
        min_position = min_temp, min_index[-1]
    else:
        min_position = ()
    
    return min_position


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    # handle an empty list
    if len(weather_data) > 0:

    # if strings in list - set the values to float 
        if type(weather_data[0]) == str:
            weather_data = [float(i) for i in weather_data]

    # find min temp 
        max_temp = max(weather_data)
    
    # handle where the min may exist more than once in list
        max_index = [i for i in range(len(weather_data)) if weather_data[i] == max_temp]
        
    # find the last index where min exists in list
        max_position = max_temp, max_index[-1]
    else:
        max_position = ()
    
    return max_position


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    #   ---------------------    
    #   Example output
    #   ---------------------
    #   5 Day Overview
    #   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
    #   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
    #   The average low this week is 12.2°C.
    #   The average high this week is 17.8°C.

    
    weather_data_summary = str(len(weather_data)) + " Day Overview\n"

    # add a for loop to loop through the 
    day_list = []
    min_list = []
    max_list = []

    # create list of dates, min, max
    for i in range(len(weather_data)):
        day_list.append(weather_data[i][0])
        min_list.append(weather_data[i][1])
        max_list.append(weather_data[i][2])
   
    # get lowest temp
    min_temp = min(min_list)

    # get index of lowest temp and find day
    min_index = [i for i in range(len(min_list)) if min_list[i] == min_temp]    
    min_date = day_list[min_index[-1]]           

    # convert date format
    min_day = convert_date(min_date)

    # get highest temp 
    max_temp = max(max_list)    

    # get index of highest temp and find day
    max_index = [i for i in range(len(max_list)) if max_list[i] == max_temp]
    max_date = day_list[max_index[-1]]   

    # convert date format
    max_day = convert_date(max_date)

    # get average low
    mean_min = mean(min_list)

    # get average high
    mean_max = mean(max_list)

    # convert fahrenheit to celsius
    weather_data_summary += "  The lowest temperature will be " + format_temperature(convert_f_to_c(min_temp)) 
    weather_data_summary += ", and will occur on " + min_day +".\n"
    weather_data_summary += "  The highest temperature will be " + format_temperature(convert_f_to_c(max_temp)) 
    weather_data_summary += ", and will occur on " + max_day +".\n"    
    weather_data_summary += "  The average low this week is " + format_temperature(convert_f_to_c(mean_min)) +".\n"
    weather_data_summary += "  The average high this week is " + format_temperature(convert_f_to_c(mean_max)) + ".\n"

    # print(weather_data_summary)
    return weather_data_summary    
    



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    #   ---------------------
    #   Example output
    #   ---------------------    
    #   ---- Friday 02 July 2021 ----
    #   Minimum Temperature: 9.4°C
    #   Maximum Temperature: 19.4°C
    
    weather_data_summary = ""

    # add a for loop to loop through the 
    for i in range(len(weather_data)):

        weather_data_summary += "---- "

        # convert date format
        weather_data_summary += convert_date(weather_data[i][0])
        weather_data_summary += " ----" + "\n"

        # convert fahrenheit to celsius
        min_temp = format_temperature(convert_f_to_c(weather_data[i][1]))
        max_temp = format_temperature(convert_f_to_c(weather_data[i][2]))
        
        weather_data_summary += "  Minimum Temperature: " + str(min_temp) + "\n"
        weather_data_summary += "  Maximum Temperature: " + str(max_temp) + "\n\n"

    # print(weather_data_summary)
    return weather_data_summary
