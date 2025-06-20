import random

# fonction d'ouverture des données
def setup():
    try:
        file = open("data.txt", "r", encoding="utf-8")
    except FileNotFoundError:
        file = open("data.txt", "w", encoding="utf-8")
        file.writelines(["-1", "\n", "{}", "\n", "{}", "\n", "{}", "\n", "{}"])
        file.close()
        file = open("data.txt", "r")
    content = file.readlines()
    rep = int(content[0])
    dico = eval(content[1])
    question = eval(content[2])
    for i in question:
        question[i] = question[i].split(" ")
    synonyme = eval(content[3])
    blacklist = eval(content[4])
    blackwords = ["et", "mais", "ou", "or", "ni", "car", "que", "?", "!", ".", "de", "donc", ";", ":", "", " "]
    back = None
    file.close()
    return back, blacklist, dico, rep, question, synonyme, blackwords

# fonction de sauvegarde des nouveaux mots
def close(blacklist, dico, rep, question, synonyme):
    execute = False
    for i in question:
        question[i] = " ".join(question[i])
    file = open("data.txt", "w", encoding="utf-8")
    file.writelines(
        [
            str(rep),
            "\n",
            str(dico),
            "\n",
            str(question),
            "\n",
            str(synonyme),
            "\n",
            str(blacklist),
        ]
    )
    file.close()
    return execute

# fonction d'ajout de données
def adddata(blacklist, dico, rep, question, synonyme):
    destination = input("Entrer la destination du fichier")
    try:
        file = open(destination, "r")
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
        return blacklist, dico, rep, question, synonyme


# fonction transforme la phrase en liste de mot
def liste(inter):
    reponse = inter.split("-")
    reponse = " ".join(reponse)
    reponse = reponse.split(",")
    reponse = " ".join(reponse)
    reponse = reponse.split(".")
    reponse1 = " ".join(reponse)
    reponse = reponse1.split(" ")
    return reponse1, reponse


# fonction si c'est la première fois
def first(back, dico, rep, question):
    print("hum...")
    rep = 0
    question[rep] = reponse
    dico[rep] = input("que dois-je répondre  ?")
    back = rep
    back, dico, rep, question

# fonction scan toutes les phrases et établit leur pertinence
def scan(back, reponse1, blacklist, rep, question, synonyme, blackwords, reponse):
    choix = {}
    verif = True
    for i in range(rep + 1):
        choix[i] = 0
        try:
            if back in blacklist:
                if reponse1 in blacklist[back]:
                    if i in blacklist[back][reponse1]:
                        choix[i] = None
        except KeyError:
            pass
        for b in reponse:
            repetition = []
            verifi = True
            use = True
            verification = True
            if b in blackwords:
                if reponse == question[i]:
                    print("oui")
                    verification = True
                else:
                    verification = False
            for n in repetition:
                if n in question[i]:
                    verifi = False
            if verifi == True:
                if b in question[i]:
                    if choix[i] != None:
                        if verifi == True:
                            if verification == False:
                                choix[i] += 1
                            else:
                                choix[i] += 2
                    else:
                        choix[i] = 0
                # on vérifi si des synonymes du mot existent
                elif synonyme != {}:
                    # si un mot de la question a des synonymes avec la phrase traitée
                    if b in synonyme:
                        for h in synonyme[b]:
                            if use == True:
                                if h in question[i]:
                                    if choix[i] != None:
                                        if verification == False:
                                            choix[i] += 1
                                        else:
                                            choix[i] += 2
                                    else:
                                        choix[i] = 0
                    # si un mot de la phrase traitée a des synonymes avec la question
                    for h in synonyme:
                        if use == True:
                            if h in question[i]:
                                for g in synonyme[h]:
                                    if g == b:
                                        if choix[i] != None:
                                            if verification == False:
                                                choix[i] += 1
                                            else:
                                                choix[i] += 2
                                        else:
                                            choix[i] = 0
            repetition.append(b)
    return choix

