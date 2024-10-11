from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import abrirArquivo
import os

def criptografar_rsa():
    caminho_arquivo = abrirArquivo.abrir_navegador_arquivos()

    if caminho_arquivo:
        
        caminho_chavePublica = os.path.join('keys', 'chavePublicaAssimetrica.pem')

        with open(caminho_chavePublica, 'rb') as filePublico:
            chave_publica = serialization.load_pem_public_key(filePublico.read())
        
        with open(caminho_arquivo, 'rb') as arquivo:
            conteudo_arquivo = arquivo.read()
        
            criptografado = chave_publica.encrypt(
            conteudo_arquivo,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
            with open(caminho_arquivo, 'wb') as arquivo_criptografado:
                arquivo_criptografado.write(criptografado)
