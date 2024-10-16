from cryptography.fernet import Fernet
import abrirArquivo
import os

def descriptografar():
 caminho_arquivo_criptografado = abrirArquivo.abrir_navegador_arquivos()

 if caminho_arquivo_criptografado:
  
  caminho_chaveSimetrica = os.path.join('keys', 'chaveSimetrica.key')
  with open(caminho_chaveSimetrica, 'rb') as filekey:
     chave = filekey.read()

  fernet = Fernet(chave)

  with open(caminho_arquivo_criptografado, 'rb') as arquivo_criptografado:
     criptografado = arquivo_criptografado.read()

  descriptografado = fernet.decrypt(criptografado)

  with open(caminho_arquivo_criptografado, 'wb') as arquivo_descriptografado:
     arquivo_descriptografado.write(descriptografado)