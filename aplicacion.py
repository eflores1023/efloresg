#Autores: Esteban Andres Flores Gutierrez y Camila Fernanda Guzman Lara

import base

def ConvertirAbase(bf):

    fin= 'Fin de la funcion '+str('ConvertirAbase')
    basef=bf
    bi= input('Base inicial: ')
    if basef==bi or bi < 2 or bi > 10:
        print 'Ingrese base correcta.'

    else:
        numero= input('Ingrese numero: ')
        if base.esNumero(numero, bi)== False:
            print 'Ingrese numero y base correcta.'
        
        else:
            ni=base.decimal(numero,bi)
            nf=base.cambio(ni,basef)
            print nf
        
    q=raw_input('Otra conversion? (si/no): ')
    if q.lower()== 'si':
        return ConvertirAbase(basef)
    elif q.lower()== 'no':
        print '\n'
        print fin
        return 0
    else:
        print 'Si desea otra conversion, responda con si/no. De lo contrario, se finalizara la funcion.'


def Mayor(mayor=0, var=0, var2=0):

    gigante= mayor
    basemayor= var
    numayor=var2
    
    dig= input('Ingrese numero: ')
    
    if dig == int(0):
        print 'Decimal: ' + str(gigante) + ' ; ' + 'Base: ' +str(var)+' ; ' 'Numero: ' +str(var2)
        print '\n'
        print 'Fin de la funcion'+str('Mayor')
        return 0
        
    else:
        numero= dig/10
        bas= dig%10

        if bas < 2:
            print "Ingrese base correcta"

        elif base.esNumero(numero,bas) == False:
            print "Numero incorrecto"

        else:
            final= base.decimal(numero,bas)
            print "Decimal: "+str(final)

            if final > gigante:
                gigante = final
                basemayor= bas
                numayor = numero
            else:
                basemayor= var
                numayor=var2

        return Mayor(gigante, basemayor, numayor)



print "****************************************************"
print "***** Ejemplo de la funcion ConvertirAbase(2) ******"
print "****************************************************"
ConvertirAbase(2)
print "************************************************"
print '\n'
print "************************************************"
print '\n'
print "****************************************************"
print "***** Ejemplo de la funcion ConvertirAbase(6) ******"
print "****************************************************"
ConvertirAbase(6)
print "************************************************"
print '\n'
print "************************************************"
print '\n'
print "*************************************************"
print "********** Ejemplo de la funcion Mayor **********"
print "*************************************************"
Mayor()
print "************************************************"
print '\n'
print "************************************************"
print '\n'
print 'F i n \t d e l \t p r o g r a m a'






