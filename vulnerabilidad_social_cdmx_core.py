import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt 

#NotesIndex
    #>1=Variable respuesta-registro
    #>2=Variable alcaldia-intensidad
    #>3=Variable para descrbirir alcaldia por alcaldia {INFO AREA{#Total de entradas, AREA TOTAL, AREA POR INTENSIDAD, ESTADISTICAS},
        #INFO INTENSIDAD{#TOTALENTRADAS, DESCRIPCION INTENSIDAD,ESTADISTICAS(QUIZA CREAR UN DF}
    #>9=Exportar la dataframe a un nuevo documento


#>Objetivos:
    #>Determinar cual es la alcaldia con mayor vulnerabilidad social
    #>Determinar cual es el tipo de vulnerabilidad social que más se hace presente en la CDMX
    #>Determinar cuales son las areas totales de los tipos de vulnerabilidad social y compararlas
    #>Determinar las estadisticas generales de cada una de las vulerabilidades
    #>Hacer graficas especificas d8e las alcaldias


db = pd.read_csv('datasets/db.csv')
dfo = pd.DataFrame(db)#Es el dataframe original
df = pd.DataFrame(db)#Es el dataframe con el que se trabajará y modificará
df.rename(columns={'Fenómeno':'Fenomeno','Taxonomía':'Taxonomia','Descripción':'Descripcion','Alcaldía':'Alcaldia',
                   'Área mt2':'Area','Perímetro':'Perimetro'}, inplace=True)#Se renombran las columnas para facilitar el uso de variables
dfo.rename(columns={'Fenómeno':'Fenomeno','Taxonomía':'Taxonomia','Descripción':'Descripcion','Alcaldía':'Alcaldia',
                   'Área mt2':'Area','Perímetro':'Perimetro'}, inplace=True)
df = df.drop(['Geopoint','Geoshape','ID','Fenomeno','Fuente','Cvegeo','Int2','Taxonomia','Rpve'], axis=1)#Se eliminan estas columnas porque son inecesarias
df = df.set_index(['Descripcion'])#setea a la columna descripcion como indice
df = df.drop('N/D.', axis=0)#elimina todas las columnas del indice con ('N/D'), ya que, no contaban con datos, entonces
#se decidió eliminar para trabajar con solo los datos válidos, resultando en una imagen de solo 2810/4908
#resultando en 57% datos rescatables de la databased
df = df.set_index('Alcaldia')
df = df.drop(['Benito JuÃ¡rez', 'CoyoacÃ¡n', 'CuauhtÃ©moc', 'TlÃ¡huac'], axis=0)#Se eliminan las alcaldias repetidas y
#tambien se elimina la Alcaldía Alvaro Obregon, ya que, no contaba con ningun dato de nivel de vulnerabilidad


# ____VARIABLES____
ic = ['Muy Alto','Alto','Medio','Bajo','Muy Bajo'] #define el INTENSIDAD'S CATEGORIES
t_alcaldias = ['Azcapotzalco','Benito Juárez','Coyoacán','Cuauhtémoc','Gustavo A. Madero','Iztacalco','Iztapalapa','Miguel Hidalgo',
               'Milpa Alta', 'Tláhuac','Tlalpan','Venustiano Carranza','Xochimilco']#LISTA DE TODAS LAS ALCADIAS
colors = ['red','tomato','orangered','orange','gold','yellow','lightgreen','lime','green','blue','cyan','magenta','darkmagenta']#se hace una lista para colores de la grafica

error = ('               ********** ERROR **********'+ '\n' +
         '               [   Digita correctamente   ]')
# ____FIN DE VARIABLES____

def sep(x):#define la variable para hacer una separacion y que se vea mas estetico y ordenado
    print('-------------------- ' + str(x) + ' --------------------')#imprime guines con el valor que introduzcan en sep(x)
    print('Imprimiendo ' +str(x) + ' ...') #imprime el valor introducido en sep(x)

#print(df.describe())
#print(df.dtypes)
#print(df.isnull().count())

# sep('Estadisticas de Alcaldia')
# print(df['Alcaldia'].describe())#imprime el resumen estadistico de alcaldia
# alc = df_new.groupby(['Alcaldia','Intensidad'])#agrupa la columna alcaldia
# print(alc.sum())
# print(alc.count())
# print(pd.DataFrame(alc))

#Alcaldia

# dfoalc = dfo.groupby('Alcaldía') #agrupa los valores por allcaldias
# print(dfoalc.count()) #hace un conteo de la dataframe anterior
# print(df[(df['Alcaldia']=='Tláhuac')].count())#hace una nueva dataframe con la alcadia tlahuac 

def rr(x):#definicion variable respuesta-registro
    print(' > Dentro de la base de datos se cuentan con ' + str(len(df[(df['Intensidad'] == x)].index)) +
          ' de ' + str(len(df.index)) + ' registros disponibles con Intensidad: '+ x + '\n'
          + '  >> Representa el ' + '[' + str(len(df[(df['Intensidad']== x)]) / len(df.index) * 100) + ' %] del total')
    #obtiene la longitutd de los registros con la intensidad (x) y hace una representacion porcentual de los valores


#Areas
# print(df['Area'].sum())#AREA TOTAL DE LA IMAGEN CON LOS REGISTROS LIMPIOS (2407)
# print(df['Area'].describe())
# areas = df.groupby([(df['Intensidad']=='Alto'),'Area'])
# print(areas.count()
# print(df[{(df['Intensidad']=='Alto'),'Area'}])
# print(df[{(df['Intensidad']=='Alto'),'Area'}])
# print(df[{'Area','Intensidad'}].describe())
# itensitdad = (df[(df['Intensidad']=='Alto')])
# print(df[itensitdad, 'Area'])

# print(df[[df['Intensidad']=='Alto','Area']])
# intensidad = (df[(df['Intensidad']=='Alto')])
# g1 = dfo.groupby(['Alcaldia','Intensidad'])
# print(df.loc['Coyoacán'])

#SELECCIONA EL LAS ALCALDIAS CON INTENSIDAD

