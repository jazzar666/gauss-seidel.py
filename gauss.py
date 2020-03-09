def seidel(a, x ,b): 

#Longitud de búsqueda de un (3)
    n = len(a)
# for loop por 3 veces como para calcular x, y, z
    for j in range(0, n):         

# variable temporal d para almacenar b [j]
        d = b[j]                   

          
# para calcular respectivas xi, yi, zi
        for i in range(0, n):      

            if(j != i): 

                d-=a[j][i] * x[i] 

# actualizar el valor de nuestra solución
        x[j] = d / a[j][j] 

# devolviendo nuestra solución actualizada
    return x     

   
# int (input ()) entrada como número de variable a resolver
n = 3                              

a = []                             

b = []         
# solución inicial dependiendo de n (aquí n = 3)
x = [0, 0, 0]                         

a = [[4, 1, 2],[3, 5, 1],[1, 1, 3]] 

b = [4,7,3] 

print(x) 

  
# ejecución en bucle m veces dependiendo de m el valor de error
for i in range(0, 5):             

    x = seidel(a, x, b) 

#print cada vez que la solución actualizada
    print(x)
