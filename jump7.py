for a in range(1,101):
    if a % 10 == 7:
        continue
    elif a % 7 == 0:
        continue
    elif a >= 70 and a <= 79:
        continue
    else:
        print(a)
