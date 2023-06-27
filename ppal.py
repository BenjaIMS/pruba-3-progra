import funciones as fn 
nombre=[]
rut=[]
annionacimiento=[]
categoria=[]
celular=[]
pareja=[]
correos=[]
opc=0
while opc!=4:
    opc=fn.menu()
    if opc==1:
        nombre,rut,annionacimiento,categoria,celular,pareja,correos=fn.agregarJugador(nombre,rut,annionacimiento,categoria,celular,pareja,correos)
    elif opc==2:
        fn.mostrarJugador(nombre,rut,categoria,celular,correos)
    elif opc==3:
        fn.imprimirParejas(rut,nombre,pareja)
    else:
        fn.salir()
        break
    