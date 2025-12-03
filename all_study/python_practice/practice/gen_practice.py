def nums_0_59():
    num=0
    while num <= 59:
        yield num   # Pauses execution here and returns the value
        num += 1
        if num==60:
            num=0
def nums_0_23():
    num=0
    while num <=23:
        yield num
        num+=1
        if num==24:
            num=0

gen_sec = nums_0_59()
gen_min = nums_0_59()
gen_hour = nums_0_23()

def gen_time_func(s,m,h):
    seconds=next(s)
    minutes=next(m)
    hours=next(h)
    while(seconds<=59):
        time_string = "%02d:%02d:%02d" % (hours, minutes, seconds)
        yield time_string
        seconds=next(s)
        if(seconds==0):
            minutes=next(m)
            if(minutes==0):
                hours=next(h)

gen_time=gen_time_func(gen_sec,gen_min,gen_hour)

def gen_years_func(year=2010):
    while True:
        yield year
        year+=1
def gen_months_func():
    month=1
    while True:
        yield month
        month+=1
        if month==13:
            month=1
def gen_days_func():
    day=1
    while True:
        yield day
        day+=1
        if day==31:
            day=1
def gen_date_func(D,M,Y):
    days=next(D)
    months=next(M)
    year=next(Y)
    while(days<=30):
        date_string = "%02d/%02d/%04d" % (days, months, year)
        yield date_string
        days=next(D)
        if(days==1):
            months=next(M)
            if(months==1):
                year=next(Y)
  

def gen_full_date_func(g_d,g_t):
    date=next(g_d)
    time=next(g_t)
    yield f"{date} {time}"
    while True:
        time=next(g_t)
        if(time=='00:00:00'):
            date=next(g_d)
        yield f"{date} {time}"
full_time=gen_full_date_func(gen_date_func(gen_days_func(),gen_months_func(),gen_years_func()),gen_time_func(gen_sec,gen_min,gen_hour))

        


def manual_clock_gen(start_year=2010):
    year = start_year
    while True: # Infinite loop for years
        # Months (1 to 12)
        for month in range(1, 13):
            # Days: Simple logic (30 days) - Complex logic would need a lookup table
            max_days = 31 if month in [1,3,5,7,8,10,12] else 30 
            if month == 2: max_days = 28 # Ignoring leap years for simplicity here
            
            for day in range(1, max_days + 1):
                for hour in range(24):
                    for minute in range(60):
                        for second in range(60):
                            yield f"{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}"
        
        year += 1 # Increment year after months loop finishes

# Usage
gen = manual_clock_gen()

# Burn through some values to show it works
for i in range(500000):
    next(gen)
    if i%10000==0: print(next(gen))