# coding: utf-8
from random import randint
from typing import Union
from termcolor import colored
from colorama import init
import os, sys

os.system('cls')

init()

def banner() -> None:
    texto = """
     █████╗ ██████╗ ██╗██╗   ██╗██╗███╗   ██╗██╗  ██╗███████╗     █████╗         
    ██╔══██╗██╔══██╗██║██║   ██║██║████╗  ██║██║  ██║██╔════╝    ██╔══██╗        
    ███████║██║  ██║██║██║   ██║██║██╔██╗ ██║███████║█████╗      ███████║        
    ██╔══██║██║  ██║██║╚██╗ ██╔╝██║██║╚██╗██║██╔══██║██╔══╝      ██╔══██║        
    ██║  ██║██████╔╝██║ ╚████╔╝ ██║██║ ╚████║██║  ██║███████╗    ██║  ██║        
    ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝        
                                                                                
            ██████╗  █████╗ ██╗      █████╗ ██╗   ██╗██████╗  █████╗             
            ██╔══██╗██╔══██╗██║     ██╔══██╗██║   ██║██╔══██╗██╔══██╗            
            ██████╔╝███████║██║     ███████║██║   ██║██████╔╝███████║            
            ██╔═══╝ ██╔══██║██║     ██╔══██║╚██╗ ██╔╝██╔══██╗██╔══██║            
            ██║     ██║  ██║███████╗██║  ██║ ╚████╔╝ ██║  ██║██║  ██║            
            ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝            

                                                GitHub: https://github.com/Jonathan-Freire      
    """

    print(colored(texto, 'magenta'))
    print(colored('='*100, 'magenta'))

banner()
print('\n')
def comoJogar() -> None:
    print(colored(' COMO JOGAR ? '.center(100, '*'), 'cyan'))
    print(colored('1. Digite qualquer palavra de 5 dígitos', 'yellow'))
    print(colored('2. Você terá pistas do quão perto chegou da palavra correta pela cor de fundo.\n', 'yellow'))
    print(colored(' [ ~ ] Fundo Amarelo: A letra existe na palavra mas está em outra posição. ', 'grey', 'on_yellow'))
    print(colored(' [ ~ ] Fundo Verde: A letra existe na palavra e está na posição correta. ', 'grey', 'on_green'))
    print(colored(' [ ~ ] Fundo Vermelho: A letra não existe na palavra. ', 'grey', 'on_red'))
    print(colored('*'*100, 'cyan'))
comoJogar()

def mensagemVitoria() -> None:
    mensagem_vitoria = """
     █████╗  ██████╗███████╗██████╗ ████████╗ ██████╗ ██╗   ██╗    ██╗
    ██╔══██╗██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██║   ██║    ██║
    ███████║██║     █████╗  ██████╔╝   ██║   ██║   ██║██║   ██║    ██║
    ██╔══██║██║     ██╔══╝  ██╔══██╗   ██║   ██║   ██║██║   ██║    ╚═╝
    ██║  ██║╚██████╗███████╗██║  ██║   ██║   ╚██████╔╝╚██████╔╝    ██╗
    ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝     ╚═╝
                                                                                                                                                                                          
    """
    print(colored(mensagem_vitoria, 'green'))

def jogarNovamente() -> bool:
    pergunta = input(colored('[ ? ] Deseja jogar novamente ?\n[ 1 ] Sim\n[ 2 ] Não\nR: ', 'yellow'))
    while pergunta not in ['1', '2']:
        print(colored('[ ! ] Opção inválida, digite apenas o número da opção desejada.\n', 'red'))
        pergunta = input(colored('[ ? ] Deseja jogar novamente ?\n[ 1 ] Sim\n[ 2 ] Não\nR: ', 'yellow'))

    if pergunta == '1':
        return True
    elif pergunta == '2':
        return False

# Dicionários com as letras que irão ser substituidas
letras = {
    'á' : 'a',
    'ã' : 'a',
    'â' : 'a',
    'é' : 'e',
    'ê' : 'e',
    'í' : 'i',
    'ó' : 'o',
    'ô' : 'o',
    'ú' : 'u',
    'ç' : 'c'
}