def ai(x,y):#define alcaldia-intensidad
    alcal = (dfo['Alcaldia'] == str(x))  # espeficifica que busca la columna ALCALDIA para tenerlo como parametro
    intens = (dfo['Intensidad'] == str(y))  # especifica que se busca la columna intensidad para tenerlo como parametro
    r_p_ntrs = len(dfo[alcal & intens].index) #une ambos valores para obtener los resultados de ambos parametros y solo
    #obtener las entradas resultantes de las especificaciones que introduzca el usuario #OBTIENE RESULTADOS PARCIALES
    r_t_ntrs = len(df.loc[x].index)#obtiene el total de entries de intensidades para la alcaldia #OBTIENE RESULTADOS TOTALES
    #se obtiene a partir de los datos depurados de la database limpia
    print(' > La Alcaldía ' + x + ' cuenta con ' + '[' + str(r_p_ntrs) + ']' + ' entradas para intensidad = ' + '[' + y + ']')
    print('  >> Representa el ' + '[%' + str(r_p_ntrs/r_t_ntrs*100) + '] del total de datos (' + str(r_t_ntrs) + '). ')


# for alcaldias in t_alcaldias: #imprime todos los resultados por alcaldia e intensidad
#     for i in ic:
#         print(ai(alcaldias,i))

#DESCRIPCION GENERAL(INCLUYENDO TODAS LAS ENTRIES SIN ALCALDIAS ESPECIFICAS)
def db_info1():#define la variable db_info1 para la informacion de la base de datos
    print(df.shape)#imprime los parametros de la base de datos 
    print('> La base de datos ha sido limpiada y ha arrojado [' +  str(len(df.index)) + '] de [' + str(len(dfo.index)) + '] totales.')#imprime el indice de la base de datos limpia
    #y la base de datos sin limpiar
    print(' >> ¡SE HA CREADO UNA IMAGEN DEL [' + str(len(df.index)/len(dfo.index)*100) + '%] A PARTIR DE LA BASE DE DATOS ORIGINAL!')#hace una representacion porcentua del indice nuevo sobre el indice viejo

def at(): #variable para obtener las areas totales
    areas = (df['Area'])

# print(dfo('Coyoacán'))
# print(ai('Coyoacán','Alto'))
# alcal = (dfo['Alcaldia'] == 'Coyoacán')  # espeficifica que busca la columna ALCALDIA para tenerlo como parametro
# intens = (dfo['Intensidad'] == 'Bajo')  # especifica que se busca la columna intensidad para tenerlo como parametro
# r_p_ntrs = len(dfo[alcal & intens].index)  # une ambos valores para obtener los resultados de ambos parametros y solo
#     # obtener las entradas resultantes de las especificaciones que introduzca el usuario #OBTIENE RESULTADOS PARCIALES
# r_t_ntrs = len(dfo[alcal].index)  # obtiene el total de entries de intensidades para la alcaldia #OBTIENE RESULTADOS TOTALES
# print(' > La Alcaldía ' + 'Coyoacán' + ' cuenta con ' + '[' + str(r_p_ntrs) + ']' + ' entradas para intensidad = ' + '[' + 'Alto' + ']')
# print('  > Representa el ' + '[%' + str(r_p_ntrs / r_t_ntrs * 100) + '] del total de datos (' + str(r_t_ntrs) + '). ')


# print(ai(('Coyoacán'),('Bajo')))
# inte = (dfo['Intensidad']=='Bajo')
# coyo = (dfo['Alcaldia']=='Coyoacán')
# # print(len(dfo[inte & coyo].index))
# # print(len(dfo[coyo].index))
# print(len(df.loc['Coyoacán'].index))


def alc_desc_gen():#se define la variable para la descripcion general de las alcaldias#QUEDA OBSOLETA TRAS UNA ACTUALIZACION
    r = int(input(' >|Selecciona la elección de tu preferencia|'))#solicita un valor para el menu de preferencia
    callable(t_alcaldias)#llama a la variable t_alcaldias(encuentran todas las alcaldias)
    values0 = [] #setea una lista
    values1 = []#setea una lista
    values2 = []#setea una lista
    values3 = []#setea una lista

    for alcaldias in t_alcaldias:#hace un loop para obtener los resultados de alcaldias
        alcaldias_x_area_df = df['Area']#define la variable como un nuevo dataframe en donde se encuentra la columna area del dataframe limpo
        alc_ntrs = len(df.loc[alcaldias].index)#define la variable para obtener el total de alcaldias, localizando los indices 'alcaldia'
        values0 = values0 + [alc_ntrs]#agrega a la lista cada uno de los resultados del loop (total de entradas)
        values1 = values1 + [alcaldias]#agrega a la lista cada uno de los resultados del loop
        values2 = values2 + [alc_ntrs/len(df.index)*100]#agrega a la lista una valoracion porcentual
        values3 = values3
        # values3 = values3 + [alc_ntrs

    alc_desc_gen_df = pd.DataFrame(list(zip(values1,values0,values2)),#crea un nuevo dataframe con los resultados de las listas anteriores
                       columns=['Alcaldía','Número de entradas','% del total'])#setea nombre a las columnas

    # edf = pd.DataFrame({'Alcaldía':[values1],'Número de entradas':[values0]},columns=['Alcaldía','Número de entradas'])
    if r == 1:#si se escribe el valor 1 entonces
        print('1',alc_desc_gen_df)#imprime 1 y la nueva dataframe
    if r ==2:
        print('PRUEBA 2')#prueba
    if r==3:
        print('PRUEBA3')#prueba
# data = [values1],[values0]
# print(djdf)
# print(g1.count())
# g = dfo.groupby([intensidad,'Alcaldia']).count(
# print(df.loc[['Tláhuac'],['Intensidad']].info())
# print(df.loc[['Coyoacán'], [(df['Intensidad']=='Alto')]])
# print(df.loc[coyoacan & (df['Intensidad']=='Alto')].info())
# df.to_csv('Prueba1.csv')

# print(df[(df.loc['Area'],df.loc['Coyoacán'])].sum)

# print(df[[df.loc['Coyoacán'], ['Area']]].sum())

