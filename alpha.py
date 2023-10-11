def print_alphabet_pattern(letter, n):
    if letter == 'A':
        for i in range(n):
            if i == n // 2:
                print("*" * n)
            else:
                print(" " * (n // 2 - i) + "*" + " " * (i * 2 - 1) + "*" if i > 0 else "*" * n)
    elif letter == 'B':
        for i in range(n):
            if i == 0 or i == n // 2 or i == n - 1:
                print("*" * n)
            else:
                print("*" + " " * (n - 2) + "*")
    elif letter == 'C':
        for i in range(n):
            if i == 0 or i == n - 1:
                print(" " * (n - 1) + "*")
            else:
                print("*")

# Enter the alphabet and size (n) you wish to print
desired_letter = input("Enter the alphabet you wish to print: ")
size = int(input("Enter the size (n) of the alphabet pattern: "))
print_alphabet_pattern(desired_letter, size)