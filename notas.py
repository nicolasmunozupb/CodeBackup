n1=float(input("ingrese valor nota1"))
n2=float(input("ingrese valor nota2"))
n3=float(input("ingrese valor nota3"))
n4=float(input("ingrese valor nota4"))
n5=float(input("ingrese valor nota5"))

final=float((n1*0.1)+(n2*0.15)+(n3*0.25)+(n4*0.15)+(n5*0.35))

if final>=3.0:
	if final>4.5:
		print("buen trabajo, eres un estudiante destacado y tu nota es", final)
	else:
		print("aprobo y su nota es ",final)
else:
	if final<2.0:
		print("no puede habilitar la asignatura y su nota es", final)
	else:
		print("Debe habilitar la signatura y su nota es", final)
