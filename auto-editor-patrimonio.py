import pyautogui
import time

pyautogui.FAILSAFE = True #para parar bruscamente a execução do programa

#pyautogui.alert("Instruções:\n\n 1- Não mexer em nada após executar o script, somente o que for pedido \n2 - Certificar-se que abriu o documento primeiro e com a janela maximizada")

count = 0
valor = pyautogui.prompt(text='Digite o valor inicial', title='Editor de patrimonio ' , default='')

pyautogui.alert("A edição vai começar...")
time.sleep(3)

#lista(tuplas) com as posições para o mouse se mover #50 posicoes
posicoes1 = [(672, 279), (829, 275), (990, 279), (1140, 280), (1308, 278), #1
            (674, 355), (850, 355), (991, 358), (1131, 359), (1291, 355),  #2
            (670, 436), (842, 435), (992, 442), (1139, 437), (1287, 441),  #3
            (681, 513), (831, 516), (999, 520), (1142, 520), (1285, 518),  #4
            (674, 598), (839, 597), (980, 600), (1148, 598), (1295, 597),  #5
            (680, 681), (832, 677), (985, 681), (1139, 681), (1277, 683),  #6
            (671, 752), (842, 753), (998, 755), (1147, 752), (1292, 748),  #7
            (674, 832), (837, 836), (987, 839), (1140, 837), (1284, 835),  #8
            (665, 913), (843, 912), (990, 919), (1151, 916), (1303, 916),  #9
            (672, 993), (834, 992), (983, 998), (1144, 993), (1284, 997)]  #10

posicoes2 = [(668, 776), (822, 776), (989, 782), (1132, 781), (1283, 775), #1
            (672, 854), (841, 855), (989, 861), (1131, 854), (1279, 853),  #2
            (670, 935), (836, 935), (981, 939), (1150, 938), (1297, 934)]  #3

#percorre a lista de posicoes e digita os valores

while count < 65:
    if count < 50:
        for posicao in posicoes1:
            pyautogui.moveTo(posicao)
            pyautogui.doubleClick()
            pyautogui.typewrite(valor)
            count += 1
            numero = int(valor) #converte para inteiro para poder incrementar
            numero += 1
            valor = str(numero).zfill(6) #converte de volta para string - zfill para preencher com zeros
    elif count >= 50:
        #scrolldown
        time.sleep(2.5)
        pyautogui.scroll(-1000)
        
        #mais 15 posicoes
        for posicao in posicoes2:
            pyautogui.moveTo(posicao)
            pyautogui.doubleClick()
            pyautogui.typewrite(valor)
            count += 1
            numero = int(valor) #converte para inteiro para poder incrementar
            numero += 1
            valor = str(numero).zfill(6) #converte de volta para string - zfill para preencher com zeros
    else:
        pyautogui.alert("Ocorreu um erro!")

#pagedown
#pyautogui.press('pgdn')
#pyautogui.press('pgdn')
#pyautogui.press('pgdn')
#time.sleep(3)

time.sleep(5)
pyautogui.alert("A edição foi finalizada!")