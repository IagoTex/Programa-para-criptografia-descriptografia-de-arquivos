from cryptography.fernet import Fernet
import abrirArquivo


def criptografar():
 caminho_arquivo = abrirArquivo.abrir_navegador_arquivos()

 if caminho_arquivo:
  with open('chave.key', 'rb') as filekey:
     chave = filekey.read()

  fernet = Fernet(chave)

  with open(caminho_arquivo, 'rb') as arquivo:
     conteudo_arquivo = arquivo.read()

  criptografado = fernet.encrypt(conteudo_arquivo)

  with open(caminho_arquivo, 'wb') as arquivo_criptografado:
     arquivo_criptografado.write(criptografado)
