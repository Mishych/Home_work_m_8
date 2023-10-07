from datetime import date, timedelta, datetime


def get_period(start_date, delta):
    period = {}
    for _ in range(delta + 1):
        period[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1) 
    return period

    
def get_birthdays_per_week(users):
    # sorted_users = sorted(users, key=lambda x: (x["birthday"].month, x["birthday"].day))
    # day_of_weeks = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday"}
    data = {}
    # filtered_data = {}
    # if not sorted_users:
    #     return filtered_data
    if not users:
        return data
    
    start_date = date.today()
    result = get_period(start_date, 7)
    
    # for _ in range(7):
    #     result[start_date.day, start_date.month] = start_date.year
    #     start_date += timedelta(1) тут Ви поточний startdate змінюєте, тому я і виносив в зовнішню функцію.
    
    print(users)
    print(start_date)
    for user in users:
        bd: date = user["birthday"]
        date_bd = bd.day, bd.month
        if date_bd in list(result):
            bd = bd.replace(year = result[date_bd])
            print(bd)
            if bd.weekday() in (5, 6):  #bd.weekday() ==  or bd.weekday() == 6:
                wekk = "Monday"
            else:
                wekk = bd.strftime("%A")
            if wekk not in data:
                data[wekk] = []
            data[wekk].append(user["name"])
    print(data)
    return data

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 10, 13).date()},
        {"name": "Ivan Jonson", "birthday": datetime(1999, 10, 11).date()},
        {"name": "Mikhael", "birthday": datetime(2001, 10, 10).date()},
        {"name": "Andriy", "birthday": datetime(2003, 10, 6).date()},
        {"name": "Tolik", "birthday": datetime(2002, 10, 8).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
