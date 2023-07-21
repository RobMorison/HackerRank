# def avg (arguments):
#     total_sum = 0
#     for number in arguments:
#         total_sum += arguments
#     return(total_sum)

# avg(10)

# n = 6

# if n % 2 == 0 and n >1 and n <6:
#     print('not weird')
# elif n >1 and n <6:
#     print('wierd')
# else:
#     print('number out of range select a number 2-5')

# a = 2
# b = 4
# c = a - b

# print (c)
# print (b)

# a = 3
# b = 5

# c = 3 // 5
# d = 3 / 5

# print(c)
# print (d)

# n = 4

# for i in range (n):
#     print (i+1,end='')

# n = 4

# for i in range(n):
#     print(i * i)

# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the 
# fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source



def is_leap(year):
    leap = False

    if year % 4 == 0:
        
        if year % 100 == 0:

      
            if year % 400 == 0:
                leap = True

            else:
                return leap
        
        else:
            return leap
    
    
    else:
        return leap



    return leap

is_leap(2100)
    