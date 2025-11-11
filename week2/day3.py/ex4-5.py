
import datetime 

#ex4
print(datetime.date.today())

# ex5
now = datetime.datetime.now()
next_year = now.year + 1
new_year = datetime.datetime(next_year, 1, 1)
print(now)
time_left = new_year - now
print("Time left until New Year:", time_left)