def descripcion_variable(x,y):#define la variable descripcion_Variable para describir la variable de un dataframe, teniendo como x= el dataframe; y= el nombre de la columna o variable del df
    variable = str(y) #define a la variable 'variable' como el string del nombre de la variable a describir
    print('               ---------- [DESCRIPCIÓN VARIABLE |' + variable + '| ] ----------')#imprime descripcion variable y la variable a describir
    time.sleep(2)#se toma 2 segundos para ejecutar el siguiente comando
    df_descrp = x[y]#se define un nuevo dataframe como x=nombre del df; y=columna/variable
    print(df_descrp.describe())#imprime la descripcion del nuevo dataframe
    print('\n' + '>>>')#imprime un espacio y >>>
    time.sleep(2)#espera 2 segundos antes de ejecutar el siguiente comando
    
    print(' > La variable |' + variable + '| cuenta con [ ' + str(len(df_descrp.index)) + ' ] entradas totales.')#imprime las entradas totales de la variable
    time.sleep(1)#se espera 1 segundo
    print(' > El valor mínimo de la variable |' + variable + '| es de: [ ' +str(df_descrp.min()) + ' ]')#imprime el valor minimo de la variable
    time.sleep(1)#se espera 1 segundo
    print(' > El valor máximo de la variable |' + variable + '| es de: [ ' + str(df_descrp.max()) + ' ]')#imprime el valor maximo de la variable
    time.sleep(1)#se espera 1 segundo
    print(' > El promedio de la variable |' + variable + '| es de: [ ' + str(df_descrp.mean()) + ' ]')#imprime el promedio de la variable
    time.sleep(1)#se espera 1 segundo
    print(' > El promedio de la variable |' + variable + '| es de: [ ' + str(df_descrp.median()) + ' ]')#imprime la mediana de la variable
    time.sleep(1)#se espera 1 segundo
    print(' > La variación estandar para la variable |' + variable + '| es de: [ ' + str(df_descrp.std()) + ' ]')#imprime la variacion estandar de la variable
    time.sleep(1)#se espera 1 segundo

    
def imprimir_barh(x,y,z):#define la variable para imprimir graficas 
    callable(colors)#llama las variable colors
    callable(t_alcaldias)#define una lista de las alcaldias con valor numerico
    t_alcaldias1 = tuple(t_alcaldias)
    plt.bar(t_alcaldias1,x[y], width=0.5, edgecolor = 'black', color=z)#define los parametros de la grafica
    plt.xticks(fontsize=5, rotation=45)
    plt.ylabel('Número de entradas')#ponle la etiqueta en y
    plt.xlabel('Alcaldías')#ponle la etiqueta en x 
    plt.title('Gráfica de barras por número de entradas de :' +'\n' +
              '[ ' + str(y) + ' ]')#define el titulo de la grafica 
    a = int(input(' >|¿Quieres exportar como imágen la gráfica? [si = 1] [no = 0]; Digita el número de tu preferencia|'))#solicita un valor para exportar la grafica
    if a ==1:#si el valor es 1
        print(' > Imprimiendo gráfica...')#imprime strng
        print(' > Exportando gráfica...')#imprime strng
        time.sleep(2)#se espera 2 segundos
        plt.savefig('Vulnerabilidad_social_x_alcaldias_descrp_general_' + y + '.png')#exporta la grafica a png
        print(' > ¡Vulnerabilidad_social_x_alcaldias_descrp_general_' + y + '.png ha sido exportada con éxito!')#imprime que se exporto la grafica
        plt.show()#enseña la grafica 
        time.sleep(2)#se espera 2 segundps
    elif a ==0:#si el valor es 0
        print(' > Imprimiendo gráfica...')#imprime str
        time.sleep(1.5)#se espera 1.5 s
        plt.show()#imprime la grafica 
        time.sleep(2)#se espera 2 segundos
    
    else:
        print(error)#imprime la variable error
