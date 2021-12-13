a = float(input("請輸入x的2次方的系數= "))
b = float(input("請輸入x的1次方的系數= "))
c = float(input("請輸入常數= "))

s = (b**2)-(4*a*c)

if s == 0 :
    x = (-b-((b**2)-(4*a*c))**0.5)/(2*a)
    print(f"該方程式重根 x = {x}")
elif s>0:
    x1 = (-b-((b**2)-(4*a*c))**0.5)/(2*a)
    x2 = (-b+((b**2)-(4*a*c))**0.5)/(2*a)
    print(f"該方程式有兩個根 x = {x1} 及 {x2}")
else:
    print("該方程式沒有實數解")
