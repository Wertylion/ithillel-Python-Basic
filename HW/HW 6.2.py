seconds = int(input("Enter seconds: "))

days = seconds // 86400
seconds = seconds % 86400

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
    day_word = "дні"
else:
    day_word = "днів"

if hours < 10:
    hours = "0" + str(hours)
else:
    hours = str(hours)

if minutes < 10:
    minutes = "0" + str(minutes)
else:
    minutes = str(minutes)

if seconds < 10:
    seconds = "0" + str(seconds)
else:
    seconds = str(seconds)

print(str(days) + " " + day_word + ", " + hours + ":" + minutes + ":" + seconds)