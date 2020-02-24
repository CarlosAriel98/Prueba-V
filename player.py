#-*- Coding: utf8-*-
#programa: player..py
#objetivo clase que simula el comportamiento de un reproductor
#Autor: Carlos Ariel Molina
#Fecha: 02/10/2020
import sys
import os
import platform


class Player:
    """
    se encarga de las funcionalidades del reproductor
    reporduce, pausa y detiene la reporduccion de archivos 
    de audio:
    """

    def __init__(self):
        """ Inicializa una lista de reproduccion"""
        self.playlist = list()
        #diccionarios
        #objetos que almacena las informacion en pares (claves y valor)
        self.option = {"1": self.add_song,
                       "2": self.play,
                       "3": self.search_song,
                       "4": self.delete_song,
                       "5": self.close}


        def menu(self):
            """ Despliega el menu princial """
            self.limpiar_patalla()
        print("""
               Reproductor musica
               
               1. Agregar cancion a la lista de reproduccion
               2. Reproducir
               3. Buscar una cancion a la lista de reproduccion
               4. Eliminar una cancion en la lista de reproduccion
               5. Salir
               """)

        def presione_enter(self):
            """ Realiza una pausa y solicita presionar una teclar """
            input("\nPrecione Enter para continuar")


        def limpiar_patalla(self):
            """
            Verificar mediante la libreria platform el sistema del usuario y limpia 
            la pantalla depediendo del SO utilisado
            """
            if platform.system() == "Windos":
                os.system("cls")
            elif platform.system() == "Darwin" or platform.os == "Linux":
                os.system("clear")
            else:
                print("Plataforma no soportada")
        
        def add_song(self):
            """ Agrega una nueva cancion a la lista de reproduccion"""2
            print("\n=== Agregar nuevas caciones a la lista de reproduccion")
            print("Las canciones deben seguir el siguiente formato")
            print("nombrecancion + . + extencion ejemoplo: Cancion.mp3 ")
            self.playlist.append(
                 input("Ingrese el nombre de la cancion: "))
            self.presione_enter()
            