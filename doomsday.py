#doosmday algorithm by boubou
from math import *
def creation_liste(date):
    carac='/'
    x=date.split(carac)
    return x
def century(d):
    if d%4==1:
        return 0
    elif d%4==2:
        return 5
    elif d%4==3:
        return 3
    else:
        return 2
def diff_jour(jour,mois,anne):
    if anne%4==0 and mois==1:
        diff_j=abs(jour-4)
    elif anne%4!=0 and mois==1:
        diff_j=abs(jour-3)
    elif anne%4==0 and mois==2:
        diff_j=abs(jour-29)
    elif anne%4!=0 and mois==2:
        diff_j=abs(jour-3)
    elif mois%2==0:
        diff_j=abs(mois-jour)
    elif mois==3:
        diff_j=abs(14-jour)
    elif mois==5:
        diff_j=abs(9-jour)
    elif mois==7:
        diff_j=abs(11-jour)
    elif mois==9:
        diff_j=abs(5-jour)
    elif mois==11:
        diff_j=abs(7-jour)
    return diff_j
def num_jour(le_jour_nombre):
    if le_jour_nombre==0:
        le_jour_lettre='Dimanche'
    elif le_jour_nombre==1:
        le_jour_lettre='Lundi'
    elif le_jour_nombre==2:
        le_jour_lettre='Mardi'
    elif le_jour_nombre==3:
        le_jour_lettre='Mercredi'
    elif le_jour_nombre==4:
        le_jour_lettre='Jeudi'
    elif le_jour_nombre==5:
        le_jour_lettre='vendredi'
    elif le_jour_nombre==6:
        le_jour_lettre='Samedi'
    return ('le jour de la semaine de cette date est un',le_jour_lettre)   
def doomsday(date):
    date=creation_liste(date)
    date=list(map(int, date))
    j_doomsday_day=(date[3]+(date[3]//4)+century(date[2]))%7
    le_jour_nombre=(j_doomsday_day+diff_jour(date[0],date[1],date[3]))%7
    return num_jour(le_jour_nombre)
def jeu():
    a=input('quel date? veillez a bien l ecrire de la forme 05/09/20/04, c est a vous!         ')
    print(doomsday(a))
jeu()