
import solucao_candidata
from typing import Final

# cria soluções
a=solucao_candidata.solucao_candidata()
a.f=[1,5]
a.nome="A"

b=solucao_candidata.solucao_candidata()
b.f=[2,3]
b.nome="B"

c=solucao_candidata.solucao_candidata()
c.f=[4,1]
c.nome="C"

d=solucao_candidata.solucao_candidata()
d.f=[1.5,4]
d.nome="D"


solucoes=[a,b,c,d]
solucoesaux:Final = [a,b,c,d]
vr = 0
for x in solucoes:
    vr=vr+1

tamanho = vr 
m = 2
vetorcomp = []
for x in solucoes:
    vetorcomp.append(x.f)

vetorcomp.sort(reverse=True)

for x in range(len(vetorcomp)):
    for item in solucoesaux:
        if item.f[0] == vetorcomp[x][0] and item.f[1] == vetorcomp[x][1]:
            solucoes[x]=item

        
for x in range(m):
    solucoes[0].distance=float("inf")
    solucoes[len(solucoes)-1].distance=float("inf")



for x in range(m):
    y=1
    for y in range(len(solucoes)-1):
        aux = (solucoes[y+1].f[x] - solucoes[y-1].f[x])/(solucoes[tamanho-1].f[x]-solucoes[0].f[x])
        solucoes[y].distance = solucoes[y].distance + aux
        
for x in solucoes:
    print(x.nome,x.distance,sep=" = ")
 