'''Weather forecasting organization wants to show is it day or night. So, write a
program for such organization to find whether is it dark outside or not.
Hint: Use time module'''

import time

x=time.localtime()

if x.tm_hour < 6 or x.tm_hour > 18:
    print ('It is night-time')
else:
    print ('It is day-time')