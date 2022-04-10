import os
os.system("clear")

#####################################################################################
# Opcion 1. Cálculo de la nota final para pasar una asignatura
#####################################################################################

def opcion1():
    materias = int(input("Cuantas materias va a ingresar: "))
    promedio = 0
    porcentaje_acum = 0
    i = 1
    # Pide las notas mientras que el acumulado de % no llegue a 100%, el exámen final 
    # valdrá 100% - porcentaje acumulado
    while i <= materias:        
        # Pide y valida la nota
        nota = -1
        while nota < 0 or nota > 5.0:
            nota = float(input(f"Nota {i}: "))
            if (nota < 0 or nota > 5.0):
                print("La nota debe estar entre 0.0 y 5.0")
        
        # Pide y valida el porcentaje
        porcentaje = -1
        while porcentaje < 0 or porcentaje >= 100:
            porcentaje = float(input(f"Porcentaje {i}: "))
            if porcentaje < 0 or porcentaje >= 100:
                print("El porcentaje debe ser mayor que 0% y menor a 100%") 

        # Suma el porcentaje si no pasa de 100%, si pasa muestra un mensaje y sigue pidiendo notas
        if ((porcentaje_acum + porcentaje) < 100):
            porcentaje_acum += porcentaje
            promedio += nota * porcentaje / 100
            i += 1
            print(f"------------------------------")
            print(f"% acumulado: {porcentaje_acum} %")
            print(f"------------------------------")
        else:
            print("El porcentaje acumulado no puede ser mayor que 100%")
        

    porcentaje_examen = 100 - porcentaje_acum
    print("------------------------------------------------------------")
    print(f"Acumulado: {porcentaje_acum}% Exámen: {porcentaje_examen}%")

    print("------------------------------------------------------------")
    print("Resultados:")

    if (promedio < 3.0):
        # Calcula el faltante para sacar 3.0 como definitiva
        faltante = 3.0 - promedio
        # Calcula la nota mínima del exámen para que la definitiva sea 3.0
        nota_minima_examen = faltante / (porcentaje_examen / 100)

        if (nota_minima_examen > 5.0):
            print(f"Ya perdió la materia, necesita en el examen final: {nota_minima_examen:.2f}")
            def_si_sacara_5 = promedio + 5.0 * porcentaje_examen / 100
            if (def_si_sacara_5 >= 2.5 and def_si_sacara_5 <= 2.9):
                print(f"Puede presentar habilitación, si saca 5.0 en el exámen final su definitiva sería: {def_si_sacara_5:.2f}")
            else:
                print(f"No puede presentar habilitación, si saca 5.0 en el exámen final la definitiva sería: {def_si_sacara_5:.2f}")
        else:
            print(f"Debe presentar el exámen, su promedio ponderado es: {promedio:.2f}")
            print(f"La nota mínima del exámen final ser: {nota_minima_examen:.2f}")
    else:
        print(f"No necesita presentar el exámen, ya tiene: {promedio:.2f}")

    print("------------------------------------------------------------")
    input("Presione Enter para volver al menú...")

#####################################################################################
# Opcion 2.	Cálculo del promedio ponderado del semestre
#####################################################################################

def opcion2():
   # Se pide y valida las materias
    materias = -1
    while materias < 1:
        materias = int(input("Cuantas materias desea ingresar: "))
        if materias < 1:
          print("Debe ser de 1 en adelante")

    sumatoria_nota = 0
    sumatoria_creditos = 0  
    i = 0
    # Se piden todas las materias con sus créditos
    while i < materias:  
        nota = -1
        # Pide y valida la nota
        while nota < 0 or nota > 5.0:
            nota = float(input("Nota: "))
            if (nota < 0 or nota > 5.0):
                print("La nota debe estar entre 0.0 y 5.0")
        
        creditos = int(input("Creditos: "))
        # Acumula las notas y los créditos
        sumatoria_nota += nota * creditos
        sumatoria_creditos += creditos 
        i = i + 1
    
    # Calcula el promedio
    promedio = sumatoria_nota / sumatoria_creditos
    
    # Muestra los resultados
    print("------------------------------------------------------------")
    print(f"El promedio ponderado es: {promedio}")
    print("------------------------------------------------------------")
    input("Presione Enter para volver al menú...")

#####################################################################################
# Opcion 3.	Liquidación de la matrícula del siguiente semestre
#####################################################################################

