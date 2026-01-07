from datetime import datetime

nascimento = int(input("Digite o seu ano de nascimento: "))
idadeatual = int(datetime.now().year) - nascimento
if nascimento > 2008:
    print ("você terá que fazer o alistamento em breve")
elif nascimento < 2008:
    print ("você já passou da idade do alistamento militar")
else:
    print ("você está na idade exata do alistamento militar")

if idadeatual < 18:
    menordeidade = 18 - idadeatual
    saldomenor = int(datetime.now().year) + menordeidade
    print ("Faltam {} anos para você chegar na idade do alistamento, seu alistamento será em {}. ".format(menordeidade,saldomenor))
elif idadeatual > 18:
    maiordeidade = idadeatual - 18
    saldomaior = int(datetime.now().year) - maiordeidade
    print ("Faz {} anos que você deveria ter se alistado, no ano de {}. ".format(maiordeidade,saldomaior))
else:
    print ("O processo deve ser feito este ano")
