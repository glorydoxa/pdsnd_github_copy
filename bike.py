import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("would you like to see data for Chicago, New York, or Washington?")

    while True:
        city_choice = str(input('Get the filters for: '))
        cities = ['1', '2', '3', 'chicago', 'new_york', 'washington']

        if city_choice == 'chicago' or '1':
            city_choice = 'chicago.csv'
        elif city_choice == 'new york' or '2':
            city_choice = 'new_york_city.csv'
        elif city_choice == 'washington' or '3':
            city_choice = 'washington.csv'
        else:
            print ('The city chosen is out of range')
        break


    print(f"'{city_choice}' Which month would you like to view its data?./n")

    period_filters = ['1', '2', '3', '4', 'month', 'day', 'both', 'none']

    while True:
        period_filters_choosen = input(
            f"\n\nWould you like to filter {cities}'s data by:\n\n\t(1) Month\n\t(2) Day\n\t(3) Both\n\t(4) None\n\n(Type the filter number or the filter name.)\n> ").strip().lower()

        # Input validation
        if period_filters_choosen in period_filters:
            break
        else:
            print(f"'{period_filters_choosen}' is not a valid input. Please try again.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    Months = ['January', 'February', 'March', 'April', 'May', 'June']
    DOW = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday'] #Where DOW means Day of Week

    #when there is no filter needed
    if period_filters == 'none' or '4':
        print(f"\ndata{cities}'s data from January to June.\n\n")
        Month = 'all'
        Day = 'all'

    #When the period_filters choosen are for both
    elif period_filters == 'both' or '3':
        while True:
            month_choosen = str(input('Get the filters for the month of?: ')).title()
            if month_choosen in Months:
                Month = month_choosen
                break
            else:
                print ('The choosen month is out of range')

        # For day period filters
        while True:
            day_choosen = str(input('name of the day of week to filter by, or "all" to apply no day filter:')).title()
            if day_choosen == 'Monday':
                day_choosen = DOW[0]
            elif day_choosen == 'Tuesday':
                day_choosen = DOW[1]
            elif day_choosen == 'Wednesday':
                day_choosen = DOW[2]
            elif day_choosen == 'Thursday':
                day_choosen = DOW[3]
            elif day_choosen =='Friday':
                day_choosen = DOW[4]
            elif day_choosen == 'Saturday':
                day_choosen = DOW[5]
            elif day_choosen == 'Sunday':
                day_choosen = DOW[6]
                break
            else:
                print('The day choosen is out of range')


    #for only month period  filters
    elif period_filters == 'month' or '1':
        while True:
            month_choosen = str(input('Get the filters for the month of?: ')).title()

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
           #input filtering
            if month_choosen in Months:
                Month = month_choosen
                Day = 'all'
                break
            else:
                print(
                    f"'{month_choosen}' is out of range. Please try again.\n")


    elif time_filter == '2' or period_filters == 'Day':
        while True:
            day_selection = input(
                "\nWhich day?\nType a day name: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]\n> ").strip().lower()

            # Input filtering
            if day_choosen in DOW:
                Day = day_choosen
                Month = 'all'

                break
            else:
                print(
                    f"'{day_selection}' is out of range. Please try again.\n")
    print('-'*40)
    return city_choice, Month, Day

values_filtered = get_filters()
city_choice, Month, Day = values_filtered


def load_data(city_choice, Month, Day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loading data files
    df = pd.read_csv(city_choice)

    # conveting Start Time column to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # getting month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['dow'] = df['Start Time'].dt.dayofweek

    #  month filter when choosen
    if Month != 'all':
        df = df[df['month'] == month.title()]
    else:
        pass

    # month filter when choosen
    if Day != 'all':
        # New dataframe filtered by day
        df = df[df['dow'] == day.title()]

    return df

df = load_data(city_choice, Month, Day)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if Month == 'all':
        freq_month = df['month'].mode()[0]
        print(f"The most frequent Month is: {freq_month}")

    # TO DO: display the most common day of week
    # DOW filters where applicable
    if Day == 'all':
        freq_day = df['dow'].mode()[0]
        print(f"The most frequent  day is: {freq_day}")

    # TO DO: display the most common start hour
    # create an hour column from the 'Start Time' column
    df['hour'] = df['Start Time'].dt.hour

    freq_hour = df['hour'].mode()[0]
    print(f"the most frequent Start Hour is: {freq_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

time_stats(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Freq_start_stats = df['Start Station'].mode()[0]
    print(f"the most frequent start station is: {Freq_start_stats}\n")

    # TO DO: display most commonly used end station
    freq_end_stats = df['End Station'].value_counts().index.tolist()[0]
    print(f"The most frequent end station is: {freq_end_stats}\n")

    # TO DO: display most frequent combination of start station and end station trip
    freq_route = df.groupby(['Start Station', 'End Station']).size().reset_index(name='count').sort_values(
        'count', ascending=False).head(1).reset_index()[['Start Station', 'End Station', 'count']]
    print(
        f"The most frequent use of both start station & end station trip is: {freq_route}\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip = df['Trip Duration'].sum()
    print("Total Travel Time:",trip, sep = " ")

    # TO DO: display mean travel time
    avg_trip = df['Trip Duration'].mean()
    print ("Mean Travel :",avg_trip, sep= " ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Subscribers = len(df[df["User Type"] == "Subscriber"])
    Customers = len(df[df["User Type"] == "Customer"])
    print ('subscribers:' , Subscribers, sep = " ")
    print ('customers:', Customers, sep = " ")

    # TO DO: Display counts of gender
    try:
        Males = len(df[df["Gender"] == "Male"])
        Females = len(df[df["Gender"] == "Female"])
    except:
        print('There is no Gender data')
    else:
        print('Males :', Males, sep = " ")
        print('Females :', Females, sep = " ")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()
    except:
        print('There is no Birth Year data')
    else:
        print ('Earliest :', earliest, sep = " ")
        print ('Most recent :', most_recent, sep = " ")
        print ('Most common :', most_common, sep = " ")

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #-Descriptive Statistics

def descriptive_stats(df):

    while True:
        show_me_more = str(input('Do you need to see more data ? yes or no')).lower()
        if show_me_more == 'yes':
            print(df.describe())
        else:
            print('Done')
        break

def show_data(city_choice):
    """
    This takes the city name from the choosesn input fuction
    and returns the data of that city like the .head() method in pandas
    Args:
        (str) city - name of the city to show the data.
    Returns:
        df - raw data of that city first 5 rows.
    """

    print('\ncity data to display... \n')

    choosen_data_view = input(
        "View the raw data in chuncks of 5 rows type? (Yes/No)\n> ").strip().lower()
    start_loc = 0
    while choosen_data_view == 'yes':
        print(df.iloc[0:5])
        start_loc += 5
        choosen_data_view = input('do you wish to continue?')

    while choosen_data_view != 'yes':
        pass
        break
        print ('That will be all. Bye')

show_data(city_choice)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city,month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
