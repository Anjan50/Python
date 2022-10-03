import time
from win10toast import ToastNotifier

time_now = time.localtime()
hour = time_now[3]
toaster = ToastNotifier()
next_hour = hour
while True:
    time_now = time.localtime()
    hour = time_now[3]
    if hour == next_hour:
        toaster.show_toast("Drink Water and Wash your Face!",
                           "Always take a break")
        next_hour = hour + 1
        print(next_hour)
    if hour == 0:
        next_hour = 0
    print(time_now)

print(time_now)
