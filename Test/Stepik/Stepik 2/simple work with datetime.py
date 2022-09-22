import datetime

year, month, day = map(int, input().split())
d = datetime.date(year, month, day)
delta = datetime.timedelta(days=int(input()))
result = d + delta
print(result.year, result.month, result.day)  # Обрезает нули
