import pyautogui
import time

exe_venv = open('.venv/Scripts/activate')

time.sleep(1)
def sleep():
    time.sleep(0.5)

print("\n \t==== CHECK LIST ====\n\n• ABRIR O SISTEMA NA PAGINA INICIAL\n• COORDENADAS COPIADAS\n\n")
cod_cliente = input('QUAL O CODIGO DO CLIENTE? \n')
cod_coordenad = input('QUAL AS COORDENADAS? \n')

lenCoord = str(cod_coordenad) #RECEBE VALOR DO da cordenada
if len(lenCoord) < 39:
    lenCoord = lenCoord.zfill(39)
formatedLati = '{},{}'.format(lenCoord[:3], lenCoord[5:19])#FORMATA A STRING COM BASE NA ENUMERACAO da LATITUDE
formatedLong = '{},{}'.format(lenCoord[21:24], lenCoord[25:])#FORMATA A STRING COM BASE NA ENUMERACAO da LONGITUDE

#   PESQUISAR MODULOS
pyautogui.moveTo(628,106, 0.3)
pyautogui.click()
sleep()
# PESQUISA O MODULO CADASTRO DE CLIENTE
pyautogui.typewrite('CADASTRO DE CLIENTE')
time.sleep(2)
pyautogui.moveTo(600,150, 0.3)# clica no modulo descrito
pyautogui.click()
time.sleep(6)

pyautogui.typewrite(cod_cliente)
pyautogui.press('ENTER')
sleep()
pyautogui.moveTo(483,659, 0.3)# clica em ENDS
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(621,239, 0.3)# duplo click no endereco de entrga
pyautogui.doubleClick()
time.sleep(1)

pyautogui.moveTo(976,559, 0.3)# clica em gerenciar coordenadas
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(1027,253, 0.3)# clica em adicionar nova coordenada
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(856, 608, 0.3)# clica em latitude
pyautogui.click()
time.sleep(1)
pyautogui.typewrite(formatedLati)# ESCREVE LATITUDE
sleep()

pyautogui.press('TAB')# VAI PRA LONGITUDE
pyautogui.typewrite(formatedLong)# ESCREVE LATITUDE

pyautogui.moveTo(998, 638, 0.3)# clica em EFETIVA
pyautogui.click()
time.sleep(1)

print("\n ==== \tSANEAMENTO FINALIZADO COM SUCESSO\t ====\n")