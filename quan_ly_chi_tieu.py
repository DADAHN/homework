chi_tieu=[]
while True:
	pass
	def add(chi_tieu,khoan_chi):
		chi_tieu.append(khoan_chi)
	def finding_index(chi_tieu,index):
		index=-1
		for i in range(len(chi_tieu)):
			if chi_tieu[i]['name']==name:
				index = i
		return index
	def delete(chi_tieu,name):
		if finding_index(chi_tieu,name) > -1:
			del chi_tieu[finding_index(chi_tieu,name)]
		else:
			print(name + 'Không tồn tại')


	print('Bạn muốn thêm hay xoá?-\n'\
		'1. Thêm -\n'\
		'2. Xoá')
	option=int(input('Nhập 1 hoặc 2:'))

	if option == 1:
		name=input('Nhập tên khoản chi:')
		day=input('Nhập ngày chi:')
		amount=input('Nhập số tiền chi:')
		khoan_chi={'name':name,'day':day,'amount':amount}
		add(chi_tieu,khoan_chi)
	elif option ==2:
		name=input('Nhập tên muốn xoá:')
		delete(chi_tieu,name)
	else:
		print('Vui lòng nhập lại!')
	yon=input('Bạn muốn tiếp tục không?(Y/N):')
	if yon=='N':
		break

