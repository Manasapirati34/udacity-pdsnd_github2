import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list=['january','february','march','april','may','june','all']
day_list=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
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
    city=(input("enter city:"))
    city=city.lower()
    while city not in ["chicago","new york city", "washington"]:
        print("Enter correct city")
        city=(input())
        city=city.lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    #month_list=['january','february','march','april','may','june','all']
    month=(input("enter month:"))
    month=month.lower()
    while month not in month_list:
        print("Enter correct month")
        month=(input())
        month=month.lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #day_list=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    day=input("enter day:")
    day=day.lower()
    while day not in day_list :
        print("Enter Correct day")
        day=(input())
        day=day.lower()
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
    df = pd.read_csv(CITY_DATA[city])
     
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    df['hour'] = df['Start Time'].dt.hour
    # filtering by month
    # using month_list          
    if month != 'all':
        # using the index of  month_list to get the corresponding integer
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = month_list.index(month) + 1 
            # filtering  by month to create the new dataframe
            df = df[df['month'] == month]
     # filtering by day of week if applicable
     # using day_list         
    if day != 'all':
            # filtering  day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]                                        
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_m=df['month'].mode().values[0]
    common_month=month_list[common_m-1]
    print("common month is {}".format(str(common_month)))
              
    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode().values[0]   
    print(" common day of week {},".format(str(common_day)))      

    # TO DO: display the most common start hour
    common_hour=df['hour'].mode().values[0]
    print("common hour {}".format(str(common_hour)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode().values[0]
    print("Common start station is {}".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode().values[0]
    print("Common End station is {}".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " " + df['End Station']
    common_trip= df['routes'].mode().values[0]
    print("Common start and end station combination trip is: {}".format(common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # defining a label duration
    df['duration'] = df['End Time'] - df['Start Time']
    total=df['duration'].sum()
    print("Total travel time is: {}".format(str(total)))
    
    # display mean travel time
    mean=df['duration'].mean()
    print("Mean travel time is: {}".format(str(mean)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    print("counts of user types:")
    print(df['User Type'].value_counts())
    
    # TO DO: Display counts of user types
    try:
        gender_count=df['User Type'].value_counts()
        print("Here are the counts of gender: {}".format(gender_count))
    except Execption as e:
        print('Can not calculate the amount and gender of users, as an Error occurred: {}'.format(e))    
    # Display earliest, most recent, and most common year of birth
    #earliest year of birth
    try:
        min_year=int(df['Birth Year'].min())
        print("Earliest birth year is: {}".format(str(min_year)))
    
    #recent year of birth
        max_year=int(df['Birth Year'].max())
        print("Recent birth year is: {}".format(str(max_year)))
                
    # common birth year
        common_year=int(df['Birth Year'].mode().values[0])             
        print("Common birth year is: {}".format(str(common_year)))
    except Exception as e:
        print('Couldn\'t calculate the age structure of our customers, as an Error occurred: {}'.format(e))    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_info(df):
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """

    start_loc = 0
    end_loc = 5

    display_active = input("Do you want to see the raw data?: ").lower()

    if display_active == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_info(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
