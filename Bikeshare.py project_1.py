import time
import pandas as pd

CITY_DATA = {
    'chicago': 'data/chicago.csv',
    'new york city': 'data/new_york_city.csv',
    'washington': 'data/washington.csv'
}

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze, handling invalid inputs.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data')

    # Get user input for the city while handling invalid inputs
    city = get_user_input("Which city would you like to analyze (Chicago, New York City, Washington)? ", CITY_DATA.keys())

    # Get user input for the month and handle invalid inputs
    month = get_user_input("Enter the month (all, january, february, ..., june): ", MONTHS)

    # Get user input for the day of the week and handle invalid inputs
    day = get_user_input("Enter the day of the week (all, monday, tuesday, ..., sunday): ", DAYS)

    print('-' * 40)
    return city, month, day

def get_user_input(prompt, valid_options):
    """
    Helper function to get valid user input from a list of options.

    Args:
        prompt (str): The input prompt for the user.
        valid_options (list): List of valid options.

    Returns:
        (str) user_input - User input after validation.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            break
        else:
            print(f'Invalid input. Please choose from {", ".join(valid_options[:-1])}, or {valid_options[-1]}')
    return user_input

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

    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A').str.lower()

    # Filter by month if applicable
    if month != 'all':
        df = df[df['month'] == MONTHS.index(month) + 1]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Check if the DataFrame is empty
    if not df.empty:
        # Display the most common month.
        common_month = df['month'].mode().values[0]
        print(f"The most common month for bike rides is: {common_month}")

        # Display the most common day of the week.
        common_day = df['day_of_week'].mode().values[0]
        print(f"The most common day of the week for bike rides is: {common_day}")

        # Extract the hour from the 'Start Time' column.
        df['hour'] = df['Start Time'].dt.hour

        # Display the most common start hour.
        common_hour = df['hour'].mode().values[0]
        print(f"The most common start hour for bike rides is: {common_hour}")

        print("\nThis took %s seconds." % (time.time() - start_time))
    else:
        print("No data available for the selected filters.")

    print('-' * 40)

# The rest of your code (station_stats, trip_duration_stats, user_stats, display_data, and main) remains the same.

# Call the main function if the script is run as the main program.
if __name__ == "__main__":
    main()
