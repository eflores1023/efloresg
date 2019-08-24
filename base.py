#Autores: Esteban Andres Flores Gutierrez y Camila Fernanda Guzman Lara

import math

######### ASSERT AL FINAL DEL CODIGO

def esNumero(numero, base):
    if base >= 2 and base <= 9:
        def validar(numero, base):
            dig= numero/10
            res= numero%10
            if res>=base:
                n1= bool(0)
                return n1
            elif dig != 0:
                return validar(dig, base)
            else:
                n1 = bool(10)
                return n1
            return validar(numero, base)
    
        n = validar(numero, base)
        return n

    else:
        return "Ingrese base entre 2 y 9."

def decimal(numero,base):
    def decimal1(numero,base,exp):
        digito=numero%10
        var=numero/10
        if var==0:
            return digito*base**exp
        else:
            return digito*base**exp+decimal1(var,base,exp+1)

    assert esNumero(numero,base) 
    return decimal1(numero,base,0)


def cambio(numero,base):
    def cambio1(numero,base,exp):
        digito=numero%base
        var=numero/base
        if var==0:
            n=digito*10**exp
            return n
        else:
            n= digito*10**exp+cambio1(var,base,exp+1)
            return n

    assert esNumero(numero,10) 
    return cambio1(numero,base,0)

"""print "----------------P A R T E     A--------------"
print "EJEMPLOS VALIDACION DE       B A S E S       "
print "Ejemplo1 enunciado esNumero(102,3): " +str(esNumero(int(102),int(3)))
print "Ejemplo2 enunciado esNumero(102,2): "+str(esNumero(int(102),int(2)))
print "Exempli gratia 1 esNumero(10729,2): "+str(esNumero(int(10729),int(2)))
print "Exempli gratia 2 esNumero(1054722,8): "+str(esNumero(int(1054722),int(8)))
print "Exempli gratia 3 esNumero(10776382,8): "+str(esNumero(int(10776382),int(8)))
print "Ejemplo error esNumero(1054722,12): "+str(esNumero(int(1054722),int(12)))
print "---------------------------------------------"
print " "
print "----------------P A R T E     B--------------"
print "Entregar un numero (arg1) dado en la base del segundo argumento y escribirlo en base diez."
print "Ejemplo1 enunciado decimal(215,8): "+str(decimal(215,8))
print "Exempli gratia 1 decimal(764,9): "+str(decimal(764,9))
print "Exempli gratia 2 decimal(10110,2): "+str(decimal(10110,2))
print "Exempli gratia 3 decimal(523,7): "+str(decimal(523,7))
print "Exempli gratia 4 decimal(413,5): "+str(decimal(413,5))
print "---------------------------------------------"
print " "
print "----------------P A R T E     C--------------"
print "Entregar un numero en base diez (arg1) y escribirlo en la base del segundo argumento."
print "Ejemplo1 enunciado cambio(431,8): "+str(cambio(431,8))
print "Exempli gratia 1 cambio(431,6): "+str(cambio(431,6))
print "Exempli gratia 2 cambio(785,9): "+str(cambio(785,9))
print "Exempli gratia 3 cambio(22,2) (Verificar con Exempli 2  P A R T E     B): "+str(cambio(22,2))
print "Exempli gratia 4 cambio(312,4): "+str(cambio(312,4))
print "---------------------------------------------" """


assert esNumero(int(102),int(3))==True
assert esNumero(int(102),int(2))==False
assert esNumero(int(10729),int(2))==False
assert esNumero(int(1054722),int(8))==True
assert esNumero(int(10776382),int(8))==False

####################################################

assert decimal(215,8)== 141
assert decimal(764,9)== 625
assert decimal(10110,2)== 22
assert decimal(523,7)== 262
assert decimal(413,5)== 108

###################################################

assert cambio(431,8) == 657
assert cambio(431,6) == 1555
assert cambio(785,9) == 1062
assert cambio(22,2) == 10110
assert cambio(312,4) == 10320








