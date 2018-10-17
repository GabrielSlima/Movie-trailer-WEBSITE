import filmes
import tomatoes_gabriel
import sys
''' TODOS OS NOSSO OBJETOS/FILMES
    ESTRUTURA:
    TITULO,
    ENDERECO DO POSTER,
    LINK DO TRAILER NO YOUTUBE
'''
got = filmes.Filme(
    'Game of Thrones',
    'https://www.gstatic.com/tv/thumb/tvbanners/14160794/p14160794_b_v8_aa.jpg',  # NOQA
    'https://www.youtube.com/watch?v=7cUELYuzRGc'
    )

mr_robot = filmes.Filme(
    'Mr. ROBOT',
    'https://elladog.com.ar/wp-content/uploads/2017/10/postermrrobot.jpg',
    'https://www.youtube.com/watch?v=xIBiJ_SzJTA'
    )

interstellar = filmes.Filme(
    'Interstellar',
    'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg',  # NOQA
    'https://www.youtube.com/watch?v=zSWdZVtXT7E'
    )

the_imitation_game = filmes.Filme(
    'The imitation game',
    'https://www.gstatic.com/tv/thumb/v22vodart/10771057/p10771057_v_v8_ah.jpg',  # NOQA
    'https://www.youtube.com/watch?v=5gcyB72nFmc'
    )

minha_mae_peca = filmes.Filme(
    'Minha mãe é uma peça',
    'https://m.media-amazon.com/images/M/MV5BYWE3YWM5NDQtN2ZlZi00ZWY0LTg4M2QtMGNjMjEwNzAzY2M2XkEyXkFqcGdeQXVyMTkzODUwNzk@._V1_SY1000_CR0,0,675,1000_AL_.jpg',  # NOQA
    'https://www.youtube.com/watch?v=HrST-4WLlbA'
    )

my_wife_and_kids = filmes.Filme(
    'My wife and kids',
    'https://images-na.ssl-images-amazon.com/images/I/81lnE8Sf6ZL._RI_.jpg',
    'https://www.youtube.com/watch?v=oNf606dfCb0'
    )

snowden = filmes.Filme(
    'Snowden',
    'https://www.gstatic.com/tv/thumb/v22vodart/11823926/p11823926_v_v8_an.jpg',  # NOQA
    'https://www.youtube.com/watch?v=QlSAiI3xMh4'
    )
# TODOS OS FILMES A SEREM ADICIONADOS NA PAGINA WEB
todos_filmes = [
    got,
    mr_robot,
    interstellar,
    the_imitation_game,
    minha_mae_peca,
    my_wife_and_kids,
    snowden]
# VERIFICAÇÃO DOS ATRIBUTOS DOS FILMES
for filme in todos_filmes:
    titulo = filme.titulo
    poster = filme.endereco_poster
    trailer = filme.endereco_trailer
    (
        print(
            'Alguma informação não está correta, por favor,cheque o Script'
            ' de centro de informações.'
            )or sys.exit() if not titulo or not poster or not trailer else None
            )


# TRATANDO ERROS DE ATRIBUTO
try:
    tomatoes_gabriel.abrir_pagina_filmes(todos_filmes)
except AttributeError:
    print(
        'Talvez você tenha se confundido e informado uma foto'
        'ao invés de um endereço do YouTube, por favor, cheque o'
        'Script de centro de informações.'
    )
