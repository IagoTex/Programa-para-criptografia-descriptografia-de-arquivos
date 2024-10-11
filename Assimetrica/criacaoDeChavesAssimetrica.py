from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os

def criacaoChavesAssimetricas():

     chave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
     
     pasta = "keys"
     os.makedirs(pasta, exist_ok=True)

     caminho_chave_privada = os.path.join(pasta, 'chavePrivadaAssimetrica.pem')
     caminho_chave_publica = os.path.join(pasta, 'chavePublicaAssimetrica.pem')

     with open(caminho_chave_privada, 'wb') as file_privado:
          file_privado.write(
                chave_privada.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
          )
     chave_publica = chave_privada.public_key()
     with open(caminho_chave_publica, 'wb') as file_publico:
          file_publico.write(
                chave_publica.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
          )

