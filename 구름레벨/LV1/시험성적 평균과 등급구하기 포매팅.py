arr = list(map(float,input().split(" ")))

result = sum(arr)

answer = round(result/3,2)

print(format(answer,".2f"), end =" ")



if answer >= 90:
	print("A")
elif answer >= 80:
	print("B")
elif answer >= 70:
	print("C")
elif answer >= 60:
	print("D")
else:
	print("F")
