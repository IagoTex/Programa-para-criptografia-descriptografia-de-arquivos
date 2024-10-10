from tkinter import *
from tkinter import ttk
import criptografiaSimetrica
import descriptografiaSimetrica
import opcoes
import interfaceBack
import os

#Janela principal
janela = Tk()
janela.title("Cripto Iago")

pasta = 'midias'
os.makedirs(pasta, exist_ok=True)
caminhoIcone = os.path.join(pasta, 'icone.png')
icone = PhotoImage(file=caminhoIcone)
janela.iconphoto(False, icone)


texto_orientacao = Label(janela, text="Programa para criptografar arquivos", font=("Arial", 20, "bold"))
texto_orientacao.grid(column=0, row=0)

#Controlador de Abas
controle_de_abas = ttk.Notebook(janela)

tab_criptografia = ttk.Frame(controle_de_abas)
tab_descriptografia = ttk.Frame(controle_de_abas)
tab_hash = ttk.Frame(controle_de_abas)
tab_opcoes = ttk.Frame(controle_de_abas)

controle_de_abas.add(tab_criptografia, text="Criptografia simétrica")
controle_de_abas.add(tab_descriptografia, text="Criptografia assimétrica")
controle_de_abas.add(tab_hash, text="Hash")
controle_de_abas.add(tab_opcoes, text="Opções")

controle_de_abas.grid(column=0, row=1, sticky="nsew")

#Aba de criptografia simétrica:
texto_criptografia = Label(tab_criptografia, text="Criptografia simétrica")
texto_criptografia.grid(column=0, row=0)
botao_criptografia = Button(tab_criptografia, cursor="hand2", bg='#ffde21', fg='black', text="Selecionar arquivo", command=criptografiaSimetrica.criptografar)
botao_criptografia.grid(column=0, row=1)
texto_descriptografia = Label(tab_criptografia, text="Selecione o arquivo que você deseja descriptografar")
texto_descriptografia.grid(column=0, row=2)
botao_descriptografia = Button(tab_criptografia,cursor="hand2", bg='#ffde21', fg='black', text="Selecionar arquivo", command=descriptografiaSimetrica.descriptografar)
botao_descriptografia.grid(column=0, row=3)


#Aba de descriptografia:


#Aba de opções:
texto_opcoes = Label(tab_opcoes, text="Opções")
texto_opcoes.grid(column=0, row=0)

texto_opcoes_simetrica = Label(tab_opcoes, text="Criptografia simétrica:")
texto_opcoes_simetrica.grid(column=0, row=1)
botao_copiar_chaveSimetrica = Button(tab_opcoes, text="Copiar chave atual", command=opcoes.CopiarChaveSimetrica)
botao_copiar_chaveSimetrica.grid(column=0, row=2)
botao_mudar_chaveSimetrica = Button(tab_opcoes, text="Mudar chave atual", command=interfaceBack.confirmar_mudar_chaveSimetrica)
botao_mudar_chaveSimetrica.grid(column=0, row=3)







janela.mainloop()