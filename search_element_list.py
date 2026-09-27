numbers = list(map(int, input("Enter numbers: ").split()))

search = int(input("Enter element to search: "))

if search in numbers:
    print(search, "is present in the list.")
else:
    print(search, "is not present in the list.")
