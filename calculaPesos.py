arquivo = open('dados_segunda.txt','r')
dados = arquivo.readlines()
todosEnlaces = []
enlacesUnicos = []

#Coloca todos os enlaces em uma lista e coloca os enlaces unicos em outra lista
for z in range(len(dados)):
    todosEnlaces.append(dados[z][:-1])
    if dados[z][:-1] not in enlacesUnicos:
        enlacesUnicos.append(dados[z][:-1])
arquivo.close() 

#Calcula quantas vezes um enlace unico acontece em todosEnlaces, o resultado e o peso que sera adicionado ao par de nos 
pesos = []
for y in range(len(enlacesUnicos)):
    quantidade = todosEnlaces.count(enlacesUnicos[y])
    separar = enlacesUnicos[y].split(" ")
    inf = separar[0]+' '+separar[1]+" "+str(quantidade)+'\n'
    pesos.append(inf)

arquivo2 = open('pesos.edgelist','a')
for xp in range(len(pesos)):
    arquivo2.write(pesos[xp])
arquivo2.close()