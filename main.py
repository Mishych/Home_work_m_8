from datetime import date, timedelta, datetime

def get_birthdays_per_week(users):
    sorted_users = sorted(users, key=lambda x: (x["birthday"].month, x["birthday"].day))
    day_of_weeks = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday"}
    data = {}
    filtered_data = {}
    if not sorted_users:
        return filtered_data
    start_date = date.today()
    result = {}
    
    for _ in range(7):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)
    
    for user in sorted_users:
        bd: date = user["birthday"]
        date_bd = bd.day, bd.month
        if date_bd in list(result):
            bd = bd.replace(year = start_date.year)
            if bd.weekday() == 5 or bd.weekday() == 6:
                wekk = day_of_weeks[0]
            else:
                wekk = day_of_weeks[bd.weekday()]
            if wekk not in data:
                data[wekk] = []
            data[wekk].append(user["name"])
                
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
