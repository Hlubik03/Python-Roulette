import random
kapital=int(input("Zadajte kapital: "))
def spin():
    hod=random.randrange(0, 36)
    return hod

def gamble(kapital):
    global padlo, padlokombin,hody,kombinacie,balance,statistika,cierne,cervene
    padlo=[]
    padlokombin={
        'cislo': 0,
        'cierna': 0,
        'cervena': 0,
        'parnost': 0,
        'neparnost': 0,
        '1-15': 0,
        '19-36': 0
    }
    kombinacie=[]
    copadlo=''
    hody={}
    balance=[]
    statistika=[]
    hods=0
    suma=0
    while kapital>0:
        bet=int(input("Zadaj sumu, ktoru chces vsadit: "))
        if bet>0:
            if bet > kapital:
                print("Nemáš dostatek penazi")
                pokracovat=int(input("Chces pokracovat? 1.Áno 2.Nie"))
                if pokracovat==2:
                    print("Tvoj kapital je: {}".format(kapital))
                    break
                elif pokracovat==1:
                    bet=1
            else:
                hod=spin()
                statistika.append(hod)
                padlo.append(hod)
                print(hod)
                co=int(input("Na co chces vsadit? 1.Cislo 2.Cierna 3.Cervena 4.Parnost/Neparnost 5.1-15 6.19-36: "))
                if co==1:
                    copadlo='cislo'
                    kombinacie.append(copadlo)
                    cislo=int(input("Na ake cislo chces vsadit? "))
                    if cislo==hod:
                        print("Vyhral si vsadil si na cislo {} a padlo {}".format(cislo, hod))
                        kapital+=bet*35
                        suma=bet*35
                        balance.append(suma)
                        print("Tvoj kapital je: {}".format(kapital))
                        padlokombin[copadlo] += 1

                    else:
                        print("Prehral sivsadil si na cislo {} a padlo {}".format(cislo, hod))
                        kapital-=bet
                        suma=-bet
                        balance.append(suma)
                        print("Tvoj kapital je: {}".format(kapital))

                elif co==2:
                    cierne=[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
                    copadlo='cierna'
                    kombinacie.append(copadlo)
                    if hod in cierne:
                        print("Vyhral si vsadil si na ciernu a padlo {}".format(hod))
                        kapital+=bet
                        suma=bet
                        balance.append(suma)
                        print("Tvoj kapital je: {}".format(kapital))
                        padlokombin[copadlo] += 1
                    else:
                        print("Prehral si vsadil si na ciernu a padlo {}".format(hod))
                        kapital-=bet
                        suma=-bet
                        balance.append(suma)
                        print("Tvoj kapital je: {}".format(kapital))
                elif co==3:
                    cervene=[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
                    copadlo='cervena'
                    kombinacie.append(copadlo)
                    if hod in cervene:
                        print("Vyhral si vsadil si na cervenu a padlo {}".format(hod))
                        kapital+=bet
                        suma=bet
                        balance.append(suma)
                        print("Tvoj kapital je: {}".format(kapital))
                        padlokombin[copadlo] += 1
                    else:
                        print("Prehral si vsadil si na cervenu a padlo {}".format(hod))
                        kapital-=bet
                        suma=-bet
                        balance.append(suma)
                        print("Tvoj kapital je: {}".format(kapital))
                elif co==4:
                    parnost=int(input("Na co chces vsadit? 1.Parnost 2.Neparnost: "))
                    if parnost==1:
                        copadlo='parnost'
                        kombinacie.append(copadlo)
                        if hod%2==0:
                            print("Vyhral si vsadil si na parne a padlo {}".format(hod))
                            kapital+=bet
                            suma=bet
                            balance.append(suma)
                            print("Tvoj kapital je: {}".format(kapital))
                            padlokombin[copadlo] += 1
                        else:
                            print("Prehral si vsadil si na parne a padlo {}".format(hod))
                            kapital-=bet
                            suma=-bet
                            balance.append(suma)
                            print("Tvoj kapital je: {}".format(kapital))
                    elif parnost==2:
                        copadlo='neparnost'
                        kombinacie.append(copadlo)
                        if hod%2!=0:
                            print("Vyhral si vsadil si na neparne a padlo {}".format(hod))
                            kapital+=bet
                            suma=bet
                            balance.append(suma)
                            print("Tvoj kapital je: {}".format(kapital))
                            padlokombin[copadlo] += 1
                        else:
                            print("Prehral si vsadil si na neparne a padlo {}".format(hod))
                            kapital-=bet
                            suma=-bet
                            balance.append(suma)
                            print("Tvoj kapital je: {}".format(kapital))
                elif co==5:
                    copadlo='1-15'
                    kombinacie.append(copadlo)
                    if hod>=1 and hod<=15:
                        print("Vyhral si vsadil si na 1-15 a padlo {}".format(hod))
                        kapital+=bet
                        suma=bet
                        balance.append(suma)
                        print("Tvoj kapital je: {}".format(kapital))
                        padlokombin[copadlo] += 1
                    else:
                        print("Prehral si vsadil si na 1-15 a padlo {}".format(hod))
                        kapital-=bet
                        suma=-bet
                        balance.append(suma)
                        print("Tvoj kapital je: {}".format(kapital))
                elif co==6:
                    copadlo='19-36'
                    kombinacie.append(copadlo)
                    if hod>=19 and hod<=36:
                        print("Vyhral si vsadil si na 19-36 a padlo {}".format(hod))
                        kapital+=bet
                        suma=bet
                        balance.append(suma)
                        print("Tvoj kapital je: {}".format(kapital))
                        padlokombin[copadlo] += 1
                    else:
                        print("Prehral si vsadil si na 19-36 a padlo {}".format(hod))
                        kapital-=bet
                        suma=-bet
                        balance.append(suma)
                        print("Tvoj kapital je: {}".format(kapital))
                hods+=1
                hody[hods] = bet
        elif bet==0:
            print("Tvoj kapital je: {}".format(kapital))
            hod=spin()
            padlo.append(hod)
            print("Passol si a padlo cislo {}".format(hod))
            hods+=1
            hody[hods] = bet
            kombinacie.append("pass")
            suma=0
            balance.append(suma)
            continue
        else:
            print("Tvoj kapital je: {}".format(kapital))
            break
    if kapital<=0:
        print("Koniec hry prehral si vsetko")
        return padlo

gamble(kapital)

unikatne=[]
for cislo in padlo:
    if cislo not in unikatne:
        unikatne.append(cislo)

kolkopadlo=[]
for cislo in unikatne:
    kolkopadlo.append(padlo.count(cislo))

skuska=0
output_file_path = '/Users/hlubik03/Documents/programko/zav.projekt/vystup.txt'

for cislo in unikatne:
    kde1 = unikatne.index(cislo)
    kam1 = kolkopadlo[kde1]
    perc = kam1 / len(padlo) * 100
    perc = round(perc, 2)
    vypis1 = ("Cislo {} padlo {} krat co je {}".format(cislo, kam1, perc))
    print(vypis1)
    with open(output_file_path, 'a') as file:
        file.write(vypis1 + '\n')

keys_list = list(padlokombin.keys())
spolu = sum(padlokombin.values())
if spolu > 0:
    for i in range(len(keys_list)):
        key_name = keys_list[i]
        value = padlokombin[key_name]
        perc = value / spolu * 100
        perc = round(perc, 2)
        vypis2 = ("{} kombinacia bola uhadnuta {} krat co je {}".format(key_name, value, perc))
        print(vypis2)
        with open(output_file_path, 'a') as file:
            file.write(vypis2 + '\n')

ciernych=0
cervenych=0
parnych=0
neparnych=0
patnast=0
devatnast=0

for i in statistika:
    if i in cierne:
        ciernych += 1
    elif i in cervene:
        cervenych += 1
    if i % 2 == 0:
        parnych += 1
    elif i % 2 == 1:
        neparnych += 1
    if i >= 1 and i <= 15:
        patnast += 1
    elif i >= 19 and i <= 36:
        devatnast += 1

print("Kombinacia ciernych cisel padla {} krat".format(ciernych))
print("Kombinacia cervenych cisel padla {} krat".format(cervenych))
print("Kombinacia parnych cisel padla {} krat".format(parnych))
print("Kombinacia neparnych cisel padla {} krat".format(neparnych))
print("Kombinacia 1-15 cisel padla {} krat".format(patnast))
print("Kombinacia 19-36 cisel padla {} krat".format(devatnast))


with open(output_file_path, 'a') as file:
    file.write("Kombinacia ciernych cisel padla {} krat".format(ciernych) + '\n')
    file.write("Kombinacia cervenych cisel padla {} krat".format(cervenych) + '\n')
    file.write("Kombinacia parnych cisel padla {} krat".format(parnych) + '\n')
    file.write("Kombinacia neparnych cisel padla {} krat".format(neparnych) + '\n')
    file.write("Kombinacia 1-15 cisel padla {} krat".format(patnast) + '\n')
    file.write("Kombinacia 19-36 cisel padla {} krat".format(devatnast) + '\n')


keys_list2 = list(hody.keys())
for i in range(len(keys_list2)):
    key_name = keys_list2[i]
    komb = kombinacie[i]
    value = hody[key_name]
    penez = balance[i]
    vypis3 = ("V hode cislo {} bola hodnota stavky {} na kombinaciu {} a obrat bol {}".format(key_name, value, komb, penez))
    print(vypis3)
    with open(output_file_path, 'a') as file:
        file.write(vypis3 + '\n')

