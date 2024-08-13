import datetime 
now = datetime.datetime.now()
age=int(input('Enter your bathday :'))
year = now.year
rx = year - age 
print('you age is : ' , rx)
