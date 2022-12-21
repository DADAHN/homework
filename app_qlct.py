from tkinter import *
from tkinter.ttk import *
from tksheet import Sheet 
import csv
import tkinter.font as font
import tkinter as tk
from PIL import ImageTk,Image


#Khởi tạo
root=Tk()
root.title("Quản lý chi tiêu")
root.geometry("645x500")
root.resizable(False, False)

#Background:
image=Image.open('/Users/longnguyenhoang/Desktop/BTVN/bg.jpeg')
resize_image=image.resize((645, 500))
bg=ImageTk.PhotoImage(resize_image)
label1 = Label(image=bg).place(x=0,y=0)

#Biến chứa dữ liệu khoản chi:
data=[]

#hàm xuất file csv:
def export_file():
    header=['Ngày chi','Tên khoản chi','Số tiền chi']
    path=open('/Users/longnguyenhoang/Desktop/BTVN/app_qlct.csv','w')
    writer=csv.writer(path)
    writer.writerow(header)
    writer.writerows(data)

#Hàm thêm,xem,đặt lại,xoá:
def add():
    data.append([Date.get(),Name.get(),Amount.get()])
    export_file()
    sheet.set_sheet_data(data)
def view():
    data_view=[] 
    for i in range(len(data)):
        if data[i][1]==Name.get():
            data_view.append(data[i])
    print(data_view)
    sheet.set_sheet_data(data_view)
            #Date.set(data[i][0])
            #Name.set(data[i][1])
            #Amount.set(data[i][2])
def reset():
    sheet.set_sheet_data(data)        
def delete():
    for i in range(len(data)):
        if data[i][1]==Name.get() and data[i][0]==Date.get():
            del data[i]
    export_file()
    sheet.set_sheet_data(data)

#Textvariable,Label,Entry Ngày, Tên, Số tiền của khoản chi:
##Textvariable:
Date=StringVar()
Name=StringVar()
Amount=StringVar()
##Date:
frame1=tk.Frame(root,bg='black',highlightthickness = 2,highlightbackground = "yellow")
frame1.grid(row=0,column=0,pady=10,padx=10)
date_lbl=tk.Label(frame1,text="Ngày chi tiêu",bg='black',fg="white",font=('Helvetica',16)).pack()
date_inp=tk.Entry(frame1,textvariable=Date).pack()
##Name:
frame2=tk.Frame(root,bg='black',highlightthickness = 2,highlightbackground = "yellow")
frame2.grid(row=0,column=1,pady=10,padx=10)
name_lbl=tk.Label(frame2,text="Tên khoản chi",bg='black',fg="white",font=('Helvetica',16)).pack()
name_inp=tk.Entry(frame2,textvariable=Name,bg='white').pack()
##Amount
frame3=tk.Frame(root,bg='black',highlightthickness = 2,highlightbackground = "yellow")
frame3.grid(row=0,column=2,pady=10,padx=10)
amount_lbl=tk.Label(frame3,text="Số tiền chi",bg='black',fg="white",font=('Helvetica',16)).pack()
amount_inp=tk.Entry(frame3,textvariable=Amount,bg='white').pack()

#Nút thêm,xem,đặt lại,xoá:
frame4=tk.Frame(root,highlightthickness = 2,highlightbackground = "yellow",relief="raised")
frame4.grid(row=1,column=1)
buttonFont = font.Font(family='Helvetica', size=15,weight='bold')
##Nút Thêm:
add_btn=tk.Button(frame4,text="Thêm",command=add,height=3,width=3,activeforeground="white",
                  highlightcolor='black', font=buttonFont,fg='green',relief="raised",bg="yellow").pack(side=TOP,fill=BOTH)
##Nút Xem:
view_btn=tk.Button(frame4,text="Xem",command=view,height=3,width=3,activeforeground='white',
                   font=buttonFont,relief="raised",bg="blue").pack(side=LEFT)
##Nút Xoá:
delete_btn=tk.Button(frame4,text="Xoá",command=delete,height=3,width=3,activeforeground='white',
                     font=buttonFont,fg='red',relief="raised",bg="blue").pack(side=LEFT)
##Nút Đặt lại:
update_btn=tk.Button(frame4,text="Đặt lại",command=reset,height=3,width=3,activeforeground='white',
                     font=buttonFont,fg='grey',relief="raised",bg="blue").pack(side=LEFT)


#Bảng thông tin khoản chi:
frame5=Frame(root)
frame5.grid(row=2,column=0,columnspan=3,padx=10,pady=10)
sheet = Sheet(frame5,
              column_width=150,
              width=510,
              total_columns=3,total_rows=len(data),
              show_x_scrollbar=False,
              outline_thickness=2,
              outline_color='yellow',
              header_height='1',
              header_font=('Helvetica'),
              popup_menu_fg = "dark blue",
              #change_theme(theme = "light blue"),
              theme= "dark",
              headers=["Ngày chi tiêu","Tên khoản chi","Số tiền chi"]
              )
##sheet.enable_bindings()
##sheet.set_sheet_data(data)
sheet.pack()


root.mainloop()