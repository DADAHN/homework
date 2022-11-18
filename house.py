import turtle as t

def chu_nhat(dai,rong,mau,toa_do):
	t.penup()
	t.goto(toa_do)
	t.pendown()
	t.pencolor("blue")
	t.fillcolor(mau)
	t.begin_fill()
	for i in range(2): 
		t.fd(rong)
		t.lt(90)
		t.fd(dai)
		t.lt(90)
	t.end_fill()

khung1=chu_nhat(200, 100, "red",(0,0))
khung2=chu_nhat(200,100, "red", (100,0))
khung3=chu_nhat(200,100, "red", (0,200))
khung4=chu_nhat(200,100, "red", (100,200))

window1=chu_nhat(100, 40, "white",(30,50))
window2=chu_nhat(100, 40, "white",(130,50))
window3=chu_nhat(100, 40, "white",(30,250))
window4=chu_nhat(100, 40, "white",(130,250))

khung5=chu_nhat(200, 150, "grey",(200,0))
door=chu_nhat(120, 45, "green",(230,0))
door=chu_nhat(120, 45, "green",(275,0))


t.done()


