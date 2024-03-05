from datetime import datetime

# Get the current date and time
now = datetime.now()

# Extract the day of the week in string format
day_of_week = now.strftime('%A')

# Init dict for week day
weekDay = {
    'Monday': 'Sad day',  # Often seen as the start of the work/school week.
    'Tuesday': 'Busy day',  # The productivity kicks in.
    'Wednesday': 'Hump day',  # Midweek, the peak of the workload.
    'Thursday': 'Hopeful day',  # The anticipation for the weekend begins.
    'Friday': 'Happy day',  # The excitement for the weekend is high.
    'Saturday': 'Relaxing day',  # Typically a day for leisure and relaxation.
    # Often a day for family gatherings and rest before the week starts again.
    'Sunday': 'Family day',
}

# Print conclusion
print(f"The {day_of_week} is a", weekDay[day_of_week])
