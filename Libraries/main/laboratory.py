"""
Solución del laboratorio
"""
def climas(a):
 try:
    import statistics
    guajira={"Enero":32,"Febrero":33,"Marzo":42,"Abril":40,"Mayo":43,"Junio":55,"Julio":35,"Agosto":40,"Septiembre":38,"Octubre":35,"Novimbre":32,"Diciembre":30}
    santander={"Enero":27,"Febrero":20,"Marzo":24,"Abril":26,"Mayo":28,"Junio":25,"Julio":23,"Agosto":22,"Septiembre":24,"Octubre":26,"Novimbre":25,"Diciembre":22}
    narino={"Enero":24,"Febrero":25,"Marzo":24,"Abril":23,"Mayo":22,"Junio":25,"Julio":26,"Agosto":22,"Septiembre":27,"Octubre":25,"Novimbre":24,"Diciembre":22}

    if a=="Guajira":
        print("-El departamento de eleccion es: ", a, "\n -Acontinuacion se le pedira opciones para ingresar: ","\n  -Si escribe el nombre del mes, podra saber ese mes en especifico","\n  -Si escribe TODOS, se imprimiran todos los meses","\n  -Escriba MAX para saber el de mayor temperatura","\n  -Y por ultimo PROM para saber el promedio del departamento")
        b = input("\n-Opcion o mes: ")
        if b=="TODOS":
            for keys, values in guajira.items():
                print(keys,values,"°C")
        else:
            if b=="MAX":

                print("La temperatura maxima regitrada es:",max(guajira, key=guajira.get),max(guajira.values()),"°C")
            else:
                if b=="PROM":
                    c=sum(guajira.values())
                    print("La temperatura promedio es: ",c/12,"°C")
                else:
                    if b == "ESTANDAR":
                        print("la desviacion estandar de Guajira es: ", statistics.stdev(guajira.values()), "°C")
                    else:

                        print("La temperatura en: ",b,"es de: ", guajira[b],"°C")



    if a == "Santander":
        print("-El departamento de eleccion es: ", a, "\n -Acontinuacion se le pedira opciones para ingresar: ","\n  -Si escribe el nombre del mes, podra saber ese mes en especifico","\n  -Si escribe TODOS, se imprimiran todos los meses","\n  -Escriba MAX para saber el de mayor temperatura","\n  -Y por ultimo PROM para saber el promedio del departamento")
        b = input("\n-Opcion o mes: ")
        if b == "TODOS":
            for keys, values in santander.items():
                print(keys,values,"°C")

        else:
            if b == "MAX":
                print("La temperatura maxima regitrada es:", max(santander, key=santander.get), max(santander.values()),"°C")
            else:
                if b == "PROM":
                    c = sum(santander.values())
                    print("La temperatura promedio es: ", c / 12,"°C")
                else:
                    if b == "ESTANDAR":
                        print("la desviacion estandar de Santander  es: ", statistics.stdev(santander.values()), "°C")
                    else:
                        print("La temperatura en: ", b, "es de: ", santander[b],"°C")


    if a == "Nariño":
        print("-El departamento de eleccion es: ", a, "\n -Acontinuacion se le pedira opciones para ingresar: ","\n  -Si escribe el nombre del mes, podra saber ese mes en especifico","\n  -Si escribe TODOS, se imprimiran todos los meses","\n  -Escriba MAX para saber el de mayor temperatura","\n  -Y por ultimo PROM para saber el promedio del departamento")
        b = input("\n-Opcion o mes: ")
        if b == "TODOS":
            for keys, values in narino.items():
                print(keys, values, "°C")
        else:
            if b == "MAX":
                print("La temperatura maxima regitrada es:", max(narino, key=narino.get), max(narino.values()),"°C")
            else:
                if b == "PROM":
                    c = sum(narino.values())
                    print("La temperatura promedio es: ", c / 12,"°C")
                else:
                    if b == "ESTANDAR":
                        print("la desviacion estandar de Nariño es: ", statistics.stdev(narino.values()), "°C")
                    else:
                        print("La temperatura en: ", b, "es de: ", narino[b],"°C")

    if a=="Nacional":
        print("-El departamento de eleccion es: ", a, "\n -Acontinuacion se le pedira opciones para ingresar:","\n  -Quiere saber la  desviacion estandar, entonces coloque ESTANDAR, y se le dara esta informcaion ","\n  -Si quere saber cual de los 3 departamentos anteriores mencionados es el mayor y su promedio, ingrese MAX","\n  -Si quiere saber le mes mas caliente de todos los departamentos y en que mes, ingrese ULTIMATE")
        b=input("\nOpcion a elegir: ")
        if b=="ESTANDAR":
            print("la desviacion estandar de Guajira es: ",statistics.stdev(guajira.values()),"°C")
            print("la desviacion estandar de Nariño es: ",statistics.stdev(narino.values()),"°C")
            print("la desviacion estandar de la Santander es: ",statistics.stdev(santander.values()),"°C")
        else:
            if b=="MAX":
                promG=sum(guajira.values())/12
                promS=sum(santander.values()) / 12
                promN=sum(narino.values()) / 12
                promL=[promN,promG,promS]

                print("El promedio de La guajira es de: ",promG)
                print("El promedio de La Santander es de: ", promS)
                print("El promedio de La Nariño es de: ",promN)
                print("El mayor de todos las temperaturas es el de: ",max(promL))
            else:
                if b=="ULTIMATE":
                    ultimateG=max(guajira.values())
                    ultimateS=max(santander.values())
                    ultimateN=max(narino.values())
                    if ultimateG>ultimateS and ultimateG>ultimateN:
                        print("En la Guajira se registro la temperatura maxima en: ",max(guajira, key=guajira.get),"con: ", max(narino.values()),"°C")
                    else:
                        if ultimateS>ultimateN and ultimateS>ultimateG:
                            print("En el Santander se registro la temperatura maxima en: ", max(santander, key=santander.get),"con: ", max(narino.values()),"°C")
                        else:
                            if ultimateN>ultimateG and ultimateN>ultimateS:
                                print("En el Nariño se registro la temperatura maxima en: ",max(narino, key=narino.get),"con: ", max(narino.values()),"°C")

    b = input("-Quiere continuar?, Si/No: ")
    while b!="No":
         a = input("-Ingrese un departamento entre\n-Santander\n-Nariño\n-Guajira\n-O elegirlo a nivel nacional\n:")
         climas(a)
         if a=="No":
             break

    else:
        print("Muchas gracias por usar nuestro programa")
 except:
     print("Error al digitar lo pedido, por favor intentelo despues.")




a=input("-Ingrese un departamento entre\n-Santander\n-Nariño\n-Guajira\n-O elegirlo a nivel Nacional\n:")
climas(a)



