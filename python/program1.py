import calendar

start = 2024
end = int(input("Enter final year: "))

for year in range(start, end+1):
    if calendar.isleap(year):
        print(year)