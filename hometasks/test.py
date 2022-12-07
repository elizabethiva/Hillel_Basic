number = int(input('Type number: '))
days = number // 60 // 60 // 24
hours = number // 60 // 60 % 24
hours_str = str(hours).zfill(2)
minutes = number // 60 % 60
minutes_str = str(minutes).zfill(2)
seconds = number % 60
seconds_str = str(seconds).zfill(2)
if days % 10 == 1:
    print(days, " день, ", hours_str, ":", minutes_str, ":", seconds_str, sep="")
elif days % 10 >= 2 and days % 10 <= 4:
    print(days, " дня, ", hours_str, ":", minutes_str, ":", seconds_str, sep="")
else:
    print(days, " дней, ", hours_str, ":", minutes_str, ":", seconds_str, sep="")
