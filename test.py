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



# def is_leap(year):
#     leap = False

#     if year % 4 == 0:
        
#         if year % 100 == 0:

      
#             if year % 400 == 0:
#                 leap = True
#                 return leap

#             else:
#                 return leap
        
#         else:
#             return leap
    
    
#     else:
#         return leap

# is_leap(2100)


# s = 'hello openGeNus'
# t = s.title()

# print(t)

# x = 1
# y = 1
# z = 2
# n =3

# if [x + y + z] == n:
#     print('hello')
# else:
#     print('nope')

# N = []

# N.insert(0, 5)
# N.insert(1, 10)
# N.insert(0, 6)
# print(N)
# N.remove(6)
# N.append(9)
# N.append(1)
# N.sort()
# print(N)
# N.pop(-1)
# N.reverse()
# print(N)

SELECT NAME FROM STUDENTS WHERE MARKS > 75;

SELECT (months * salary) as total_earnings FROM EMPLOYEES;


Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
    select distinct city from station where left (city,1) not in ('a','e','i','o','u') and right(city,1) not in ('a','e','i','o','u')
 