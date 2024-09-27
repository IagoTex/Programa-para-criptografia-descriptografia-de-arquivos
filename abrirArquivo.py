import tkinter as tk
from tkinter import filedialog


def abrir_navegador_arquivos():
    root = tk.Tk()
    root.withdraw()  
    
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*"))
    )
    
    if caminho_arquivo:
        print(f"Arquivo selecionado: {caminho_arquivo}")
    else:
        print("Nenhum arquivo selecionado.")
    
    return caminho_arquivo if caminho_arquivo else None



