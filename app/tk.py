def Imc():
    global entrada_altura, entrada_peso, texto
    peso = float(entrada_peso.get())
    altura = float(entrada_altura.get())
    imc = peso / altura**2

    if imc < 18.5:
        indice["text"] = "VOCÊ ESTÁ ABAIXO DO PESO NORMAL E O SEU IMC É: {:.2f}".format(imc)
    elif imc >= 18.5 and imc < 24.9:
        indice["text"] = "VOCÊ ESTÁ NO PESO NORMAL E O SEU IMC É: {:.2f}".format(imc)
    elif imc >= 25.0 and imc < 29.9:
        indice["text"] = "VOCÊ ESTÁ EM EXCESSO DE PESO E O SEU IMC É: {:.2f}".format(imc)
    elif imc >= 30.0 and imc < 34.9:
        indice["text"] = "VOCÊ ESTÁ EM OBESIDADE CLASSE I E O SEU IMC É: {:.2f}".format(imc)
    elif imc >= 35.0 and imc < 39.9:
        indice["text"] = "VOCÊ ESTÁ EM OBESIDADE CLASSE II E O SEU IMC É: {:.2f}".format(imc)
    elif imc >= 40:
        indice["text"] = "VOCÊ ESTÁ EM OBESIDADE CLASSE III E O SEU IMC É: {:.2f}".format(imc)


from tkinter import *
janela = Tk()
janela.geometry("250x250")
janela.title("Calculadora de IMC")

texto = Label(janela, text="DIGITE SEU PESO")
texto.grid(column=0, row=0)

entrada_peso = Entry(janela, width=30)
entrada_peso.grid(column=1, row=0)

texto2 = Label(janela, text="DIGITE SUA ALTURA")
texto2.grid(column=0, row=1)

entrada_altura = Entry(janela, width=30)
entrada_altura.grid(column=1, row=1)



indice = Label(janela, text="")
indice.grid(column=0, row=3)

botao= Button(janela, text="Calcular", command=Imc)
botao.grid(column=0, row=4)

janela.mainloop()