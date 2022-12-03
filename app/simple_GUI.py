import PySimpleGUI as sg
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Entre com seu peso e sua altura')],
            [sg.Text('Digite seu peso com "."', key="peso"), sg.InputText()],
            [sg.Text('Digite sua altura com "."', key="altura"), sg.InputText()],
            [sg.Text( '', key="resultado")],
            [sg.Button('Calcular'), sg.Button('Cancel')]
        ]
# Create the Window
janela = sg.Window('Calculadora de IMC', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "Calcular":
            peso = float(values[0])
            altura = float(values[1])
            imc = peso / altura**2
            if imc < 18.5:
                msg = "VOCÊ ESTÁ ABAIXO DO PESO NORMAL E O SEU IMC É: {:.2f}".format(imc)
            elif imc >= 18.5 and imc < 24.9:
                msg = "VOCÊ ESTÁ NO PESO NORMAL E O SEU IMC É: {:.2f}".format(imc)
            elif imc >= 25.0 and imc < 29.9:
                msg = "VOCÊ ESTÁ EM EXCESSO DE PESO E O SEU IMC É: {:.2f}".format(imc)
            elif imc >= 30.0 and imc < 34.9:
                msg = "VOCÊ ESTÁ EM OBESIDADE CLASSE I E O SEU IMC É: {:.2f}".format(imc)
            elif imc >= 35.0 and imc < 39.9:
                msg = "VOCÊ ESTÁ EM OBESIDADE CLASSE II E O SEU IMC É: {:.2f}".format(imc)
            elif imc >= 40:
                msg = "VOCÊ ESTÁ EM OBESIDADE CLASSE III E O SEU IMC É: {:.2f}".format(imc)
        
            janela['resultado'].update(msg)
janela.close()