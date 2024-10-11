from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import abrirArquivo
import os

def descriptografar_rsa():
    caminho_arquivo_criptografado = abrirArquivo.abrir_navegador_arquivos()

    if caminho_arquivo_criptografado:

        caminho_chavePrivada = os.path.join('keys', 'chavePrivadaAssimetrica.pem')

        with open(caminho_chavePrivada, 'rb') as filePrivado:
            chave_privada = serialization.load_pem_private_key(filePrivado.read(), password = None)

        with open(caminho_arquivo_criptografado, 'rb') as arquivo_criptografado:
            conteudo_criptografado = arquivo_criptografado.read()

        try:

            conteudo_original = chave_privada.decrypt(
                conteudo_criptografado,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )    

            with open(caminho_arquivo_criptografado, 'wb') as arquivo_original:
                arquivo_original.write(conteudo_original)
        
        except Exeption as e:
            print("Erro")
        