## ESTADISTICAS GENERALES DE LA CIUDAD
def cdmx_desc_gen():#se define la variable para la descripción general de la ciudad de mexico y vulnerabilidad social
    callable(ic)#llama a la variable ic
    values0 = []#crea lista
    values1 = []#crea lista
    values2 = []#crea lista
    values3 = []#crea lista
    values4 = []#crea lista

    o1 = '   ||1|| Mostrar por orden de tipos de intensidades' #define o1 como opcion 1
    o2 = '   ||2|| Mostrar por entradas totales'#define o2 como el str de opcion2
    o3 = '   ||3|| Mostrar por área'#define o3 como el str de opcion3 del menu
    print(o1 + '\n'+#imprime o1, o2, o3
          o2 + '\n'+
          o3 + '\n')


    a = int(input(' >|Selecciona la elección de tu preferencia|'))#solicita un digito para el menu
    for i in ic:
        intensidadxarea_df = df[df['Intensidad']== i]#VARIABLE QUE DETERMINA UN DF SOLO PARA INTENSIDAD = CADA UNA DE LAS INTENSIDADES
        suma_ixa_df = intensidadxarea_df['Area'].sum()#VARIABLE DE LA SUMA DE LA COLUMNA DE AREA
        t_ic_ntrs = len(df[(df['Intensidad']== i)].index)#OBTIENE EL NUMERO TOTAL DE ENTRADAS DE CADA INTENSIDAD
        t_areas_ntrs = df['Area'].sum()#obtiene una suma del total de areas 
        values0 = values0 + [i]#AGREGA CADA UNA DE LAS INTENSIDADES A LA LISTA DE VALUES0
        values1 = values1 + [t_ic_ntrs]#AGREGA LAS ENTRADAS TOTALES DE CADA UNA DE LAS INTENSIDADES A LA LISTA VALUES1
        values2 = values2 + [t_ic_ntrs/len(df.index)*100]#AGREGA EL PORCENTAJE DE LAS ENTRADAS PARCIALES DE CADA INTENSIDAD A LA LISTA VALUES2
        values3 = values3 + [suma_ixa_df]#AGREGA LA SUMA DE TODOS LOS VALORES PARA CADA UNA DE LAS INTENSIDADES A LA LISTA VALUES3
        values4 = values4 + [suma_ixa_df/t_areas_ntrs*100]#hace una evaluacion porcentual de la suma de las areas de una alcaldia sobre la area total
        e2df = pd.DataFrame(list(zip(values0,values1,values2,values3,values4)),#crea un nuevo dataframe con los valores anteriores
                                columns=['Intensidad','Número de entradas','% de entradas totales','Área (m²)','% del Área total'])
            #     sep(o1)
            #     print(e2df)#IMPRIME EL DATA FRAME POR intensidades
            # elif a == 2:
            #     sep(o2)
            # elif a == 3:
    if a == 1:#si a es 1
        callable(sep(o1))#llama a separacion
        print(e2df)#imprime el df
        a = int(input(' >|¿Deseas exportar el dataframe? [si= 1] [no = 0]; Digita el número de tu preferencia|'))
        #solicita un valor para exportar el dataframe o no
        if a == 1:#si el valor es 1 
            print(' > Exportando gráfica con el nombre: "Vulnerabilidad_Social_por_orden_de_tipos_de_intensidades')#imprime el str
            new.to_csv('Vulnerabilidad_Social_por_orden_de_tipos_de_intensidades.csv')#exporta el df a un csv
            time.sleep(2)#se espera dos segundos
        else:
            print('Continuando ...')#imprime el str
            time.sleep(2)#se espera 2 segundos
        time.sleep(3)#se espera 3 segundos 
    elif a ==2:#si es 2
        callable(sep(o2))#llama separacion de la opcion1
        new = (e2df.sort_values(by = '% de entradas totales', ascending=False))#define EL DATA FRAME POR EL NUMERO DE ENTRADAS [MAYOR A MENOR]
        print(new)#imprime le dataframe
        time.sleep(2)#se espera 2 segundos
        descripcion_variable(new, '% de entradas totales')#llama a la variable descripcion_variable
        print('               ---------- [DATAFRAME] ----------               ')#imprime el str
        a = int(input(' >|¿Deseas exportar el dataframe? [si= 1] [no = 0]; Digita el número de tu preferencia|'))#pide un digito para exporta el df
        if a == 1:#si el digito es 1 
            print(' > Exportando dataframe con el nombre: "Vulnerabilidad_Social_por_entradas_totales_en_la_CDMX.csv')#imprime el str
            new.to_csv('Vulnerabilidad_Social_por_entradas_totales_en_la_CDMX.csv')#exporta el nuevo df por entradas sociales
            time.sleep(2)#se espera dos segundos
        else:
            print('Continuando ...')#imprime el str
            time.sleep(2)#se espera dos segundos
            
        print('               ---------- [GRÁFICA] ----------               ')#imprime el str    
        a = int(input(' >|¿Deseas imprimir la gráfica? [si = 1] [no = 0]; Digita el número de tu preferencia|'))#pide un digito para imprimir la grafica
        if a == 1:
            values = [new['Intensidad']]#define a values como la columna 'Intensidad' del dataframe en uso
            fig1, ax1 = plt.subplots()#define los parametros para la grafica de pastel
            ax1.pie(values2, labels=ic, autopct= '%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')#define el axis de x como igual
            plt.title('[Vulnerabilidad Social por entradas totales en la CDMX]')#define el titulo del grafico
            a = int(input(' >|¿Quieres exportar como imágen la gráfica? [si = 1] [no = 0]; Digita el número de tu preferencia|'))#pide un digito para exportar el grafico 
            if a == 1:#si el digito es 1 
                print(' > Exportando gráfica...' + '\n' +
                      ' > Imprimiendo gráfica...')#imprime el str
                time.sleep(2)#se espera dos segundos
                plt.savefig('Vulnerabilidad_Social_por_entradas_totales_en_la_CDMX.png')#exporta la grafica a png
                print('¡Vulnerabilidad_Social_por_entradas_totales_en_la_CDMX.png se ha exportado con exito!')#imprime str
                plt.show()#enseña el grafico 
                
            elif a == 0:#si el digito es 0
                print(' > Imprimiendo gráfica...')#imprime el str
                time.sleep(2)#se espera dos segundos 
                plt.show()#imprime el grafico
            else:#si no es ninguno de los valores 
                print(error)#imprime error 
            time.sleep(3)
                #se espera 3 segundos
        elif a == 0:
            print('Regresando al menú principal...')#imprime el str
        else:
            print(error)#imprime la variable error

            time.sleep(3)#se espera 3 segundos
    elif a==3:#si la respuesta es 3 
        callable(sep(o3))#llama la variable separacion para la opcion3
        new = (e2df.sort_values(by = 'Área (m²)', ascending=False))#define EL DATA FRAME POR EL AREA [MAYOR A MENOR]
        print(new)#imprime el datafraME
        time.sleep(2)#SE ESPERA 2 segundos
        descripcion_variable(new, 'Área (m²)')#llama a la variable descripcion_variable para el df 'new' y la columna 'area'
        
        print('               ---------- [DATAFRAME] ----------               ')#imprime el str
        a = int(input(' >|¿Deseas exportar el dataframe? [si= 1] [no = 0]; Digita el número de tu preferencia|'))#pide un digito para exportar el df
        
        if a == 1:#si la respuesta 
            print(' > Exportando datataframe con el nombre: "Vulnerabilidad_Social_por_área_en_la_CDMX.csv')#imprime str 
            new.to_csv('Vulnerabilidad_Social_por_área_en_la_CDMX.csv')#exporta el dataframe
            time.sleep(2)#se espera 2 segundos
        else:
            print('Continuando ...')#Imprime el str
            time.sleep(2)#se espera 2 segundos
        
        print('               ---------- [GRÁFICA] ----------               ')#imprime el str
        a = int(input(' >|¿Deseas imprimir la gráfica? [si = 1] [no = 0]; Digita el número de tu preferencia|'))#pide un valor para el imprimir la grafica
        if a == 1:#si el digito es 1
            values = [new['Intensidad']]#define values como el df new['Intensidad]
            fig1, ax1 = plt.subplots()#define los parametros para la grafica de pastel
            ax1.pie(values3, labels=ic, autopct= '%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')#define el axis de x a igual
            plt.title('[Vulnerabilidad Social por área en la CDMX]')#define el titulo del grafico
            a = int(input(' >|¿Quieres exportar como imágen la gráfica? [si = 1] [no = 0]; Digita el número de tu preferencia|'))#pide un digito
            if a == 1:#si el resultado es 1 
                plt.savefig('Vulnerabilidad_Social_por_área_en_la_CDMX.png')#exporta el grafico
                print(' > Exportando gráfica...' + '\n' +
                      ' > Imprimiendo gráfica...')#imrpime el str
                time.sleep(2)#se espera 2 segundos 
                print('¡Vulnerabilidad_Social_por_área_en_la_CDMX.png se ha exportado con exito!')#imprime el str
                plt.show()#imprime la grafica 
                time.sleep(2)#se espera 2 segundos 
                
            elif a == 0:#si el resultado es 0
                print(' > Imprimiendo gráfica...')#imprime el str
                time.sleep(2)#se espera dos segundos
                plt.show()#imprime el grafico 
            else:
                print(error)#imprime el erro 
                time.sleep(2)#se espera 2 segundos
                
        elif a == 0:#si la respuesta es 0
            print('Regresando al menú principal...')#imprime el str
        else:#si la respuesta es otra 
            print(error)#imprime error
        time.sleep(3)#se espera 3 segundos 







