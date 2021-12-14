def try_test(obj):
	try:
		a = float(obj)
	except (ValueError, TypeError):
		a = "異常產生，輸入資訊必為數字或可轉浮點數之字串\n"
	else:
		print(f"確認執行，輸入的類型為{type(obj)}，將其轉化為{type(a)}")
	print(a)
	return a

try_test("fdsa")
try_test(123.5)
try_test(1)
try_test("0.58")
