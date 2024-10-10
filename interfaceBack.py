import tkinter as tk
from tkinter import messagebox
import criacaoDeChave

def confirmar_mudar_chaveSimetrica():
    confirmacao = messagebox.askokcancel("Confirmação", "Caso você tenha arquivos criptografados com a chjave atual é recomendado ou baixa-lá ou descriptografar os arquivos antes, deseja continuar?")

    if confirmacao:
        criacaoDeChave.criacaoChaveSimetrica()
