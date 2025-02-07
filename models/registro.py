# -*- coding: utf-8 -*-
"""
Módulo que contiene la clase base Registro.
"""

class Registro:
    """
    Clase base para todos los registros.

    Attributes:
        id (str): Identificador único del registro.
    """
    def __init__(self, id):
        self.id = id