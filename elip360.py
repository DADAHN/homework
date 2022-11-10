import turtle as t

n=t.Screen()
n.bgcolor('black')	
t.speed(0)
t.pensize(3)


r=100
color=['red','yellow','blue','green','brown','violet']

for i in range(0,360,10):
	t.rt(10)
	cnt=0
	t.color(color[i//10%len(color)])
	while cnt<2:
		t.circle(r,90)
		t.circle(r//2,90)
		cnt+=1
t.done()