# Função que escolhe uma palavra aleatória
def escolherPalavra() -> str:
    try:
        # Ler todo o conteúdo do arquivo txt contendo as palavras
        with open('palavras-jogo.txt', 'r', encoding='utf-8') as palavras:
            todas_palavras = palavras.readlines()
        # escolher um numero aleatório entre 0 e a quantidade de palavras que tem no 
        # arquivo txt
        numero_palavra_escolhida = randint(0, len(todas_palavras))
        return todas_palavras[numero_palavra_escolhida]
    except Exception as erroEscolherPalavra:
        mensagemErro = f'Erro ao escolher uma palavra.\nErro: {erroEscolherPalavra}'
        return mensagemErro

# Validar se a palavra digitada é a correta
def validarTentativa(palavra_tentativa: str, palavra_correta: str) -> Union[bool, str]:
    try:
        # 🟩 🟥 🟨
        tentativa_jogador_simbolo = ''
        tentativa_jogador = ''

        for index, letra_palavra_tentativa in enumerate(palavra_tentativa):
            # Validar quais letras tem na palavra
            if letra_palavra_tentativa in palavra_correta:
                
                # Validar se a letra está na mesma posição
                if letra_palavra_tentativa == palavra_correta[index]:
                    tentativa_jogador_simbolo += '🟩 '
                    tentativa_jogador += colored(f' {letra_palavra_tentativa.upper()} ', 'grey', 'on_green')
                else:
                    tentativa_jogador_simbolo += '🟨 '
                    tentativa_jogador += colored(f' {letra_palavra_tentativa.upper()} ', 'grey', 'on_yellow')
            else:
                tentativa_jogador_simbolo += '🟥 '
                tentativa_jogador += colored(f' {letra_palavra_tentativa.upper()} ', 'grey', 'on_red')

        print(tentativa_jogador_simbolo)
        print(tentativa_jogador)
        print('\n')

        # Validar se é a palavra correta
        if palavra_tentativa == palavra_correta:
            return True
        else:
            return False

    except Exception as erroValidarTentativa:
        mensagemErro = f'Erro ao tentar validar a palavra do jogador.\nErro: {erroValidarTentativa}'
        return mensagemErro

# ===== INICIAR EXECUÇÃO DO CÓDIGO =====
if __name__ == '__main__':

    with open('palavras-dicionario-5-letras.txt', 'r', encoding='utf-8') as dicionario:
        palavras_dicionario = dicionario.readlines()
        palavras_dicionario = [palavra.replace('\n', '') for palavra in palavras_dicionario]

    palavra_correta = escolherPalavra()
    maximo_tentativas = 5
    tentativas_realizadas = 1

    # Tirar os acentos para comparar as palavras e transformar em minúsculas
    palavra_correta = palavra_correta.lower().translate(str.maketrans(letras)).replace('\n', '')

    while tentativas_realizadas <= maximo_tentativas:
        palavra_tentativa = input(colored(f'[ ~ ] {tentativas_realizadas}º Tentativa: ', 'green'))
        # Tirar os acentos para comparar as palavras e transformar em minúsculas
        palavra_tentativa = palavra_tentativa.lower().translate(str.maketrans(letras)).replace('\n', '')

        while len(palavra_tentativa) != 5 or palavra_tentativa not in (palavras_dicionario):
            if len(palavra_tentativa) != 5:
                print(colored('\n[ ! ] A palavra deve conter 5 letras.\n', 'yellow'))
            elif palavra_tentativa not in (palavras_dicionario):
                print(colored('\n[ ! ] A palavra digitada não existe.\n', 'yellow'))

            palavra_tentativa = input(colored(f'[ ~ ] {tentativas_realizadas}º Tentativa: ', 'green'))
            palavra_tentativa = palavra_tentativa.lower().translate(str.maketrans(letras)).replace('\n', '')

        acertou_tentativa = validarTentativa(palavra_tentativa, palavra_correta)
        tentativas_realizadas += 1

        if acertou_tentativa:
            mensagemVitoria()
            # Perguntar se deseja jogar novamente
            jogar_novamente = jogarNovamente()
            if jogar_novamente:
                tentativas_realizadas = 1
                palavra_correta = escolherPalavra()
                palavra_correta = palavra_correta.lower().translate(str.maketrans(letras)).replace('\n', '')
                print(palavra_correta)
            else:
                sys.exit(0)
    else:
        print(colored('[ - ] Suas tentativas acabaram, você não conseguiu acertar a palavra correta =(', 'red'))
        print(colored('[ - ] A palavra era: ', 'red') + colored(f' {palavra_correta} ', 'grey', 'on_green'))
        sys.exit(0)