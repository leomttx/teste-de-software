#Lista de Testes: 
# verificar se forma um triangulo valido
# Se as entradas tiverem todos os lados iguais, o triângulo precisa retornar equilátero.
# Se as entradas tiverem todos os lados diferentes, o triângulo precisa retornar escaleno.
# Se as entradas tiverem dois lados iguais, o triângulo precisa retornar isósceles.

a = int(input("lado 1: "))
b = int(input("lado 2: "))
c = int(input("lado 3: "))
valido = False

# verificar se forma um triangulo valido
if a + b > c and a + c > b and b + c > a:
    valido = True

if valido:
    if a == b and b == c:
        print("Equilátero")
    elif a != b and a != c and b != c:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Não é um triângulo válido")










