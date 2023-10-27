#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze, handling invalid inputs.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for the city while handling invalid inputs
    while True:
        city = input('Which city would you like to analyze (Chicago, New York City, Washington)? ').strip().lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid city name. Please choose from Chicago, New York City, or Washington.')

    # Get user input for the month (all, january, february, ..., june) and handle invalid inputs
    while True:
        month = input('Enter the month (all, january, february, ..., june): ').strip().lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Invalid month. Please enter a valid month or "all" for no filter.')

    # Get user input for the day of the week (all, monday, tuesday, ..., sunday) and handle invalid inputs
    while True:
        day = input('Enter the day of the week (all, monday, tuesday, ..., sunday): ').strip().lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Invalid day of the week. Please enter a valid day or "all" for no filter.')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Load the data for the specified city
    df = pd.read_csv(CITY_DATA[city])

    # Filter the data by the selected month
    if month != 'all':
        month_index = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['Start Time'].str.startswith(f'2017-{month_index:02}')]

    # Filter the data by the selected day of the week
    if day != 'all':
        df = df[df['Start Time'].str.startswith(day.title())]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['Month'].mode().values[0]
    print(f"The most common month for bike rides is: {common_month}")

    # Display the most common day of the week
    common_day = df['Day'].mode().values[0]
    print(f"The most common day of the week for bike rides is: {common_day}")

    # Extract the hour from the 'Start Time' column
    df['Hour'] = pd.to_datetime(df['Start Time']).dt.hour

    # Display the most common start hour
    common_hour = df['Hour'].mode().values[0]
    print(f"The most common start hour for bike rides is: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode().values[0]
    print(f"The most commonly used start station is: {common_start_station}")

    # Display most commonly used end station
    common_end_station = df['End Station'].mode().values[0]
    print(f"The most commonly used end station is: {common_end_station}")

    # Create a combination of 'Start Station' and 'End Station' for trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']

    # Display the most frequent combination of start station and end station trip
    common_trip = df['Trip'].mode().values[0]
    print(f"The most frequent combination of start station and end station trip is: {common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time for bike rides is: {total_travel_time} seconds")

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The average travel time for bike rides is: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("Counts of User Types:")
    print(user_type_counts)

    # Check if 'Gender' and 'Birth Year' columns exist in the DataFrame
    if 'Gender' in df.columns and 'Birth Year' in df.columns:
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of Gender:")
        print(gender_counts)

        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode().values[0])

        print("\nYear of Birth Statistics:")
        print(f"Earliest Birth Year: {earliest_birth_year}")
        print(f"Most Recent Birth Year: {most_recent_birth_year}")
        print(f"Most Common Birth Year: {most_common_birth_year}")

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


