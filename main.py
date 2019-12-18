'''
    Autor: Richard Vinueza
    Curso: Estructura de Datos - ESPOCH
    Ejercicio: Funcionamiento basico ArbolB+ (PYTHON 3)
    IDE: PyCharm
    Version: v0.0.3
    Ejecutar: python main.py
'''

from os import system
from models.BPlusTree import BPlusTree

def main():

    print("Iniciando...")
    bplustree = BPlusTree(order=5)

    print('\nInsertando pedido 1 |  Cargando...')
    bplustree.insert('-1.658005$-78.672889', 'Casa')
    bplustree.show()

    print('\nInsertando pedido 2 |  Cargando...')
    bplustree.insert('-1.663581$-78.660529', 'Zeus')
    bplustree.show()

    print('\nInsertando pedido 3 |  Cargando...')
    bplustree.insert('-1.660150$-78.680936', 'Puerta Principal')
    bplustree.show()

    print('\nInsertando pedido 4 |  Cargando...')
    bplustree.insert('-1.660150$-78.690936', 'Lejos2')
    bplustree.show()

    print('\nInsertando pedido 5 |  Cargando...')
    bplustree.insert('-1.660150$-78.689936', 'Lejos1')
    bplustree.show()

    print('|--------  App Rider Activa  --------|')
    
    print("Recomendado: -1.660150$-78.690937")
    position = input("Ingresa tu posicion:")
    system('clear')

    print('\nEstos son los pedios que puedes recojer segun tu Posicion ACTUAL')
    print("PEDIDOS CERCANOS a tu POSICION")
    print ("\t\t", bplustree.retrieve(position))

if __name__ == '__main__':
  main()