f = open('message.txt').read().split()
flag = ''
for c in f:
    i = int(c) % 37
    if i>=0 and i<=25:
        flag+=(chr(i+65))
    elif i>25 and i<=35:
        flag+=(chr(i+22))
    else:
        flag+=("_")
print(flag)