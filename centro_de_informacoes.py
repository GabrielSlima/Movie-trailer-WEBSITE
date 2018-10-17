import filmes
import tomatoes_gabriel
import sys
from pyshorteners import Shortener
 
''' TODOS OS NOSSO OBJETOS/FILMES 

    ESTRUTURA: 
    TITULO, 
    ENDERECO DO POSTER, 
    LINK DO TRAILER NO YOUTUBE
'''
#ENCURTADOR DE URLs
encurtador = Shortener('Tinyurl') #OBJETO ENCURTADOR UTILIZANDO O ENCURTADOR Tinyulr

got = filmes.Filme(
    'Game of Thrones', 
    'https://www.gstatic.com/tv/thumb/tvbanners/14160794/p14160794_b_v8_aa.jpg',
    'https://www.youtube.com/watch?v=7cUELYuzRGc'
    )

mr_robot= filmes.Filme(
    'Mr. ROBOT', 
    'https://elladog.com.ar/wp-content/uploads/2017/10/postermrrobot.jpg',
    'https://www.youtube.com/watch?v=xIBiJ_SzJTA'
    )

interstellar = filmes.Filme(
    'Interstellar',
    'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg',
    'https://www.youtube.com/watch?v=zSWdZVtXT7E'
    )

the_imitation_game = filmes.Filme(
    'The imitation game',
    'https://www.gstatic.com/tv/thumb/v22vodart/10771057/p10771057_v_v8_ah.jpg',
    'https://www.youtube.com/watch?v=5gcyB72nFmc'
    )

minha_mae_peca = filmes.Filme(
    'Minha mãe é uma peça',
    'https://m.media-amazon.com/images/M/MV5BYWE3YWM5NDQtN2ZlZi00ZWY0LTg4M2QtMGNjMjEwNzAzY2M2XkEyXkFqcGdeQXVyMTkzODUwNzk@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
    'https://www.youtube.com/watch?v=HrST-4WLlbA'
    )

my_wife_and_kids = filmes.Filme(
    'My wife and kids',
    'https://images-na.ssl-images-amazon.com/images/I/81lnE8Sf6ZL._RI_.jpg', 
    'https://www.youtube.com/watch?v=oNf606dfCb0'
    )

snowden = filmes.Filme(
    'Snowden',
    'https://www.gstatic.com/tv/thumb/v22vodart/11823926/p11823926_v_v8_an.jpg',
    'https://www.youtube.com/watch?v=QlSAiI3xMh4'
    )

todos_filmes = [got,mr_robot, interstellar, the_imitation_game,minha_mae_peca,my_wife_and_kids, snowden]

# VERIFICAÇÃO DOS ATRIBUTOS DOS FILMES 
for filme in range(len(todos_filmes)):
    if todos_filmes[filme].titulo == '' or todos_filmes[filme].endereco_poster == '' or todos_filmes[filme].endereco_trailer == '': # SE QUALQUER ATRIBUTO FOR VAZIO
        print('Alguma informação não está correta, por favor, cheque o Script de centro de informações.')
        sys.exit()  # ENCERRA A EXECUÇÃO DO SCRIPT

    if len(todos_filmes[filme].endereco_poster) > 80:
        print(todos_filmes[filme].titulo)
        url_encurtada = encurtador.short(todos_filmes[filme].endereco_poster)
        todos_filmes[filme].endereco_poster = url_encurtada
        

# TRATANDO ERROS DE ATRIBUTO
try:
    tomatoes_gabriel.abrir_pagina_filmes(todos_filmes)
except AttributeError:
    print('Talvez você tenha se confundido e informado uma foto ao invés de um endereço do YouTube, por favor, cheque o Script de centro de informações.')
