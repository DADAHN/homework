str=input("Nhập chuỗi:")
def count(str):
    chars=0
    for char in str:
        chars += 1
    return chars
print("Độ dài chuỗi là:",count(str))