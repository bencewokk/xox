x1=" "
y1=" "
z1=" "
x2=" "
y2=" "
z2=" "
x3=" "
y3=" "
z3=" "

x1y1z1=[x1,y1,z1]
x2y2z2=[x2,y2,z2]
x3y3z3=[x3,y3,z3]

x1x2x3=[x1,x2,x3]
y1y2y3=[y1,y2,y3]
z1z2z3=[z1,z2,z3]

x1y2z3=[x1,y2,z3]
z1y2x3=[z1,y2,x3]

koords=["x1","x2","x3","y1","y2","y3","z1","z2","z3"]

jateksz=0
hkoord=[]
jatekos="X"


vege=0
while vege==0:
    if x1y1z1.count(jatekos) == 3:
        vege=1
        print(jatekos, "nyert")
    elif x2y2z2.count(jatekos) == 3:
        vege=1
        print(jatekos, "nyert")
    elif x3y3z3.count(jatekos) == 3:
        print(jatekos, "nyert")
        vege = 1

    elif x1x2x3.count(jatekos) == 3:
        vege = 1
        print(jatekos, "nyert")
    elif y1y2y3.count(jatekos) == 3:
        vege = 1
        print(jatekos, "nyert")
    elif z1z2z3.count(jatekos) == 3:
        print(jatekos, "nyert")
        vege=1
    else:
        x1y1z1 = [x1, y1, z1]
        x2y2z2 = [x2, y2, z2]
        x3y3z3 = [x3, y3, z3]

        x1x2x3 = [x1, x2, x3]
        y1y2y3 = [y1, y2, y3]
        z1z2z3 = [z1, z2, z3]

        x1y2z3 = [x1, y2, z3]
        z1y2x3 = [z1, y2, x3]

        print (x1y1z1)
        print("", x1, "|", y1, "|", z1, " 1")
        print("---+---+---")
        print("", x2, "|", y2, "|", z2, " 2")
        print("---+---+---")
        print("", x3, "|", y3, "|", z3, " 3")
        print(" x   y   z ")

        print("")


        print(jatekos, " jon")
        koord = input("hova raksz?")
        if koord in koords and koord not in hkoord:
            hkoord.append(koord)
            print (hkoord)
            if koord=="x1":
                x1=jatekos
            elif koord=="y1":
                y1=jatekos
            elif koord=="z1":
                z1=jatekos

            elif koord=="x2":
                x2=jatekos
            elif koord == "y2":
                y2 = jatekos
            elif koord == "z2":
                z2 = jatekos

            elif koord=="x3":
                x3=jatekos
            elif koord=="y3":
                y3=jatekos
            elif koord=="z3":
                z3=jatekos

            jateksz += 1
            if jateksz % 2 == 0:
                jatekos = "X"
            else:
                jatekos = "O"

        else:
            print("ervenytelen helyezes")
