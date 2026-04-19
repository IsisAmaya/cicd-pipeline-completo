# app/calculadora.py
"""
Funciones basicas de una calculadora
"""

import math

AUTORES = "icamayaa@eafit.edu.co"


def sumar(a, b):
    """
    Suma de dos numeros
    """
    return a + b


def restar(a, b):
    """
    Resta de dos numeros
    """
    return a - b


def multiplicar(a, b):
    """
    Multiplicacion de dos numeros
    """
    return a * b


def dividir(a, b):
    """
    Division de dos numeros
    Implementa manejo de error para no dividir por cero
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


def potencia(a, b):
    """
    Potencia, a elevado a b
    """
    return a**b


def raiz_cuadrada(a):
    """
    Raiz cuadradada de a
    """
    return math.sqrt(a)
