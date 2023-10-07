from datetime import date, timedelta, datetime

def get_period(start_date, delta):
    period = {}
    for _ in range(delta + 1):
        period[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1) 
    return period

def get_birthdays_per_week(users):
    data = {} 
    if not users:
        return data

    start_date = date.today()
    result = {}
    result = get_period(start_date, 7)

    for user in users:
        bd: date = user["birthday"]
        date_bd = bd.day, bd.month
        if date_bd in list(result):
            bd = bd.replace(year = result[date_bd])
            # print(bd)
            if bd.weekday() in (5, 6):
                wekk = "Monday"
            else:
                wekk = bd.strftime("%A")
            if wekk not in data:
                data[wekk] = []
            data[wekk].append(user["name"])
                
    # print(data)
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
