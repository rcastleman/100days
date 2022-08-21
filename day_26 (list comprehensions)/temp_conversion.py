weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

def convert(f):
    return f * 9 / 5 + 32

weather_f = {k:convert(v) for (k, v) in weather_c.items()}

print(weather_f)