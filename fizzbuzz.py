dau_vao = input ("Nhap vao 2 so:")
dau_vao_split=dau_vao.split(" ")
start = int (dau_vao_split[0])
end = int(dau_vao_split[1])

if start > end:
	print("So ket thuc lon hon so bat dau")
else:
	for i in range(start, end+1):
		if i%3==0 and i%5==0:
			print("fizzbuzz")
		elif i%3==0:
			print('fizz')
		elif i%5==0:
			print('buzz')
		else:
			print(i)