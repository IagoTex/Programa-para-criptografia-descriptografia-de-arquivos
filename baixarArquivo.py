import tkinter as tk
from tkinter import filedialog

def salvar_arquivo(arquivoOriginal):
    
    root = tk.Tk()
    root.withdraw()

    caminho_onde_salvar = filedialog.asksaveasfilename(
        defaultextension=".key",
        filetypes=[("Chave", "*.key")]
    )

    if caminho_onde_salvar:
        
        with open(arquivoOriginal, 'rb') as arquivoCopiado:
           conteudoCopiado = arquivoCopiado.read()

        with open(caminho_onde_salvar, 'wb') as copia:
            copia.write(conteudoCopiado)
    
        print(f"Arquivo salvo em {caminho_onde_salvar}")
        return caminho_onde_salvar if caminho_onde_salvar else None
        
        

            