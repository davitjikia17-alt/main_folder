def get_num():
    try:
        num = int(input("please enter a number: "))
    except Exception as e:
        print(f"oh no what did you do??? {e}")
        return 0
    return num
num=get_num()
print(num)