import turtle as t

#setup bút vẽ:
t.shape('turtle')
t.pensize(2)
t.colormode(255)
t.pencolor(102,178,255)
t.speed(0)

#hàm vẽ hình chữ nhật:
def chu_nhat(dai,rong,toa_do):
	t.penup()
	t.goto(toa_do)
	t.pendown()
	for i in range(2):
		t.fd(dai)
		t.lt(90)
		t.fd(rong)
		t.lt(90)

#hàm vẽ hình tam giác:
def tam_giac(toa_do,mau,canh):
	t.penup()
	t.goto(toa_do)
	t.pendown()
	t.fillcolor(mau)
	t.begin_fill()
	for i in range(3):
		t.fd(canh)
		t.rt(120)
	t.end_fill()

#vẽ hình thang cân:
def thang_can(toa_do,day_nho,day_lon,duong_cheo):
	t.pencolor(102,178,255)
	t.penup()
	t.goto(toa_do)
	t.pendown()
	t.fillcolor('grey')
	t.begin_fill()
	t.fd(day_nho)
	t.rt(80)
	t.fd(duong_cheo)
	t.rt(100)
	t.fd(day_lon)
	t.rt(100)
	t.fd(duong_cheo)
	t.end_fill()

#Vẽ nhà:
##Khung:
chu_nhat(400,200,(-100,-100))
##Cửa:
chu_nhat(80,130,(60,-100))
##ống khói:
chu_nhat(20,130,(60,100))
##mái:
t.rt(60)
tam_giac((0,273.2050807568877),'white',200)

#cay1:
##ngoncay
t.pencolor(102,204,0)
tam_giac((-230,0),(204,255,153),80)
tam_giac((-230,-69.2820323028),(0,153,76),120)
tam_giac((-230,-173.205080757),(0,51,0),160)
##thancay
t.lt(60)
thang_can((-250,-311.769145362),40,74.7296355334,100)

#cay2:
t.rt(80)
t.rt(60)
t.penup()
t.goto(500,200)
##ngoncay
t.pencolor(102,204,0)
tam_giac((500,200),(204,255,153),50)
tam_giac((500,156.698729811),(0,153,76),90)
tam_giac((500,78.7564434702),(0,51,0),120)
##thancay
t.lt(60)
thang_can((485,-25.166604984),30,54.3107448734,70)




t.done()