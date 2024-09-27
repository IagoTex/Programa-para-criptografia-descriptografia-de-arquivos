from cryptography.fernet import Fernet
import abrirArquivo

def descriptografar():
 caminho_arquivo_criptografado = abrirArquivo.abrir_navegador_arquivos()

 if caminho_arquivo_criptografado:
  with open('chave.key', 'rb') as filekey:
     chave = filekey.read()

  fernet = Fernet(chave)

  with open(caminho_arquivo_criptografado, 'rb') as arquivo_criptografado:
     criptografado = arquivo_criptografado.read()

  descriptografado = fernet.decrypt(criptografado)

  with open(caminho_arquivo_criptografado, 'wb') as arquivo_descriptografado:
     arquivo_descriptografado.write(descriptografado)