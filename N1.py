#importar re para utilizar expresiones regulares 
import re

#funcion de buscar para las coincidencias de las palabras ingresadas y los patrones 
def buscar(patrones, texto):
    i=1
    for patron in patrones:
        print("Case #"+str(i)+": " +str(len(re.findall(patron, texto))))
        i +=1

while True:
    print("Ingrese L D N (con un espacio entre cada número)")

    #guardar valores ingresados en lista num en donde num[0] = L, num[1]= D, num[2]= N
    num = input().split(' ')

    #si contine 3 valores 
    if(len(num)==3):
        palabras = []
        d=1

        #ingreso de palabras a D y L 
        while d <= int(num[1]):
            print("Ingrese palabra " +str(d) +" en minúscula y de largo " +num[0] +":")
            
            l = input()
            l = ''.join(l.split())
           
            #validar palabras repetidas
            if l in palabras:
                print ("ERROR! Palabra repetida")

            #validar si es minuscula y del largo solicitado, si es valido agrega palabra a la lista de palabras
            elif(l.islower() and len(l)==int(num[0])):
                palabras.append(l)
                d +=1
            else:
                print("ERROR! Ingrese palabra en minúscula y de largo " +num[0])
        #string de todas las palabras
        texto = ", ".join(palabras)
        patrones = []
        n=1
        
        #ingreso de patrones 
        while n<=int(num[2]):
            print ("Ingrese patron " +str(n))
            s = input()
            temp = []
            #todos los patrones 
            ses = re.findall('[a-z]+',s)
            #solo patrones entre parentesis los cuales seran evaluados mas adelante para agregar | entre ellos 
            ses3 = re.findall('\(([^)]+)', s) 
                    
            i=0
            
            # 1) crear una lista de los valores que se encuentran entreparentesis 
            # 2) agrega un | para separar
            # 3) las guarda entre parentesis y las agrega a temp 

            while(i<len(ses3)):
                
                temp.append("("+'|'.join(list(ses3[i]))+")")

                i +=1
            
            #agregar temp a ses para crear el string de patrones  
            for q, i in enumerate(ses):
                j=0
                while(j<len(ses3)):
        
                    if i == ses3[j]:
                        ses[q] = temp[j]
        
                    j +=1

                    #print(ses)

            final = ''.join(ses)

            patrones.append(final)
            n +=1
        # llama a la funcion buscar para validar si los patrones son validos 
        buscar(patrones, texto)  
        break
    else:
        print("ERROR! Ingrese sólo 3 números con espacio entre ellos")   



