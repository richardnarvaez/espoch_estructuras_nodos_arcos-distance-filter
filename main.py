'''
    Autor: Richard Vinueza 6745
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
    # Instanciando el Arbol y asignando el orden
    bplustree = BPlusTree(order=5)

    # Ingresando Pedidos ESTATICOS
    print('\nInsertando pedido 1 |  Cargando...')
    bplustree.insert('-1.658005$-78.672889', 'Casa 1')
    bplustree.show()

    print('\nInsertando pedido 2 |  Cargando...')
    bplustree.insert('-1.663581$-78.660529', 'Departamento')
    bplustree.show()

    print('\nInsertando pedido 3 |  Cargando...')
    bplustree.insert('-1.660150$-78.680936', 'Puerta Principal')
    bplustree.show()

    print('\nInsertando pedido 4 |  Cargando...')
    bplustree.insert('-1.660150$-78.690936', 'Casa Blanca')
    bplustree.show()
    
    print('\nInsertando pedido 4 |  Cargando...')
    bplustree.insert('-1.660150$-78.690936', 'Casa Blanca 1')
    bplustree.show()
    print('\nInsertando pedido 4 |  Cargando...')
    bplustree.insert('-1.660150$-78.690936', 'Casa Blanca 2')
    bplustree.show()

    print('\nInsertando pedido 5 |  Cargando...')
    bplustree.insert('-1.660150$-78.689936', 'Edificio 2')
    bplustree.show()
    print('\n--------------------------------------')
    print('|--------  App Rider Activa  --------|')
    print('--------------------------------------')
    print("\nRecomendado: -1.660150$-78.690937")
    position = input("Ingresa tu posicion:")
    system('clear')

    print('\nEstos son los pedios que puedes recojer segun tu Posicion ACTUAL')
    print("\n🔴  PEDIDOS CERCANOS")
    print ("\t\t 🏠 ", bplustree.search(position))

if __name__ == '__main__':
  main()