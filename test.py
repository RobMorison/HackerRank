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

# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.


# def print_full_name(first, last):
#     print(f'Hello {first} {last}! You just delved into python.')

# print_full_name('rob', 'morison')

# SELECT NAME FROM STUDENTS WHERE MARKS > 75;

# SELECT (months * salary) as total_earnings FROM EMPLOYEES;


Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
    select distinct city from station where left (city,1) not in ('a','e','i','o','u') and right(city,1) not in ('a','e','i','o','u')
 

Query the Name of any student in STUDENTS who scored higher than 75 Marks. Order your output by the last three characters of each name. 
If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
    SELECT NAME FROM STUDENTS WHERE MARKS > 75 ORDER BY RIGHT(NAME, 3), ID ASC;

Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
    SELECT NAME FROM EMPLOYEE ORDER BY NAME;

Write a query that prints a list of employee names (i.e.: the name attribute)
for employees in Employee having a salary greater than 2000 per month who have been employees for less than 10 months. Sort your result by ascending employee_id.
    SELECT NAME FROM EMPLOYEE WHERE SALARY > 2000 AND MONTHS < 10 ORDER BY EMPLOYEE_ID;

Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
    SELECT DISTINCT CITY FROM STATION WHERE LEFT (CITY,1) IN ('A','E','I','O','U');

Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
    SELECT DISTINCT CITY FROM STATION WHERE RIGHT (CITY,1) IN ('a','e','i','o','u');

Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
    SELECT DISTINCT CITY FROM STATION WHERE LEFT (CITY,1) IN ('A','E','I','O','U') AND RIGHT (CITY,1) IN ('a','e','i','o','u');

Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
    SELECT DISTINCT CITY FROM STATION WHERE LEFT (CITY,1) NOT IN ('A','E','I','O','U');

Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
    SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY), CITY LIMIT 1;
    SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY) DESC LIMIT 1;

Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
    SELECT DISTINCT CITY FROM STATION WHERE RIGHT (CITY,1) NOT IN ('a','e','i','o','u');

Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
    SELECT DISTINCT CITY FROM STATION WHERE LEFT (CITY, 1) NOT IN ('A', 'E', 'I', 'O', 'U') OR RIGHT (CITY, 1) NOT IN ('a', 'e', 'i', 'o', 'u');

Query a count of the number of cities in CITY having a Population larger than 100,000.
    SELECT COUNT(NAME) FROM CITY WHERE POPULATION > 100000;

Query the total population of all cities in CITY where District is California.
    SELECT SUM(POPULATION) FROM CITY WHERE DISTRICT = 'California' ;

Query the average population of all cities in CITY where District is California.
    SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = 'California';