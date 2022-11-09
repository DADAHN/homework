import turtle as t
cnt=0
n=0.2
while cnt<200:
	t.fd(n)
	t.lt(20)
	t.fd(n+1)
	n+=1
	t.lt(1)
	cnt+=1
t.done()