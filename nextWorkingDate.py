import datetime as dt

idate = '20240928'
pDate = dt.datetime.strptime(idate,'%Y%m%d')

print('Converted date is : ',pDate)
aDay=pDate.strftime('%A')
print("Day is : ",aDay)

if aDay == 'Sunday':
    toAdd = 1
elif aDay == 'Saturday':
    toAdd = 2

wDay = pDate + dt.timedelta(days=toAdd)
print('Next Working date is : ',wDay)