# fonction choisi une phrase
def chose(dico, rep, choix):
    verif = True
    choisivaleur = 0
    possibili = 0
    pertinente = []
    # on compte le nombre de possibilités
    for i in range(rep + 1):
        if verif == True:
            if choix[i] >= 1:
                choisivaleur = choix[i]
                verif = False
                nombre = i
                choisitexte = dico[i]
                print(i, "-", choix[i], dico[i])
                pertinente = [i]
                possibili = 0
        elif choix[i] > choisivaleur:
            choisivaleur = choix[i]
            nombre = i
            choisitexte = dico[i]
            print(i, "-", choix[i], dico[i])
            pertinente = [i]
            possibili = 0
        elif choix[i] == choisivaleur:
            possibili += 1
            pertinente.append(i)
            print(i,"-", choix[i], dico[i])
    # on désigne la réponse choisi
    if possibili > 1:
        ex = random.randint(0, possibili)
        nombre = pertinente[ex]
        choisitexte = dico[pertinente[ex]]
    if verif == False:
        return verif, nombre, dico, rep, choisitexte
    else:
        return verif, None, dico, rep, None

# fonction corriger si mal répondu
def check(verif, back, reponse1, blacklist, nombre, dico, rep, question, reponse):
    verification = True
    check = input("J'ai bien répondu ? (oui/non)")
    if check == "non":
        # ajout à la blacklist
        if back in blacklist:
            if reponse1 in blacklist[back]:
                blacklist[back][reponse1].append(nombre)
            else:
                blacklist[back][reponse1] = [nombre]
        else:
            blacklist[back] = {reponse1: [nombre]}
        rep += 1
        question[rep] = reponse
        dico[rep] = input("que dois-je répondre  ?")
        back = rep
        verification = False
    if verification == True:
        back = nombre
    return back, blacklist, dico, rep, question


# fonction synonyme
def synonymes(synonyme, reponse):
    ex = random.random()
    if ex <= 0.2:
        if len(reponse) > 1:
            ex = random.randint(0, len(reponse) - 1)
            inter = "donne moi un synonyme du mot :", reponse[ex], ",non = /"
            inter = " ".join(inter)
            syno = input(inter)
        else:
            inter = "donne moi un synonyme du mot:", reponse[0], ",non = /"
            inter = " ".join(inter)
            syno = input(inter)
            ex = 0
        if syno != "/":
            if syno != "":
                if reponse[ex] in synonyme:
                    synonyme[reponse[ex]].append(syno)
                else:
                    synonyme[reponse[ex]] = [syno]
    return synonyme


# fonction si rien n'a été trouvé
def ask(back, dico, rep, question, reponse):
    rep += 1
    question[rep] = reponse
    dico[rep] = input("que dois-je répondre ?")
    back = rep
    return back, dico, rep, question, reponse


# fonction principale
def main():
    back, blacklist, dico, rep, question, synonyme, blackwords = setup()
    print('pose moi une question, si tu ne veux pas répond moi "/", cela fermera le programme et enregistrera les nouveaux mots.')
    execute = True
    # boucle jusqu'à fermeture du programme
    while execute == True:
        inter = input("")
        if inter == "/":
            # ferme le programme
            execute = close(blacklist, dico, rep, question, synonyme)
        elif inter == "/adddata":
            # ajout de fichier
            blacklist, dico, rep, question, synonyme = adddata(blacklist, dico, rep, question, synonyme)
        else:
            reponse1, reponse = liste(inter)
            # si c'est la première fois
            if rep == -1:
                back, dico, rep, question = first(back, dico, rep, question, reponse)
            else:
                choix = scan(back, reponse1, blacklist, rep, question, synonyme, blackwords, reponse)
                verif, nombre, dico, rep, choisitexte = chose(dico, rep, choix)
                if verif == False:
                    print(choisitexte)
                    back, blacklist, dico, rep, question = check(verif, back, reponse1, blacklist, nombre, dico, rep, question, reponse)
                    synonyme = synonymes(synonyme, reponse)
                else:
                    back, dico, rep, question, reponse = ask(back, dico, rep, question, reponse)


"""--------------------------------------------------------------------------------
                                >>> execution >>>
"""


main()
