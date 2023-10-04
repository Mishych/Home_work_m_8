from datetime import date, timedelta, datetime


def get_birthdays_per_week(users):
    day_of_weeks = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Monday", 6: "Monday"}
    data = {}
    if not users:
        return data
    start_date = date.today()
    result = {}
    
    for _ in range(8):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)
    
    for user in users:
        bd: date = user["birthday"]
        date_bd = bd.day, bd.month
        if date_bd in list(result):
            bd = bd.replace(year = start_date.year)
            wekk = day_of_weeks[bd.weekday()]
            if wekk not in data:
                data[wekk] = []
            data[wekk].append(user["name"])
    return data

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 10, 5).date()},
        {"name": "John Lem", "birthday": datetime(1976, 10, 7).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
