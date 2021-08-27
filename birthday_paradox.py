import datetime, random


def get_birthdays(num_of_birthdays):
    """Create an object of random birthdays"""
    birthdays = []
    for i in range(num_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        random_num_of_days = datetime.timedelta(random.randint(1, 365))
        birthday = start_of_year + random_num_of_days
        birthdays.append(birthday)
    return birthdays


def find_matching_birthdays(birthdays):
    """Find matching birthdays and returns the first instance if found"""
    if len(birthdays) == len(set(birthdays)):
        return None

    for i, birthday1 in enumerate(birthdays):
        for j, birthday2 in enumerate(birthdays[i + 1:]):
            if birthday1 == birthday2:
                return birthday1


def interface():
    print('Search for matching birthdays out of how much people?')
    response = input()
    counter = 0
    print('Simulating...')
    for i in range(100000):
        birthdays = get_birthdays(int(response))
        matches = find_matching_birthdays(birthdays)
        if matches:
            counter = counter + 1
    chance = counter / 100000 * 100
    print(f"Out of 100,000 simulations, in {counter} of times there were matching birthdays.")
    print(f"This means out of {response} people there's a {chance}% chance of people with matching birthdays.")


interface()
