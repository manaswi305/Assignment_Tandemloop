a = int(input("Enter a number: "))
result = [2 * i - 1 for i in range(1, a + 1)]
print(", ".join(map(str, result)))
