import time as time

gmtime = time.time()
print (f'Seconds since January 1, 1970: {gmtime:,} or {gmtime:.2e} in scientific notation')
print (time.strftime('%b %d %Y'))
