import datetime as dt

current_date = dt.date.today()
print(current_date)

new = dt.date(2021, 10, 25)
print(new)
print("Year : ", new.year)
print("Month : ", new.month)
print("Day : ", new.day)

print("***************")

a = dt.time(10, 45, 5, 555505)
print(a)
print("Hour : ", a.hour)
print("Minute : ", a.minute)
print("Second : ", a.second)

current_time = dt.datetime.now()
print(current_time)

print("***************")

new = dt.datetime(2021,5,31,12,2,10)
print(new)
print(new.date())
print(new.time())

print("***************")

new_year = dt.datetime(2024, 1, 1)
current_date = dt.datetime.now()
dif = new_year - current_date

print(dif)

print("***************")

print(current_date)

s = current_date.strftime("%A %B %d %Y")

print(s)