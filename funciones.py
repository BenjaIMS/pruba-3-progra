def menu():
    print("-"*50)
    print("Bienvenido a Padel Duoc")
    print("-"*50)
    print("1.- Grabar jugador")
    print("2.- Buscar jugador")
    print("3.- Imprimir Parejas")
    print("4.- Salir")
    return validaNro(int,"Selecciones su opcion:  ",1,4)

def validaNro(tipo,texto,rMin=None,rMax=None):
    while True:
        try:
            nro=tipo(input(texto))
            if rMin != None and rMax!=None:
                if rMin<=nro<=rMax:
                    break
                else:
                    print("Fuera de rango!!")
            elif rMin!= None:
                if rMin<=nro:
                    break
                else:
                    print(f"El valor mínimo puede ser {rMin}")
            elif rMax!= None:
                if nro<=rMax:
                    break
                else:
                    print(f"El valor maximo puede ser {rMax}")
            else:
                break
        except:
            print("Se esperaba un N°!!")
    return nro

def validaLen(texto,large,estricto):
    while True:
        entrada=input(texto)
        if estricto:
            if len(entrada)==large:
                break
            else:
                print(f"El largo debe ser igual a {large}")
        else:
            if len(entrada)>=large:
                break
            else:
                print(f"El largo mínimo es {large}")
    return entrada

def validaGmail():
    while True:
        correo=validaLen("Ingrese su correo:  ",6,False)
        if '@' in correo:
            if '.' in correo:
                break
            else:
                print("Falta el punto (.) dentro del correo!")
        else:
            print("Falta el (@) dentro del correo!!")
    return correo

def agregarJugador(nombre,rut,annionacimiento,categoria,celular,pareja,correos):
    
    nombre.append(validaLen("Ingrese su nombre: ",2,False))
    rut.append(validaNro(int,"Ingrese su Rut sin CV:  ",5000000,99000000))
    annionacimiento.append(validaNro(int,"Ingrese año de nacimiento: ",1943,2008))
    categoria.append(validaCategoria())
    celular.append(validaLen("Ingrese su celular:  ",9,True))
    pareja.append(validaLen("Ingrese el nombre de su pareja:  ",2,False))
    correos.append(validaGmail())
    print("Se ha registrado de forma correcta!!")
    return nombre,rut,annionacimiento,categoria,celular,pareja,correos

def validaCategoria():
    while True:
        cate=validaLen("Escriba su categoria: \n-ORO \n-PLATA \n-BRONCE \n-->",3,False).upper()
        if cate=='ORO':
            break
        elif cate=='PLATA':
            break
        elif cate=='BRONCE':
            break
        else:
            print("Ingrese una categoria disponible!!")
    return cate

def mostrarJugador(nombre,rut,categoria,celular,correos):
    if len(rut)!=0:
        jugador=validaNro(int,"Ingrese el Rut sin CV del jugador que desea buscar:  ",5000000,99000000)
        for a in range(len(rut)):
            if jugador==rut[a]:
                print(f"Nombre: {nombre[a]} | Categoria: {categoria[a]} | Celular: {celular[a]} | Correo: {correos[a]}")
    else:
        print("Aun no se han registrado jugadores!!")

def imprimirParejas(rut,nombre,pareja):
    if len(rut)!=0:
        jugador=validaNro(int,"Ingrese el Rut  sin CV del jugador para concer su pareja:  ",5000000,99000000)
        for a in range(len(rut)):
            if jugador==rut[a]:
                print(f"Nombre: {nombre[a]} | Pareja: {pareja[a]}")
    else:
        print("Aun no se han registrado jugadores!!")
   
def salir():
    print("Que tenga buen dia!! \nAtte: Benjamin Marchant")
    