# -*- coding: utf-8 -*-
class Filme:
    """
        Essa classe fornece um metodo construtor para novos objetos.
        Para todo novo objeto criado um novo espaço em memoria é
        reservado para ele e seus atributos, ou seja, copias dessas
        variaveis são criadas.
    """
    def __init__(self, titulo, endereco_poster, endereco_trailer):
        """
            titulo: String - Guarda do titulo do objeto
            endereco_poster: String - Guarda uma URL do poster do objeto
            endereco_trailer: String - Guarda uma URL do YouTube,
                              é o trailer do objeto
        """
        self.titulo = titulo
        self.endereco_poster = endereco_poster
        self.endereco_trailer = endereco_trailer

