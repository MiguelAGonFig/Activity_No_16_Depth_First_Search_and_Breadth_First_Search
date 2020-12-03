from particula import Particula
import json

class Admin_particulas:
    def __init__(self):
        self.__particulas = []

    def sort(self, atrib):
        if atrib == 1:
            self.__particulas.sort(key=lambda particula: particula.id)
        elif atrib == 2:
            self.__particulas.sort(key=lambda particula: particula.distancia, reverse=True)
        else:
            self.__particulas.sort(key=lambda particula: particula.velocidad)

    def agregar_final(self, part:Particula):
        self.__particulas.append(part)

    def agregar_inicio(self, part:Particula):
        self.__particulas.insert(0, part)
    
    def consultar(self):
        for part in self.__particulas:
            print(part)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )

    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0       

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0