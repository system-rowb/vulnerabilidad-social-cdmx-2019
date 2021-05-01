from vulnerabilidad_social_cdmx_core import * #importa todas las variables del documento 'Evidencia_V3'
import matplotlib.pyplot as plt  #importa matplotlib 

print('               ********** !BIENVENIDO! **********               '+'\n'+
      ' > Seleccione la opción de su preferencia y al terminar, se le redigirá al menú principal.'+'\n'+
      ' >> Para salir del programa digite 5.'+'\n')#imprime str
###
cond = True#Pone una condicional para hacer un loop en el que cuando el usuario realice su elección, lo envie nuevamente al menu
while cond:
    print('Atlas de Vulnerabilidad Social de la Ciudad de México [DATABASE]'+ '\n>')#imprime str
    o1 = str(' ||1|| Información de la Vulnerabilidad Social en términos generales [Ciudad Completa]')#define la variable de opcion 1
    o2 = str(' ||2|| Información de la Vulnerabilidad Social en términos de [Alcaldías]')#define la variable de opcion2
    o3 = str(' ||3|| Información de la base de datos para este proyecto')#define la variable de opcion3
    o4 = str(' ||4|| Créditos')#define la variable de opcion4
    o5 = str(' ||5|| Salir')#define la variable de opcion5


    print(o1 + '\n' + o2  + '\n' + o3 + '\n' + o4 + '\n' + o5 + '\n')#imprime todas las opciones
    a = int(input('|Digita el número de tu elección|'))#pide un digito para seleccionar las opciones
    #si respuesta es igual a 1
    if a == 1:
        sep(o1)#imprimir separacion de opcion1
        cdmx_desc_gen()#ejecutar variable cdmx_desc_gen
    #si respuesta es igual a 2
    elif a == 2:
        sep(o2)#imprime separacion de opcion2 
        print(' >')
        o1 = ' ||1|| Resumen general de alcaldias [Todas las alcadias]'#define la variable de opcion1
        o2 = ' ||2|| Información individual de la alcaldía [Seleccionar alcaldía]'#define la variable de opcion2
        print(o1 + '\n'+
                o2 + '\n')#imprime las dos opciones
        a = int(input(' >|Selecciona la elección de tu preferencia|'))#pide un digito para seleccioanr opciones
        #si respuesta es 1 
        if a == 1:
            sep(o1)#Imprime separacion de opcion1
            total_alcaldias_descr_intensidad()#ejecuta la variable total_alcaldias_Descr_intensidad
        elif a == 2:#si respuesta es 2 
            sep(o2)#imprime separacion de opcion2
            descrp_x_alc()#ejecuta variable descrp_x_alc
        else:#si la respuesta no es las anteriores
            print(error)#imprimir variable error
    elif a == 3:#si la respuesta es 3
        sep(o3)#imprime separacion de operacion 3
        time.sleep(2)#se espera 2 segundos
        db_info()#ejecuta la variable db_info
        time.sleep(5)#se espera 5 segundos
    elif a == 4:#si la respuesta es 4
        sep(o4)#imprime separcion de opcion4
        time.sleep(2)#se espera 2 segundos
        print(' > Este proyecto fue desarrollado por y con el apoyo de:' + '\n')#imprime str
        time.sleep(2)#se esper 2 segundos
        print("""> Thamara
> Jorge
> Emilio
> Pedro
> Roberto""")#imprime los nombres de los integrantes
        time.sleep(3.5)#se espera 3.5 s

    elif a == 5:#si la respuesta es 5
        print(' > Saliendo del ejecutable...')#imprime str(x)
        break#cierra el ejecutable
    else:#si no son ninguno de la respuestas anteriores
        print(error)#imprime la variable eror
        time.sleep(2)#se espera 2 segundos 
