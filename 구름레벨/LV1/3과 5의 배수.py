# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())
result = 0

for i in range(1,user_input + 1):
	if i % 3 == 0 or i % 5 == 0:
		result += i		
		
print(result)
