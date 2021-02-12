n = 234
prodact = int(n/100) * int(n/10%10) * int(n%10)
sum = int(n/100) + int(n/10%10) + int(n%10)
result = prodact - sum
print(result)