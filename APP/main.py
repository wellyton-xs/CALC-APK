from kivy.app import App
from kivy.lang import Builder
GUI = Builder.load_file("tela.kv")
class MeuAplicativo(App):
    def build(self):
        return GUI
    def on_start(self):
        self.root.ids["calcular"].on_release = self.Imc
        self.root.ids["peso"].multiline = False
        self.root.ids["altura"].multiline = False
    def Imc(self):
        global msg, imc, peso, altura
        peso = float(self.root.ids["peso"].text)
        altura = float(self.root.ids["altura"].text)
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
        self.root.ids["mensagem"].text = f"{msg}"
MeuAplicativo().run()