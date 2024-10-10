from cryptography.fernet import Fernet
import abrirArquivo
import os


def criptografar():
 caminho_arquivo = abrirArquivo.abrir_navegador_arquivos()

 if caminho_arquivo:
  
  caminho_chaveSimetrica = os.path.join('keys', 'chaveSimetrica.key')
  with open(caminho_chaveSimetrica, 'rb') as filekey:
     chave = filekey.read()

  fernet = Fernet(chave)

  with open(caminho_arquivo, 'rb') as arquivo:
     conteudo_arquivo = arquivo.read()

  criptografado = fernet.encrypt(conteudo_arquivo)

  with open(caminho_arquivo, 'wb') as arquivo_criptografado:
     arquivo_criptografado.write(criptografado)
