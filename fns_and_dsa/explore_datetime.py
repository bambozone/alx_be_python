import datetime

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

# Part 2: Calculate a Future Date
def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add: "))
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future Date:", formatted_future_date)

# Main function to run the script
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()