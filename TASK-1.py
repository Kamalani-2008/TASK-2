s = input("Enter a lowercase string: ")

H = 0

print("Duplicate characters:", end=" ")

for ch in s:

    x = 1 << (ord(ch) - ord('a'))

    if (x & H) > 0:
        print(ch, end=" ")
    else:
        H = x | H