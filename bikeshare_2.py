import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
	print('Hello! Let\'s explore some US bikeshare data!')
	print('Data is available for Chicago, New York City, and Washington')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
	city = ''
	while city.lower() not in ('washington','chicago','new york city'):
		city = input('Please enter which city you would like to see:')
		if city.lower() not in ('washington','chicago','new york city'):
			print('The entry is not understood.  Please enter one of the following cities: Chicago, New York City, Washington')

    # get user input for month (all, january, february, ... , june)
    month = ''
	while month.lower() not in ('all','january','february','march','april','may','june'):
		month = input('Please enter which month you would like to see:')
		if month.lower() not in ('all','january','february','march','april','may','june'):
			print('The entry is not understood.  Please enter one of the following options: All, January, February, March, April, May,                          June')	

    # get user input for day of week (all, monday, tuesday, ... sunday)
	day = ''
	while day.lower() not in ('all','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'):
		day = input('Please enter which city you would like to see:')
		if day.lower() not in ('all','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'):
			print('The entry is not understood.  Please enter one of the following options: all, Sunday, Monday, Tuesday, Wednesday,                            Thursday, Friday, Saturday')

	print('-'*40)
return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
