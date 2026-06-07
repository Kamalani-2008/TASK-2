s = input()

H = 0

for ch in s:

    if 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')

    elif 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a') + 26

    elif '0' <= ch <= '9':
        pos = ord(ch) - ord('0') + 52

    else:
        continue

    H |= (1 << pos)

# Mask with first 62 bits set
ALL = (1 << 62) - 1

if H == ALL:
    print("YES")
else:
    print("NO")