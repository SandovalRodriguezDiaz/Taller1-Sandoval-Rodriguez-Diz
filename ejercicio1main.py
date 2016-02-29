__author__ = 'miguelolivares'

from ejercicio1class import Seno
from archivar import Archivo
from SquareClass import Square
from TriangleClass import Triangle
from SawtoothClass import Sawtooth
from Audiosystem import Audio


def main():

        print ("Generador de Onda Sinusoidal")
        Frecuenciadesampleo = 44100.0
        MaxBits = 16
        Buffer = 1024

        print ("Ingrese su opcion: ")
        Tono = input("Digite la frecuencia del tono a generar: ")
        Tiempo = input("Ingrese el tiempo de audio en segundos: ")
        Level = input("Ingrese el valor pico de la senal en dBfs: ")
        Nombre = raw_input("Ingrese el nombre del archivo a generar: ")
        FormaDeOnda = input("Seleccione la forma de Onda deseada: 1.Seno 2.Cuadrada 3.Diente de Sierra 4.Triangular  ")


        if (FormaDeOnda == 1):
                onda = Seno(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
        if (FormaDeOnda == 2):
                onda = Square(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
        if (FormaDeOnda == 3):
                onda = Sawtooth(Tono, Frecuenciadesampleo, MaxBits, Tiempo)
        if (FormaDeOnda == 4):
                onda = Triangle(Tono, Frecuenciadesampleo, MaxBits, Tiempo)

        datos = onda.generar()
        datosAjustados = onda.leveladjust(datos,MaxBits,Level)
        archivo = Archivo(Frecuenciadesampleo, MaxBits, Nombre)
        archivo.archivar(datosAjustados)

        Seleccion = raw_input("Desea reproducir el audio generado(si/no): ")

        if Seleccion == "si":
            audio = Audio(Buffer)
            Datos = audio.abrir(Nombre)
            audio.inicio(Datos[0],Datos[1],Datos[2])
            audio.reproducir(Datos[3])
            audio.cerrar()


if __name__ == "__main__":
    main()
