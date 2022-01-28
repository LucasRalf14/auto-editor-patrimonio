import pyautogui
import time
import PySimpleGUI as sg

try:
    pyautogui.FAILSAFE = True #para parar bruscamente a execução do programa

    #ler arquivo para ver o último número da última executação
    arquivo = open("lastNumber.txt", "r")

    #função para salvar o valor obtido
    def salvar (valor):
        arquivo = open("lastNumber.txt", "w")
        arquivo.write(valor)

    sg.popup('INSTRUÇÕES!\n\n- Ter certeza que o arquivo word a ser editado está aberto\n- O usuário terá que digitar o valor inicial para a execução' + 
            '\n- O usuário terá 5 (cinco) segundos após a confirmação do valor inicial para clicar na primeira imagem antes da automação iniciar'
            +'\n- O usuário sera informado quando for finalizado\n- Não salvar o documento' + 
            '\n- Na próxima vez que o programa for executado, será autopreenchido o próximo valor referente ao último valor da última vez que foi executado\n', title= 'Lista de instruções', text_color='white', background_color='#0000FF', button_color=('white', '#228B22'))

    layout = [  [sg.Text('', background_color='#0000FF')], 
                [sg.Text('Quantidade:', text_color='white', background_color='#0000FF'), sg.InputText(size=(5, 10), justification='center'), 
                sg.Text('Número inicial:', text_color='white', background_color='#0000FF'), sg.InputText(arquivo.readline(6), size=(15, 20), justification='center')],
                [sg.Text('', background_color='#0000FF')],
                [sg.Button('OK', size=(8, 0)), sg.Button('Cancelar', size=(8, 0))]]

    window = sg.Window('Editor Automático de Patrimônio', layout, size=(370, 130), resizable = True, background_color='#0000FF', button_color=('white', '#228B22'), element_justification='c')

    while True:             
        event, values = window.read()
        
        count = 0
        
        #Pegar e converter o primeiro valor do dict values
        qtd_numeros = int(values[0])

        #Pegar e converter o segundo valor do dict values
        valor = str(values[1]).zfill(6)

        if event in (sg.WIN_CLOSED, 'Cancelar'):
            break
        if event == 'OK':
            window.close()
            
            time.sleep(5)
            
            #primeiro valor sendo colocado após o usuário clicar
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.typewrite(valor)
            numero = int(valor) #converte para inteiro para poder incrementar
            numero += 1
            valor = str(numero).zfill(6) #converte de volta para string - zfill para preencher com zeros
            pyautogui.press('esc')

            countTabs = 3
            while count < qtd_numeros:
                #repetir o aperto da tecla TAB
                while countTabs > 0:
                    pyautogui.press('tab')
                    countTabs -= 1
                countTabs = 3
                pyautogui.typewrite(valor)
                pyautogui.press('esc')
                count += 1
                numero = int(valor) #converte para inteiro para poder incrementar
                numero += 1
                valor = str(numero).zfill(6) #converte de volta para string - zfill para preencher com zeros
                salvar(valor)
            sg.popup('>>>CONCLUÍDO COM SUCESSO!<<<\n\nObs: Não salvar o arquivo word.', title= 'finalizado', text_color='white', background_color='#0000FF', button_color=('white', '#228B22'))

    window.close()
    
except Exception:
    pass