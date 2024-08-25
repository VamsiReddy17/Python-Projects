## A company decides to give bonus to all its employees on New year. A 10% bonus on salary for all the male workers and
# 25% to females. build a programme to enter Salary and Gender(m or F) of employee.

gender = input()
salary = int(input())

if gender == 'm':
    bonus = salary * (10/100)
    print(bonus)
else:

    bonus = salary * (25 / 100)
    print(bonus)