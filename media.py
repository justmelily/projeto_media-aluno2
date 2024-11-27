print ("insira as 4 notas")
n1 = float(input())
n2 = float(input())
n3 = float(input())
media = (n1 * 1 + n2 * 1 + n3 * 2  ) / 4
if media > 6 :
 print ("aprovado")
elif media < 5:
 print ("reprovado ")
else : print ("recuperação")