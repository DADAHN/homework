num1=int(input("Nhập vào số thứ nhất:"))
num2=int(input("Nhập vào số thứ hai:"))
num3=int(input("Nhập vào số thứ ba:"))

def sap_xep(num1,num2,num3):
    if num1<=num2<=num3:
        print("Thứ tự từ nhỏ đến lớn là:{},{},{}".format(num1,num2,num3))
    elif num1<=num3<=num2:
        print("Thứ tự từ nhỏ đến lớn là:{},{},{}".format(num1,num3,num2))
    elif num2<=num1<=num3:
        print("Thứ tự từ nhỏ đến lớn là:{},{},{}".format(num2,num1,num3))
    elif num2<=num3<=num1:
        print("Thứ tự từ nhỏ đến lớn là:{},{},{}".format(num2,num3,num1))
    elif num3<=num1<=num2:
        print("Thứ tự từ nhỏ đến lớn là:{},{},{}".format(num3,num1,num2))
    else:
        print("Thứ tự từ nhỏ đến lớn là:{},{},{}".format(num3,num2,num1))
sap_xep(num1,num2,num3)
        

        