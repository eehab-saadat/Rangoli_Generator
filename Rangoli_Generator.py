def print_rangoli():
    import string
    alphabets = string.ascii_lowercase
    
    LIST = []
    for i in range(size):
        s = "-".join(alphabets[i:size])
        LIST.append((s[::-1]+s[1:]).center(4 * size - 3 , "-"))
    print("\nHere's your Rangoli:\n")
    print('\n'.join(LIST[:0:-1] + LIST))

print("Welcome to Rangoli Generator!")
size = int(input("Enter Integeral Size of Rangoli: "))
print_rangoli()