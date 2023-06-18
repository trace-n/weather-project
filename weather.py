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
    date_converted = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")

#   format date 
    date_formatted = date_converted.strftime("%A %d %B %Y")

#   return formatted date
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

#   return converted date to celcius
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

#   return mean temperature    
    return mean(weather_data_converted)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    # with open handles file close
    with open(csv_file, mode = "r", ) as file:
        # skip header line 1
        # file contains list of rows from csv file including /n line character
        file = file.readlines()[1:]

        # use list comprehension to execute each line with a for loop
        # first step - rstrip removes trailing character new line \n from each item in line        
        file = [line.rstrip() for line in file]          

        # second step - loop through and add the line if not blank (exclude empty lines)        
        file = [line for line in file if line]

        #read file
        csv_file_read = csv.reader(file)

        # final list to return
        csv_file_list = []

        # convert any values to integers and add to final list of lists 
        for line in csv_file_read:        
            line[1] = int(line[1])
            line[2] = int(line[2])     
            csv_file_list.append(line)       

        # return a list of lists from csv file
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
    
    # return minimum temp and position in list
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

    # find max temp 
        max_temp = max(weather_data)
    
    # handle where the max may exist more than once in list
        max_index = [i for i in range(len(weather_data)) if weather_data[i] == max_temp]
        
    # find the last index where max exists in list
        max_position = max_temp, max_index[-1]
    else:
        max_position = ()
    
    # return max temp and position in list
    return max_position


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # create a dictionary with the weather data provided
    weather_summary = {}

    # add weather data to dictionary - index as key with nested dictionary of Day, Min and Max values 
    for i in range(len(weather_data)):
        weather_summary[i] = { "Day": weather_data[i][0], "Min": weather_data[i][1], "Max": weather_data[i][2] }

    # finds the min/max temperature, index of min/max temp using function with list comprehension
    # ---------------------------------------------------
    min_temp, min_temp_index = find_min([value["Min"] for key, value in weather_summary.items()])
    max_temp, max_temp_index = find_max([value["Max"] for key, value in weather_summary.items()])

    # finds the min/max mean temp using function with list comprehension
    # ---------------------------------------------------
    mean_min = calculate_mean([value["Min"] for key, value in weather_summary.items()])   
    mean_max = calculate_mean([value["Max"] for key, value in weather_summary.items()])

    # reference the min/max temp index for dictionary key and nested dictionlary key value "Day"
    min_day = convert_date(weather_summary.get(min_temp_index).get("Day"))      
    max_day = convert_date(weather_summary.get(max_temp_index).get("Day"))  

    # output to string - format and convert temps fahrenheit to celcius    
    weather_data_summary = str(len(weather_data)) + " Day Overview\n"
    weather_data_summary += "  The lowest temperature will be " + format_temperature(convert_f_to_c(min_temp))  
    weather_data_summary += ", and will occur on " + min_day +".\n"
    weather_data_summary += "  The highest temperature will be " + format_temperature(convert_f_to_c(max_temp))
    weather_data_summary += ", and will occur on " + max_day +".\n"    
    weather_data_summary += "  The average low this week is " + format_temperature(convert_f_to_c(mean_min)) +".\n"
    weather_data_summary += "  The average high this week is " + format_temperature(convert_f_to_c(mean_max)) + ".\n" 

    # return summary of weather data 
    return weather_data_summary    


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
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

    # return daily summary weather data  
    return weather_data_summary
