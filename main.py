from tkinter import *

def calcular():
    peso1 = float(peso.get())
    altura1= float(altura.get())
    imc = peso1 / altura1 ** 2
    resposta['text'] = imc


root = Tk()
root.geometry('400x400')


Label( text="Calculando Seu IMC").grid(column=0, row=0, columnspan=2)


Label( text="Digite seu Peso:").grid(column=0, row=1)
peso = Entry(root)
peso.grid(column=1, row=1)


Label( text="Digite sua Altura:").grid(column=0, row=2)
altura = Entry(root)
altura.grid(column=1, row=2)

Button(text="Calcular", command=calcular).grid(column=0, row=3)

resposta = Label( text="Resultado")
resposta.grid(column=1, row=3)


root.mainloop()
