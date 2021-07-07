import solucao_candidata

a=solucao_candidata.solucao_candidata()
a.f=((1),(5))
a.nome="A"

b=solucao_candidata.solucao_candidata()
b.f=((2),(3))
b.nome="B"

c=solucao_candidata.solucao_candidata()
c.f=((4),(1))
c.nome="C"

d=solucao_candidata.solucao_candidata()
d.f=((3),(4))
d.nome="D"

e=solucao_candidata.solucao_candidata()
e.f=((4),(3))
e.nome="E"

f=solucao_candidata.solucao_candidata()
f.f=((5),(5))
f.nome="F"

solucoes=((a),(b),(c),(d),(e),(f))

primeira_front =[]

for i in solucoes:
    i.rank=0
    i.np=0
    for j in solucoes:
        if i.f[0]==j.f[0] and i.f[1]==j.f[1]:
            pass
        else:
            if j.f[0]>=i.f[0] and j.f[1]>=i.f[1] :
                i.sp.append(j)
            elif j.f[0]<=i.f[0] and j.f[1]<=i.f[1]:
                i.np += 1
   
    if i.np==0:

        i.rank=1
        primeira_front.append(i)

print("primeira fronteira")
for n in primeira_front:
    print(n.nome)
    
fronteiras = []
fronteiras.append(primeira_front)

var = 1
while primeira_front != []:
    Q=[]
    for i in primeira_front:
        for j in i.sp:
            j.np = j.np-1
            if j.np == 0:
                j.rank=var+1
                Q.append(j)
    fronteiras.append(Q) 
    var= var+1
    print ("fronteira ("+str(var)+")")
    for i in Q:
        print(i.nome)
    primeira_front=Q
    

    