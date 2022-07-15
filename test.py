import pyautogui

cod_coordenad = input('QUAL AS COORDENADAS? \n')

print(cod_coordenad)

lenCoord = str(cod_coordenad) #RECEBE VALOR DO da cordenada
if len(lenCoord) < 39:
    lenCoord = lenCoord.zfill(39)
formatedLati = '{},{}'.format(lenCoord[:3], lenCoord[5:19])#FORMATA A STRING COM BASE NA ENUMERACAO da LATITUDE
formatedLong = '{},{}'.format(lenCoord[21:24], lenCoord[25:])#FORMATA A STRING COM BASE NA ENUMERACAO da LONGITUDE

print(formatedLati)
print(formatedLong)
