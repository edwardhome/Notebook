print("=========")
print("歡迎來到一隻只有除法的程式")
print("=========")
i = 0
while True:
    i += 1
    try:
        try:
            a = int(input("輸入數值a= "))
            b = int(input("輸入數值b= "))
        except ValueError:
            print("=========")
            print("請重新輸入正確的數值")
            print("=========")
            continue

        try:
            c = a / b 
            print("=========")
            print(f'答案等於{c}')
            print("=========")
        except ZeroDivisionError:
            print("無法除以零")
    except KeyboardInterrupt:
        print("\n")
        print("謝謝使用")
        break
    
print(f"本程式總共被使用了{i}次")
exit()