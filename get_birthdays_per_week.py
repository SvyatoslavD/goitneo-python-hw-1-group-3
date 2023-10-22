"""
get_birthdays_per_week.py

This module defines a function for listing users to greet on 
their upcoming birthdays within the next week.

It takes a list of user dictionaries, each containing "name" and
"birthday" keys, and prints the names of users who have birthdays in
the next week, grouped by the day of the week.

Example:
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "John Doe", "birthday": datetime(1976, 2, 24)},
    ]

    birthdays = get_birthdays_per_week(users)
    # Output will contain upcoming birthdays by day of the week.
"""

from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    """
    This function takes a list of user dictionaries containing names and birthdays,
    calculates the upcoming birthdays within the next week, and returns them by day of the week.

    Args:
        users (list): A list of user dictionaries, each containing "name" and "birthday" keys.

    Returns:
        None
    """
    birthdays_by_day = defaultdict(list)

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)

        if birthday_this_year.weekday() > 4:
            delta_days = 6 - birthday_this_year.weekday() + 1
            birthday_this_year = birthday_this_year.replace(
                day=birthday.day + delta_days)

        delta_days = (birthday_this_year - today).days
        if delta_days >= 7:
            continue

        day_of_week = (today + timedelta(days=delta_days)).strftime("%A")

        birthdays_by_day[day_of_week].append(name)

    return birthdays_by_day


if __name__ == "__main__":
    test_users = [
        {"name": "20th October", "birthday": datetime(1955, 10, 20)},
        {"name": "21th October", "birthday": datetime(1955, 10, 21)},
        {"name": "22th October", "birthday": datetime(1955, 10, 22)},
        {"name": "23th October", "birthday": datetime(1955, 10, 23)},
        {"name": "24th October", "birthday": datetime(1955, 10, 24)},
        {"name": "25th October", "birthday": datetime(1955, 10, 25)},
        {"name": "26th October", "birthday": datetime(1955, 10, 26)},
        {"name": "27th October", "birthday": datetime(1955, 10, 27)},
        {"name": "28th October", "birthday": datetime(1955, 10, 28)},
        {"name": "29th October", "birthday": datetime(1955, 10, 29)},
        {"name": "30th October", "birthday": datetime(1955, 10, 30)},
        {"name": "31th October", "birthday": datetime(1955, 10, 31)},
    ]

    birthdays = get_birthdays_per_week(test_users)

    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")
