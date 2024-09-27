from tkinter import *
from tkinter import ttk
import criptografia
import descriptografia

#Janela principal
janela = Tk()
janela.title("Cripto Iago")

texto_orientacao = Label(janela, text="Programa para criptografar arquivos")
texto_orientacao.grid(column=0, row=0)

#Controlador de Abas
controle_de_abas = ttk.Notebook(janela)

tab_criptografia = ttk.Frame(controle_de_abas)
tab_descriptografia = ttk.Frame(controle_de_abas)

controle_de_abas.add(tab_criptografia, text="Criptografia")
controle_de_abas.add(tab_descriptografia, text="Descriptografia")

controle_de_abas.grid(column=0, row=1, sticky="nsew")


#Aba de criptografia:
texto_criptografia = Label(tab_criptografia, text="Selecione o arquivo que você deseja criptografar")
texto_criptografia.grid(column=0, row=0)
botao_criptografia = Button(tab_criptografia, text="Selecionar arquivo", command=criptografia.criptografar)
botao_criptografia.grid(column=0, row=1)


#Aba de descriptografia:
texto_descriptografia = Label(tab_descriptografia, text="Selecione o arquivo que você deseja descriptografar")
texto_descriptografia.grid(column=0, row=0)
botao_descriptografia = Button(tab_descriptografia, text="Selecionar arquivo", command=descriptografia.descriptografar)
botao_descriptografia.grid(column=0, row=1)





janela.mainloop()