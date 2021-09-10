#Programa que permite calcular el IVA de un producto
#Tendra un sistema de usuario y contraseña (usuario siendo flexible y la contrasena siendo una en especifico)
#Tambien se pondra una cantidad de ese producto si se ingresa más de una cantidad

ususario = ''
contra = 'tremendo'
prod = ''
contracheck = ''
SiNo = ''
cant = 0
precio = 0
ivasumado1prod = 0
ivaseparado1prod = 0
ivasumado = 0
ivaseparado = 0

print('-------------------------------------------------')
print('Bienvenido al programa para calcular el IVA!')
print('-------------------------------------------------')
print('Comience ingresando sus datos basicos (Cualquier usuario es valido, y la pw es "tremendo")')
usuario = input("Usuario: ")
contracheck = input("Contraseña: ")

if contracheck == contra:
	print('-------------------------------------------------')
	print('Ingrese los siguientes datos acerca del producto')
	prod = input("Nombre: ")
	SiNo = input("Si Desea ingresar más de una cantidad marque Si, de lo contrario No: ")
	
	if 	SiNo == "No":

		precio = int(input("Precio (C/U): "))
		ivasumado1prod = precio * 1.21
		ivaseparado1prod = precio * 0.21

		print("El producto ", prod, "tiene individualmente un IVA separado de $", ivaseparado1prod, "y sumado al producto, un total de $", ivasumado1prod)
		input()
	else: 
		cant = int(input("Cantidad: ")) #Ahora puede calcular cantidad!
		precio = int(input("Precio (C/U): "))
		ivasumado1prod = precio * 1.21
		ivaseparado1prod = precio * 0.21
		ivasumado = (cant * precio) * 1.21
		ivaseparado = (cant * precio) * 0.21
		print("El producto ", prod, "tiene individualmente un IVA separado de $", ivaseparado1prod, "y sumado al producto, un total de $", ivasumado1prod)
		print("En ", cant, " unidades, el IVA separado del producto es de $", ivaseparado, "mientras un total sumado es de $", ivasumado) #
		print('-------------------------------------------------')
		input("Presione cualquier tecla para salir")#Para evitar que el programa se cierre al instante
else:
	print('-------------------------------------------------')
	print('Contrasena incorrecta')
	print('-------------------------------------------------')
	input("Presione cualquier tecla para salir")