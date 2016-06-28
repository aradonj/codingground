numb = int(input("Enter the number whose divisors would like to be known:"))
x = []
y = []
for i in range(1, (numb+1)):
    x.append(i)
for element in x:
    if ((numb % element) == 0):
        y.append(element)
print(y)