def total_alcaldias_descr_intensidad():#define la variable para describir el total de alcaldias

# if a == 1:
    callable(t_alcaldias)#llama la variable t_alcaldias
    callable(ic)#llava la variable ic 
    values0 = []#crea lista
    values1 = []#crea lista
    values2 = []#crea lista
    values3 = []#crea lista 
    values4 = []#crea lista
    values5 = []#crea lista
    t_values_ntrs = []#crea lista

    o1 = (' ||1|| Vulnerabilidad social por orden alfabético')#define el str de la opcion 1
    o2 = (' ||2|| Vulnerabilidad social por orden de cantidad de entradas')#define el str de la opcion 2
    o3 = (' ||3|| Vulnerabilidad social por orden de Intensidad [Muy Alto]')#define el str de la opcion3
    o4 = (' ||4|| Vulnerabilidad social por orden de Intensidad [Alto]')#define el str de la opcion 4 
    o5 = (' ||5|| Vulnerabilidad social por orden de Intensidad [Medio]')#define el str de la opcion5
    o6 = (' ||6|| Vulnerabilidad social por orden de Intensidad [Bajo]')#define el str de la opcion6
    o7 = (' ||7|| Vulnerabilidad social por orden de Intensidad [Muy Bajo]')#define sltr de la opcion7

    print(o1 + '\n'+#imprime todas las opciones
          o2 + '\n'+
          o3 + '\n'+
          o4 + '\n'+
          o5 + '\n'+
          o6 + '\n'+
          o7 + '\n')

    a = int(input(' >|Selecciona la elección de tu preferencia|'))#pide un digito 
    for alcaldias in t_alcaldias:#hace un loop de alcaldias

        dfa = df.loc[alcaldias]# define una nueva dataframe 
        t_alc_ntrs_malto = dfa[dfa['Intensidad']=='Muy Alto']#define la variable como un df con intensidad = muy alto
        t_alc_ntrs_alto = dfa[dfa['Intensidad']=='Alto']#define la variable dfa con intensidad = alto
        t_alc_ntrs_medio = dfa[dfa['Intensidad']=='Medio']#define la variable dfa con intensidad = medio
        t_alc_ntrs_bajo = dfa[dfa['Intensidad']=='Bajo']#define la variable dfa con intensidasd = bajo
        t_alc_ntrs_mbajo = dfa[dfa['Intensidad']=='Muy Bajo']#define la variable como un df con intensidad = muy bajo
        values0 = values0 + [alcaldias]#agrega las alcaldias a la lista
        values1 = values1 + [len(t_alc_ntrs_malto.index)]#agrega la longitud de la columna muy alto
        values2 = values2 + [len(t_alc_ntrs_alto.index)]#agrega la longitud a la lista de la columna alto
        values3 = values3 + [len(t_alc_ntrs_medio.index)]#agrega la longitud a la lista de la columna medio
        values4 = values4 + [len(t_alc_ntrs_bajo.index)]#agrega la longitud a la lista de la columna bajo
        values5 = values5 + [len(t_alc_ntrs_mbajo.index)]#agrega la longitud a la lista de la columna muy bajo
        t_values_ntrs = t_values_ntrs + [len(dfa.index)]#agrega a la lista la longitud del indice de los valores totales

    edf = pd.DataFrame(list(zip(t_alcaldias,values1,values2,values3,values4,values5,t_values_ntrs)),
                       columns=['Alcaldía','Muy Alto','Alto','Medio','Bajo','Muy Bajo','Total entradas'])#define los parametros para crea un nuevo df
    
    

    if a ==1:#si la respuesta es 1
        callable(sep(o1))#llama separacion op1
        print(edf)#imprime el df
        time.sleep(3)#se espera 3 segundos
    elif a==2:#si la respuesta es 2
        edf1 = edf[['Alcaldía','Total entradas']]#define al nuevo df
        callable(sep(o2))#llama separacion o2
        print(edf1.sort_values(by='Total entradas', ascending=False))#imprime el df de mayor a menor
        descripcion_variable(edf1, 'Total entradas')#ejecuta la variable descripcion_variable 
        print('               ---------- [GRÁFICAS] ----------               ')#imprime l str
        imprimir_barh(edf,'Total entradas','magenta')#imprime las grafica 
        time.sleep(1.5)#se espera 1.5 s
    elif a==3:#si la respuesta es 3
        edf1 = edf[['Alcaldía','Muy Alto']]#se define un nuevo df 
        callable(sep(o3))#llama a la variable sep para la opcion3
        print(edf1.sort_values(by='Muy Alto', ascending=False))#imprime el df por la variable 'muy alto' de mayor a menor 
        descripcion_variable(edf1, 'Muy Alto')#ejecuta la variable descripcion_variable
        print('               ---------- [GRÁFICAS] ----------               ')#imprime el str
        imprimir_barh(edf, 'Muy Alto','red')#imprime la variable de grafica 
        time.sleep(1.5)#se espera 1.5 s
    elif a==4:#si la respuesta es 4
        edf1 = edf[['Alcaldía','Alto']]#define un nueo df 
        callable(sep(o4))#llama la variable sep para la opcion4
        print(edf1.sort_values(by='Alto', ascending=False))#ordena de mayor a menor el df para la columna alto
        descripcion_variable(edf1, 'Alto')#ejecuta la variable descrpcion_variable
        print('               ---------- [GRÁFICAS] ----------               ')#imprime str
        imprimir_barh(edf, 'Alto','orangered')#ejecuta la variable de grafica 
        time.sleep(1.5)#se espera 1.5 s 
    elif a==5:#si la respuesta es 5
        edf1 = edf[['Alcaldía','Medio']]#define un nuevo df
        callable(sep(o5))#llama a separcion de la opcion5
        print(edf1.sort_values(by='Medio', ascending=False))#imprime el nuevo df por orden descendente de la columna medio
        descripcion_variable(edf1, 'Medio')#ejecuta la variable descrpcion_Variable
        print('               ---------- [GRÁFICAS] ----------               ')#imprime el str
        imprimir_barh(edf, 'Medio','gold')#ejecuta la variable para imprimir graficas 
        time.sleep(1.5)#se espera 1.5 s
    elif a==6:#si la respuesta es 6
        edf1 = edf[['Alcaldía','Bajo']]#define un nuevo d f
        callable(sep(o6))#llama a separacion la opcioon6
        print(edf1.sort_values(by='Bajo', ascending=False))#imprime el nuevo df por orden descendente de la columna bajo
        descripcion_variable(edf1, 'Bajo')#ejecuta la variable descripcion_variable
        print('               ---------- [GRÁFICAS] ----------               ')#imprime el str
        imprimir_barh(edf, 'Bajo','lightgreen')#ejecuta la variable para imprimir graficas 
        time.sleep(1.5)#se espera 1.5 s 
    elif a==7:#si la respuesta es 7
        edf1 = edf[['Alcaldía','Muy Bajo']]#define un nuevo df 
        callable(sep(o7))#llama la separacion de la opcion7
        print(edf1.sort_values(by='Muy Bajo', ascending=False))#se ordena el df por orden descendente de la columna muy bajo
        descripcion_variable(edf1, 'Muy Bajo')#eecuta la variable descripcion_variable
        print('               ---------- [GRÁFICAS] ----------               ')#imprime el str
        imprimir_barh(edf, 'Muy Bajo','green')#ejecuta la variable para imprimir graficas 
        time.sleep(1.5)#se espera 1.5 s
    else:
        print(error)#imprime error


