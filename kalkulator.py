n = []
print("Author: Batyrlan Kushekbayev", end='\n')
print("--------------------------------------------------------------", end='\n')
print("Choose the action (type a number):", end='\n')
print("1. Find the average (среднее)", end='\n')
print("2. Find the most common (мода)", end='\n')
print("3. Find the median (медиана)", end='\n')
print("4. Find the sum (cумма)", end='\n')
print("5. Find the length (длина)", end='\n')
print("6. Find the square mean (среднее квадратичное)", end='\n')
print("7. Find the variance (дисперсия)", end='\n')
print("8. Find standard deviation (стандартное отклонение)", end='\n')
print("9. Combo (все сразу)", end='\n')
print("--------------------------------------------------------------", end='\n')
u = int(input())
print("Enter a series of numbers (separated by spaces):", end='\n')
n = sorted(list(map(float, input().split())))
b = len(n)
if u == 1:
    print("Average is:", sum(n) / len(n))
if u == 2:
    total = maxtotal = moda = 0 
    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            total += 1
            if(total > maxtotal):
                maxtotal = total
                moda = n[i]
        else:
            total = 0
    print("The most common is:", moda)
if u == 3:
    if(len(n) % 2 == 0):
        print("Median is:", ((n[len(n) // 2 - 1] + n[len(n) // 2]) / 2))
    else:
        print("Median is:", (n[len(n) // 2]))
if u == 4:
    print("Sum is:", sum(n))
if u == 5:
    print("Length is:", len(n))
if u == 6:
    sum = 0
    for i in range(len(n)):
        sum += n[i] ** 2
    print("Square mean is:", sum / len(n))
if u == 7:
    summ = 0
    for i in range(len(n)):
        summ += n[i] ** 2
    srkv = summ / len(n)
    sr = sum(n) / len(n)
    print("Variance is:", srkv - sr)
if u == 8:
    summ = 0
    for i in range(len(n)):
        summ += n[i] ** 2
    srkv = summ / len(n)
    sr = sum(n) / len(n)
    d = srkv - sr
    print("Standard deviation is:", d ** 0.5)
if u == 9:
    print("Average is:", sum(n) / len(n))
    total = maxtotal = moda = 0 
    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            total += 1
            if(total > maxtotal):
                maxtotal = total
                moda = n[i]
            else:
                total = 0
    if(moda == 0):
        print("The most common is all numbers")
    else:
        print("The most common is:", moda)
    if(len(n) % 2 == 0):
        print("Median is:", ((n[len(n) // 2 - 1] + n[len(n) // 2]) / 2))
    else:
        print("Median is:", (n[len(n) // 2]))
    print("Sum is:", sum(n))
    print("Length is:", len(n))
    summ = 0
    for i in range(len(n)):
        summ += n[i] ** 2
    print("Square mean is:", summ / len(n))
    summ = 0
    for i in range(len(n)):
        summ += n[i] ** 2
    srkv = summ / len(n)
    sr = sum(n) / len(n)
    print("Variance is:", srkv - sr)
    summ = 0
    for i in range(len(n)):
        summ += n[i] ** 2
    srkv = summ / len(n)
    sr = sum(n) / len(n)
    d = srkv - sr
    print("Standard deviation is:", d ** 0.5)
elif(u > 9):
    print("ERROR 404")
       # if n[i] != n[i + 1]:
        #    r.append(n[i])
   # r.append(n[len(n) - 1])
    #for i in range(len(r)):
    #    answer.append(r[i] ** 2)
    #print(answer)
