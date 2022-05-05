while True:
    num = input()
    if num=="0":
        break
    length = len(num)
    is_penlindrom = "yes"
    for i in range(length//2):
        if num[i] != num[length-i-1]:
            is_penlindrom = "no"
            break
    print(is_penlindrom)