def menu():#define el menu
    o1 = str(' ||1|| Información de la Vulnerabilidad Social en términos generales [Ciudad Completa]')#define la opcion1
    o2 = str(' ||2|| Información de la Vunerabilidad Social en términos de específicos [Alcaldías]')#define la opcion2
    o3 = str(' ||3|| Información de la base de datos para este proyecto')#defione la opcion3
    o4 = str(' ||4|| Créditos')#define la opcion4
    o5 = str(' ||5|| Salir')#define la opcion5
    print(o1 + '\n' + o2  + '\n' + o3 + '\n' + o4 + '\n' + o5)#imprime todas las opciones
    print('\n')






##DESCRIPCIÓN ALCALD
# intens = df[df['Intensidad']=='Alto']
# coy = df.loc['Coyoacán']
# print(len(coy[(coy['Intensidad']=='Alto')]))

# print(len(df[(df['Intensidad']=='Alto')].index))

# is_intensidad_alta = df['Intensidad']=='Alto'
# area = df['Area']
# ex = dfo[dfo['Alcaldia'] =='Coyoacán']
# ex2 = df[df['Intensidad']=='Alto']
#
# df['Area'] = df['Area'].astype(np.float64)
# print(ex2['Area'].sum())

# df.to_csv('Test1.csv')
def descrp_alc(x):#define la variable descrp_alc

    values0 = []#crea lista
    values1 = []#crea lista
    values2 =[]#crea lista
    values3 = []#crea lista
    values4 = []#crea lista
    values5 = []#crea lista
    t_values_ntrs = []#crea lista
    alcaldia = [x]#define a x como valor inicial de la lista 
    areatotal = (df['Area'].sum())#define la variable como la suma del area

    dfa = df.loc[x]#crea un nuevo dataframe al localizar la variable x
    t_alc_ntrs_malto = dfa[dfa['Intensidad'] == 'Muy Alto']#define el total de entradas para intensidad == muy alto
    t_alc_ntrs_alto = dfa[dfa['Intensidad'] == 'Alto']#define el total de entradas para intensidad == alto
    t_alc_ntrs_medio = dfa[dfa['Intensidad'] == 'Medio']#define el total de entradas para intensidad == medio
    t_alc_ntrs_bajo = dfa[dfa['Intensidad'] == 'Bajo']#define el total de entradas para intensidad == bajo
    t_alc_ntrs_mbajo = dfa[dfa['Intensidad'] == 'Muy Bajo']#define el total de entradas para intensidad == muy bajo
    values0 = values0 + [x]#agrega x a la lista 
    values1 = values1 + [len(t_alc_ntrs_malto.index)]#agrega el total de entradas para intensidad malto a la lista
    values2 = values2 + [len(t_alc_ntrs_alto.index)]#agrega el total de entradas para intensidad alto a la list
    values3 = values3 + [len(t_alc_ntrs_medio.index)]#agrega el total de entradas para intensidad medio a la lista
    values4 = values4 + [len(t_alc_ntrs_bajo.index)]#agrega el total de entradas para inteisdad bajo a la lista
    values5 = values5 + [len(t_alc_ntrs_mbajo.index)]#agrega el total de entradas para la intensidad mbajo a la lista
    t_values_ntrs = t_values_ntrs + [len(dfa.index)]#agrega el total de entradas a la lista
    total_values = [values1, values2, values3, values4, values5]#crea una lista de listas
    edf = pd.DataFrame(list(zip(alcaldia, values1, values2, values3, values4, values5, t_values_ntrs)),#define los parametros para la creaciond e un nuevo df 
                   columns=['Alcaldia', 'Muy Alto', 'Alto', 'Medio', 'Bajo', 'Muy Bajo', 'Total entradas'])
    t_values = (len(t_alc_ntrs_malto.index),len(t_alc_ntrs_alto.index),len(t_alc_ntrs_medio.index),len(t_alc_ntrs_bajo.index),len(t_alc_ntrs_mbajo.index))#define un tuple con los valores
    t = tuple(total_values)#pasa de lista a tuple
    print(edf)#imprime el dataframe
    print('\n')#imprime un espacio
    time.sleep(1.5)#se espera 1.5s
    print(' > La alcaldía ' + str(x) + ' cuenta con un total de entradas de  [' + str(len(dfa.index)) + ' ]' + '\n'
          '   correspondiente al [ ' + str((len(dfa.index))/(len(df.index))*100) + ' % ] del total de entradas ( ' + str(len(df.index)) + ' )')#total de entradas y representacion porcentual
    time.sleep(1.5)#se espera 1.5 s 
    print(' > El total de entradas para la alcaldía ' + str(x) + ' suman un área de [ '+ str((dfa['Area']).sum()) + ' ] metros cuadrados'+'\n'+
          '   correspondiente al [ '+ str((dfa['Area'].sum())/areatotal*100) + ' % ] del área total de todas las alcaldías ( ' +
          str(df['Area'].sum()) + ' ) metros cuadrados.')#total de area y representacion porcentual
    time.sleep(1.5)#se espera 1.5 s
    print(' > El total de entradas para la alcaldía ' + str(x) + ' suman un perímetro de [ ' + str((dfa['Perimetro'].sum())) + ' ] metros' + '\n'+
          '   correspondiente al [ ' + str((dfa['Perimetro'].sum())/(df['Perimetro'].sum())*100) + ' % ] del perímetro total de todas las alcaldías ( '+
          str(df['Perimetro'].sum()) + ' ) metros.')#total de entradas y representacion porcentuañ
    time.sleep(1.5)#se espera 1.5 s
    print('               ---------- [INTENSIDADES] ----------               ')#imprime el str
    time.sleep(2)#se espera 2 s
    callable(ic)#llama a la variable ic

    print(' > El total de entradas para la alcaldía [ ' + str(x) + ' ] con Intensidad == [Muy Alto] son ' +  str(values1) + '\n' +
          '   correspondiente al [ ' + str(len(t_alc_ntrs_malto.index)/(len(dfa.index))*100) + ' % ] del total de entradas ( ' + str(len(dfa.index)) + ' )')
    #imprime el total de entradas con intensidad muy alto y representacion porcentual
    print(' > El total de entradas para la alcaldía [ ' + str(x) + ' ] con Intensidad == [Alto] son ' + str(
        values2) + '\n' +
          '   correspondiente al [ ' + str(
        len(t_alc_ntrs_alto.index) / (len(dfa.index)) * 100) + ' % ] del total de entradas ( ' + str(
        len(dfa.index)) + ' )')
    #imprime el total de entradas con intensidad alto y representacion porcentual
    print(' > El total de entradas para la alcaldía [ ' + str(x) + ' ] con Intensidad == [Medio] son ' + str(
        values3) + '\n' +
          '   correspondiente al [ ' + str(
        len(t_alc_ntrs_medio.index) / (len(dfa.index)) * 100) + ' % ] del total de entradas ( ' + str(
        len(dfa.index)) + ' )')
    #imprime el total de entradas con intensidad medio y representacion porcentual 
    print(' > El total de entradas para la alcaldía [ ' + str(x) + ' ] con Intensidad == [Bajo] son ' + str(
        values4) + '\n' +
          '   correspondiente al [ ' + str(
        len(t_alc_ntrs_bajo.index) / (len(dfa.index)) * 100) + ' % ] del total de entradas ( ' + str(
        len(dfa.index)) + ' )')
    #imprime el total de entradas con intensidad bajo y representacion porcentual
    print(' > El total de entradas para la alcaldía [ ' + str(x) + ' ] con Intensidad == [Muy Bajo] son ' + str(
        values5) + '\n' +
          '   correspondiente al [ ' + str(
        len(t_alc_ntrs_mbajo.index) / (len(dfa.index)) * 100) + ' % ] del total de entradas ( ' + str(
        len(dfa.index)) + ' )')
    #imprime el total de entradas con intensidad muy bajo y representacion porcentual
    print('               ---------- [GRÁFICAS] ----------')#imprime el str
    time.sleep(2)#se espera 2 s 
    
    callable(ic)#llama la variable ic 
    plt.plot(ic, total_values, label='Entradas', linewidth=2, alpha=0.5, color='red')#define los parametros para grafica lineal
    plt.title('[' +  str(x) + ']')#define el titulo
    plt.xlabel('Intensidades de la Alcaldía [' + str(x) + ']')#define la descripcion del eje x
    plt.ylabel('Número de entradas')#define la descripcion del eje y
    plt.legend()#ejecuta la leyenda
    print(' > ||1|| Gráfica lineal de Intensidades por número de entradas')#imprime el str
    
    
    a = int(input(' >|¿Quieres exportar como imágen la gráfica? [si = 1] [no = 0]; Digita el número de tu preferencia|'))#pide un digito
    if a ==1:#si la respuesta 1
        print(' > Imprimiendo gráfica...' + '\n'+
              ' > Exportando gráfica....')#imprime str
        time.sleep(2)#se espera 2 s
        print(' > ¡Gráfica_lineal_descripción_' + str(x) + '.png ha sido exportada con exito!')#imprime str
        plt.savefig('Gráfica_lineal_descripción_' + str(x) + '.png')#exporta el grafico a ´ng
        plt.show()#imprime la grafica
        time.sleep(2)#se espera 2 s
    elif a == 0:#si la respuesta es 0
        print(' > Imprimiendo gráfica...')#imprime str
        plt.show()#imprime la grafica 
        time.sleep(2)#se espera 2 s
    else:#si la respuesta no es ninguna
        print(error)#imprime error
        time.sleep(2)#se espera 2 s
    
    print('\n' +
          '  > ||2|| Gráfica de pastel de Intensidades por porcentaje')#imprime  el str
    a = int(input(' >|¿Quieres exportar como imágen la gráfica? [si = 1] [no = 0]; Digita el número de tu preferencia|'))#pide un digito
    if a ==1:#si la respuesta es 1
        fig1, ax1 = plt.subplots()
        ax1.pie(t, labels=ic, autopct= '%1.1f%%',
                    shadow=True, startangle=90)#define la grafica de pastel
        ax1.axis('equal')#define el axis como igual
        plt.title('[' + str(x) + ']')#define el titulo
        print(' > Imprimiendo gráfica...' + '\n'+
              ' > Exportando gráfica....')#define le str
        time.sleep(2)#se espera 2 segundos
        print(' > ¡Gráfica_pastel_descripción_' + str(x) + '.png ha sido exportada con exito!')#imprime str
        plt.savefig('Gráfica_pastel_descripción_' + str(x) + '.png')#exporta el grafico como png
        plt.show()#imprime la grafica 
        time.sleep(2)#se espera 2 s
    elif a ==0:#si la respuesta e 0
        fig1, ax1 = plt.subplots()
        total = np.arange(len(total_values))
        ax1.pie(t, labels=ic, autopct= '%1.1f%%',
                    shadow=True, startangle=90)#define los parametros para la grafica de pastel
        ax1.axis('equal')#define axis de x como igual
        plt.title('[' + str(x) + ']')#define el titulo
        print(' > Imprimiendo gráfica...')#imprime str
        time.sleep(2)#se espera 2 s
        plt.show()#imprime la grafica 
    else:
        print(error)#imprime la variable error
        
        

