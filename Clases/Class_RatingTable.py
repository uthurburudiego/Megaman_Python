import pygame
import json
from Clases.Class_Label import Label
from Clases.utilidades import cargar_imagen


class RankingTable:
    def __init__(self, screen, json_file):
        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.json_file = json_file
        self.data = self.load_data()  # Carga los datos desde el archivo JSON

        # Crea una lista de Labels para mostrar los nombres y puntajes de los jugadores
        self.labels = []

        x, y = 100, 100  # Posición inicial de los Labels
        for player in self.data:
            margen = 300
            name = player['nombre']
            score = player['puntaje']
            label_text = f"{name}: {score}"
            label = Label(self.width // 2 - 150, self.height // 2 - margen,
                          cargar_imagen("Recursos\Img\Menu\label.png", 288, 84), self.fuente, self.screen, f"{label_text}")  # Crea un Label para cada jugador
            self.labels.append(label)
            margen += 90  # Ajusta la posición vertical para el siguiente jugador

    def load_data(self):
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"El archivo {self.json_file} no se encontró.")
            return []

    def draw(self):
        for label in self.labels:
            label.draw()
