from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import string

class Tela:

    def __init__(self):

        #Iniciar Tela
        self.tela = Tk()
        self.tela.geometry("400x400")
        self.tela.title("Gerador de Senha")
        self.tela.configure(background="#484f60")

        self.style = ttk.Style(self.tela)
        self.style.theme_use("clam")

        #Campo da senha
        self.campo_senha = Entry(self.tela, font=(70), width=35,)
        self.campo_senha.place(x=40, y=20)
        self.campo_senha.configure(background="#feffff" )

        #SpinBox
        self.var =IntVar()
        self.var.set(8)
        self.qtd_caracter = Spinbox(self.tela, from_=0, to=32, width=10, textvariable=self.var,)
        self.qtd_caracter.place(x=60, y=100)

        #Botoes
        self.botao_copia = Button(self.tela, text="Copiar", width=35, font=70, relief="flat", activebackground="#6f9fbd", fg="#feffff", command=self.copiar_senha)
        self.botao_copia.place(x=40, y=50)
        self.botao_copia.configure(background="#444466")

        self.botao_gerar = Button(self.tela, text="Gerar Senha", width=35, font=70, command=self.gerar_senha, relief="flat", activebackground="#6f9fbd", fg="#feffff")
        self.botao_gerar.place(x=40, y=350)
        self.botao_gerar.configure(background="#444466")

        #CheckBox Letra Maiuscula, Minuscula, numeros e simbolos
        self.estado_1 = StringVar()
        self.estado_1.set('0')  # seta o estado do CheckButton
        self.ch_1 = Checkbutton(self.tela, var=self.estado_1 ,text="Incluir letras maiusculas", width=30, font=50, activebackground="#6f9fbd")
        self.ch_1.place(x=25, y=150)
        self.ch_1.configure(background="#484f60")

        self.estado_2 = StringVar()
        self.estado_2.set('0')  # seta o estado do CheckButton
        self.ch_2 = Checkbutton(self.tela, var=self.estado_2 ,text="Incluir letras minusculas", width=30, font=50, activebackground="#6f9fbd")
        self.ch_2.place(x=25, y=200)
        self.ch_2.configure(background="#484f60")

        self.estado_3 = StringVar()
        self.estado_3.set('0')  # seta o estado do CheckButton
        self.ch_3 = Checkbutton(self.tela, var=self.estado_3 ,text="Incluir numeros", width=24, font=50, activebackground="#6f9fbd")
        self.ch_3.place(x=23, y=250)
        self.ch_3.configure(background="#484f60")
        
        self.estado_4 = StringVar()
        self.estado_4.set('0')  # seta o estado do CheckButton
        self.ch_4 = Checkbutton(self.tela, var=self.estado_4 ,text="Incluir simbolos", width=29, font=50, activebackground="#6f9fbd")
        self.ch_4.place(x=0, y=300)
        self.ch_4.configure(background="#484f60")
        self.tela.mainloop()


    def gerar_senha(self):
        self.alfa_menor = string.ascii_lowercase
        self.alfa_maior = string.ascii_uppercase
        self.numeros = '0123456789'
        self.simbolos = "!#$%&()*+,-./:;" 
        
        self.combinado = ""

        if self.estado_1.get() == '1':
            self.combinado += self.alfa_maior

        if self.estado_2.get() == '1':
            self.combinado += self.alfa_menor

        if self.estado_3.get() == '1':
            self.combinado += self.numeros

        if self.estado_4.get() == '1':
            self.combinado += self.simbolos

        self.senha = "".join(random.sample(self.combinado, int(self.qtd_caracter.get())))
        self.campo_senha.delete(0, END)
        self.campo_senha.insert(0, self.senha)   

    def copiar_senha(self):
        self.info = self.senha
        self.tela.clipboard_clear()
        self.tela.clipboard_append(self.info)
        messagebox.showinfo("Sucesso","A senha foi copiada com sucesso") 

Tela()