#Descripción para alcaldias
def descrp_x_alc():
    callable(t_alcaldias)#llama la variable alcaldias
    callable(ic)#llama la variable ic 
    numeros = -1#define a numeros como -1
    for alcaldias in t_alcaldias:#hace un loop con t_alcalias
        numeros = numeros + 1#suma 1 numero cada vex que se hace el loop
        print(' ||'+str(numeros) +'|| '+ alcaldias)#imprime las opciones

    a = str(input(' >|Escribe el nombre de la Alcaldía de la que quieras informarte|'))#pide un digito
    callable(sep(a))#llama a separacion para a
    descrp_alc(a)#llama descripcion de variable a
    time.sleep(3)#se espera 3 segundos


def db_info():#define la variable para la informacion de la db
    print(' > Identificador de conjunto de datos: atlas-de-riesgo-indice-de-vulnerabilidad-social')
    print(' > Descargas:    [740]' + '\n'+
          ' > Temas:    Desarrollo Urbano, vivienda y territorio, Medio ambiente y cambio climático' + '\n' +
          ' > Palabras clave:     atlas de riesgo, protección civil, resiliencia' +'\n' +
          ' > Licencia: CC BY' + '\n'+
          ' > Idioma:     Español' + '\n' +
          ' > Modificado: 9 enero de 2019 20:21' + '\n'+
          ' > Publicador:    Secretaría de Gestión Integral de Riesgos y Protección Civil' + '\n' +
          ' > Ultimo procesamiento: 7 de mayo de 2019 4:54 (metadatos)' + '\n' +
          '                         10 de enero de 2019 20:34 (datos)' + '\n' +
          ' > URL:    https://datos.cdmx.gob.mx/explore/dataset/atlas-de-riesgo-indice-de-vulnerabilidad-social/information/')#imprime informacion de la base de datos original
    time.sleep(2)#se espera 2 segundos
    print('>>>' + '\n'+
          '   La base de datos original cuenta con ' + str(dfo.shape) + ' registros y columnas totales' + '\n' +
          '   Se realizó una limpieza y de ' + str(dfo.shape) + ' registros, pasaron a ser ' + str(df.shape) + '\n'+
          '   Se eliminaron la mitad de los registros debido a que estos eran duplicados de alcaldías, del mismo modo,' + '\n'+
          '   se eliminó la alcadía Álvaro Obregón debido a que no se contaban registros válidos, resultando en 13 alcaldías de las 14 iniciales' + '\n' +
          '   Del mismo modo, se reducieron el número de columnas de 15 columnas de la base de datos original a solo un índice [Alcaldía] y 4 columnas [Intensidad, Entidad, Area, Perimetro]')
    time.sleep(2)#se espera 2 segundos
    print('>>>' + '\n')#imprime un espacio
    callable(db_info1)#llama a la variable db_info1
    db_info1()#se ejecuta la variable db_info1
    time.sleep(2)#se espera 2 segundos
    print('               ---------- [DATAFRAME] ----------')#imprime el str
    a = int(input(' >|¿Deseas exportar el dataframe? [si= 1] [no = 0]; Digita el número de tu preferencia|'))#PIDE UN DIGITO
     
    if a == 1:#si la respuesta es 1
         time.sleep(2)#se espera 2 segundois 
         print(' > Exportando DATAFRAME NUEVO...')
         df.to_csv('Atlas_de_riesgo_vulnerabilidad_social_bd_evidencia_limpia.csv')#exporta el df
         time.sleep(2)#se espera 2 seg
         print(' > ¡Atlas_de_riesgo_vulnerabilidad_social_bd_evidencia_limpia.csv ha sido exportada con exito!')#imprime str
    elif a==0:#si la respuesta es 0
        print(' > Continuando...')#Imprime str
        time.sleep(2)#se espera 2 s
    else:#si la respuesta es diferente a lo anterior
        print(error)#imprime la variable error 
        
    
# descrp_x_alc()
# descrp_x_alc()
