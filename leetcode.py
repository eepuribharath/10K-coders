num = input("Enter a number: ")

n = int(num) + 1

result = []

for digit in str(n):
    result.append(int(digit))

print("Result:", result)