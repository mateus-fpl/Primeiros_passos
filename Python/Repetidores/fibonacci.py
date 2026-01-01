n = int(input("Quantos termos você quer ver? "))
a = 0
b = 1
cont = 0 

while cont < n:
    print(a, end=" ")
    
    a, b = b, a + b
    
    cont += 1 
print (n)