from curses.ascii import isdigit

with open('students.txt') as numbers:
    text = numbers.read()
    list = []
    sum = 0
    for i in text:
        if isdigit(i):
            sum += i
            list.append(i)
print(sum/len(list))
