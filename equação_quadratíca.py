from math import sqrt
from time import sleep
def li(tam=32):
	print('='*tam)
		
def es(msg):
	print(msg)

def cal(a=0, b=0, c=0):
	li()
	es('Cálculo de Equacão quadrática\nDo Tipo: ax²+bx+c=0')
	com = b**2-4*a*c
	raiz = sqrt(com)
	li()
	es(f'O valor do \033[33m∆={com}\033[m')
	es('\033[1;40;mcalculando X½\033[m')
	li()
	sleep(1)
	x1 = -b+raiz
	x2 = -b-raiz
	cal1 = x1/2*a
	cal2 = x2/2*a
	cx1 = int(cal1)
	cx2 = int(cal2)
	es(f'As raizes da equaçao\nX1 = \033[32m{cx1}\033[m\nX2 = \033[32m{cx2}\033[m')
	li()

cal(1,4,-5)


