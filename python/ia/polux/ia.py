try:
	file = open('data.txt', 'r')
except FileNotFoundError:
	file = open('data.txt', 'w')
	file.writelines(["-1", "\n", "{}", "\n", "{}", "\n", "{}", "\n", "{}"])
	file.close()
	file = open('data.txt', 'r')
content = file.readlines()
rep = int(content[0])
dico = eval(content[1])
question = eval(content[2])
synonyme = eval(content[3])
blacklist = eval(content[4])
choix = {}
blackwords = ["et", "mais", "ou", "or", "ni", "car", "que", "?", "!", ".", "aux", "de"]
execute = True
motblack = None
file.close()
print('pose moi une question, si tu ne veux pas répond moi "/", cela fermera le programme et enregistrera les nouveaux mots.')
while execute == True:
    inter = input("")
    if inter == "/":
        execute = False
        file = open('data.txt', 'w')
        file.writelines([str(rep), "\n", str(dico), "\n", str(question), "\n", str(synonyme), "\n", str(blacklist)])
        file.close()
    elif inter == "/adddata":
        destination = input("Entrer la destination du fichier")
        try:
            file = open(destination, 'r')
        except FileNotFoundError:
            print("La destination du fichier est introuvable")
        else:
            print("Ajout des données en cours...")
            content = file.readlines()
            repadd = int(content[0])
            dicoadd = eval(content[1])
            questionadd = eval(content[2])
            synonymeadd = eval(content[3])
            blacklistadd = eval(content[4])
            for a in dicoadd.copy():
                b = a + rep + 1
                dico.update({b: dicoadd[a]})
            for a in questionadd.copy():
                b = a + rep + 1
                question.update({b: questionadd[a]})
            synonyme.update(synonymeadd)
            for a in blacklistadd.copy():
                for b in blacklistadd[a].copy():
                    for d in list(blacklistadd[a].values()):
                        c = b + rep + 1
                        blacklistadd[a] = {c: d}
                        blacklist.update(blacklistadd)
            rep = int(content[0]) + rep + 1
            file.close()
            print("Ajout des données terminé !")
    else:
        reponse = inter.split('-')
        reponse = " ".join(reponse)
        reponse = reponse.split(' ')
        if rep == -1:
            print("hum...")
            rep = 0
            question[rep] = reponse
            motblack = input("que dois-je répondre  ?")
            dico[rep] = motblack
        else:
            verif = True
            for i in range(rep+1):
                choix[i] = 0
                for b in reponse:
                    repetition = []
                    for a in question[i]:
                        verifi = True
                        for x in blackwords:
                            if x == b:
                                verifi = False
                        for n in repetition:
                            if a == n:
                                verifi = False
                        if verifi == True:
                            if a == b:
                                choix[i] = choix[i] + 1
                                repetition.append(a)
                            if synonyme != {}:
                                for g in synonyme:
                                    try:
                                        synonyme[g]
                                    except NameError:
                                        synonyme[g] = []
                                    for h in synonyme[g]:
                                        if h == a and g == b:
                                            choix[i] = choix[i] + 1
                                        elif h == b and g ==a:
                                            choix[i] = choix[i] + 1
            try:
                for i in range(rep+1):
                    for c in blacklist:
                        for l in blacklist[c]:
                            for m in blacklist[c][l]:
                                if c == motblack:
                                    if m == dico[i]:
                                        choix[i] = 0
            except KeyError:
                r = None
            choisinombre = 0
            choisi = 0.5
            posibili = 0
            for i in range(rep+1):
                if choix[i] > choisi:
                    choisi = choix[i]
                    posibili = 1
                elif choix[i] == choisi:
                    posibili = posibili + 1
            for i in range(rep+1):
                if verif == True:
                    if choix[i] >= 1:
                        choisitexte = dico[i]
                        choisinombre = choix[i]
                        nombre = i
                        verif = False
                elif choix[i] > choisinombre:
                    choisitexte = dico[i]
                    choisinombre = choix[i]
                    nombre = i
                elif choix[i] == choisinombre:
                    import random
                    ex = (random.random())
                    if ex <= 1 / posibili:
                        choisitexte = dico[i]
                        choisinombre = choix[i]
                        nombre = i
            if verif == False:
                import random
                ex = (random.random())
                rand = 0
                for d in reponse:
                    rand = rand + 1
                calcul = 1 / rand
                ok = True
                for f in reponse:
                    if ok == True:
                        if ex <= calcul:
                            syn = f
                            ok = False
                        calcul = calcul + calcul
                print(choisitexte)
                verification = True
                check = input("J'ai bien répondu ? (oui/non)")
                if check == "non":
                    try:
                        blacklist[motblack][i]
                    except KeyError:
                        try:
                            blacklist[motblack].update({i: []})
                        except KeyError:
                            blacklist[motblack] = {i: []}
                    blacklist[motblack].update({i: []})
                    blacklist[motblack][i].append(choisitexte)
                    rep = rep + 1
                    question[rep] = reponse
                    motblack = input("que dois-je répondre  ?")
                    dico[rep] = motblack
                    verification = False
                if verification == True:
                    motblack = choisitexte
                import random
                ex = (random.random())
                if ex <= 0.2:
                    interme ="donne moi un synonyme du mot", syn, ",non = /"
                    itermediaire = " ".join(interme)
                    syno = input(itermediaire)
                    if syno != "/":
                        if syno != "":
                            try:
                                synonyme[syn]
                            except KeyError:
                                synonyme[syn] = []
                            synonyme[syn].append(syno)
            else:
                rep = rep + 1
                question[rep] = reponse
                motblack = input("que dois-je répondre  ?")
                dico[rep] = motblack