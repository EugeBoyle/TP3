#Programa que permite calcular el IVA de un producto
#Tendra un sistema de usuario y contrasena (usuario siendo flexible y la contrasena siendo una en especifico)
#Tambien se podra una cantidad de ese producto si se ingresa mas de 1 cantidad

ususario = ''
contra = 'tremendo'
prod = ''
contracheck = ''
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
contracheck = input("Contrasena: ")

if contracheck == contra:
	print('-------------------------------------------------')
	print('Ingrese los siguientes datos acerca del producto')
	prod = input("Nombre: ")
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