def opcion3():
    print("------------------------------------------------------------")
    print("1. INGENIERÍA DE SISTEMAS")
    print("2. INGENIERÍA DE INDUSTRIAL")
    print("3. INGENIERÍA DE ELECTRÓNICA")
    print("------------------------------------------------------------")
    print("¿Que programa desea cursar?")
    print("------------------------------------------------------------")
    
    # Pide y valida el programa
    programa = -1
    while programa < 1 or programa > 3:
        programa = int(input("Elija del 1 al 3: "))
        if programa < 1 or programa > 3:
            print("Debe ser entre 1 y 3")
    
    #Calculo el valor del credito por programa
    valor_credito = 0 
    if programa == 1:
        valor_credito = 170000
    elif programa == 2:
        valor_credito = 270000
    elif programa == 3:
        valor_credito = 180000    
    # Se pide y valida las materias 
    materias = -1
    while materias < 1:
        materias = int(input("Numero de materias: "))
        if materias < 1:
            print("Debe ser de 1 en adelante")
   
    i = 1
    costo_base = 0
    while i <= materias:
        creditos = int(input(f"Numero de creditos Materia {i}: "))
        costo_base += creditos * valor_credito
        i = i + 1
    # se pide y valida el estrato    
    estrato = -1
    while estrato < 1 or estrato > 6:
        estrato = int(input("Digite el estrato de 1 a 6: "))
        if estrato < 1 or estrato > 6:
            print("Debe ser entre 1 y 6")
    # se pide y valida la etnia        
    etnia = -1
    while etnia != "S" and etnia != "N":        
        etnia = str(input("Pertenece a una minoría etníca, S ó N (MAYÚSCULA): "))
        if etnia != "S" and etnia != "N": 
            print("Debe ser S ó N (MAYÚSCULA)")

    descuento_estrato = 0
    if estrato <= 2:
        descuento_estrato = 10/100 * costo_base
    
    descuento_etnía = 0
    if etnia == ("S"):
        descuento_etnía = 5/100 * costo_base
 
    print("------------------------------------------------------------")
    print(f"El costo base es: {costo_base:.2f}")  
    print(f"El descuento pot estrato es: {descuento_estrato:.2f} ")
    print(f"El descuento por etnia es: {descuento_etnía:.2f}")
    print(f"El valor final es : {costo_base - descuento_estrato - descuento_etnía}")
    print("------------------------------------------------------------")
    input("Presione Enter para volver al menú...")  

#####################################################################################
# Opcion 4.	Autorización para presentar las pruebas Saber Pro
#####################################################################################

def opcion4():
    print("------------------------------------------------------------")
    print("1. INGENIERÍA DE SISTEMAS")
    print("2. INGENIERÍA DE INDUSTRIAL")
    print("3. INGENIERÍA DE ELECTRÓNICA")
    print("------------------------------------------------------------")
    print("¿Que programa cursa?")
    print("------------------------------------------------------------")
    
    # se pide y valida programa  
    programa = -1
    while programa < 1 or programa > 3:
        programa = int(input("Elija del 1 al 3: "))
        if programa < 1 or programa > 3:
            print("Debe ser entre 1 y 3")

    #Calculo el valor del credito por programa
    total_creditos = 0 
    if programa == 1:
        total_creditos = 170
    elif programa == 2:
        total_creditos = 169
    elif programa == 3:
        total_creditos = 150  

    creditos_cursados = int(input("Numero de creditos cursados: "))    
    nivel_ingles = int(input("Ultimo nivel de ingles cursado y aprobado: "))

    #calculo del aprobado
    aprobado = creditos_cursados / total_creditos * 100
    
    print("------------------------------------------------------------")
    print("RESULTADOS")
    print("------------------------------------------------------------")
    if aprobado < 75:
        print(f"No puede presentar las pruebas saber pro, aprobó: {aprobado:.2f}% (min 75%)")
    elif nivel_ingles < 5:
        print("No puede presentar las pruebas saber pro, nivel de igles debe ser minimo 5")
    else:
        print("Puede presentar las pruebaas saber pro")

    print("------------------------------------------------------------")
    input("Presione Enter para volver al menú...")     

#####################################################################################
# Programa principal
#####################################################################################

opcion = 1
while opcion != 0: 
    print("---------------------------------------------")
    print("        PROGRAMA DE CONSULTA ACADEMICA")
    print("---------------------------------------------")
    print("1. Cálculo de la nota final para pasar una asignatura")
    print("2. Cálculo del promedio ponderado del semestre")
    print("3. Liquidación de la matrícula del siguiente semestre")
    print("4. Autorización para presentar las pruebas Saber Pro")
    print("0. Salir")

    opcion = int(input("Elija una opción del 0 al 4: "))       

    if opcion == 1:
        opcion1()
    elif opcion == 2:
        opcion2()
    elif opcion == 3:
        opcion3()   
    elif opcion == 4:
        opcion4()
    elif opcion == 0:
        print("Elijio Salir") 
    else:
        print("Opción incorrecta")   

    os.system("clear")              

