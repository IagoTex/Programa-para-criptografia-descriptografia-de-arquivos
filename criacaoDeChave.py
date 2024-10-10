from cryptography.fernet import Fernet
import os

def criacaoChaveSimetrica():
 chave = Fernet.generate_key()

 pasta = "keys"
 os.makedirs(pasta, exist_ok=True)

 caminho_chave = os.path.join(pasta, 'chaveSimetrica.key')

 with open(caminho_chave, 'wb') as filekey:
     filekey.write(chave)