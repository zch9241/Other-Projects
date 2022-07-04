import time
month, date = time.strftime('%m %d').split(' ')    #str

format_time = str(int(month)) + '.' + str(int(date))
print(format_time)