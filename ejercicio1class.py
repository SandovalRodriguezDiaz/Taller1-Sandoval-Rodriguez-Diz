__author__ = 'miguelolivares'

import math
import matplotlib.pylab as plt
import numpy as np


class Seno:

        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = int(sampling * time)

        def generar(self):
            wavearray = []
            for i in range(0, self.tamano):

                    datos = math.sin((2*math.pi*self.Frecuencia*i)/self.SamplingRate)

                    wavearray.append(datos)
            FinalData = np.asarray(wavearray)

            return FinalData


        def leveladjust(self, datos, bits, level):
            peaklevel = max(abs(datos))
            print peaklevel
            valueLevel = (10**(level/20))*((2**16)/2.0)
            valueAdjust = valueLevel / float(peaklevel)
            datosAjustados = datos * valueAdjust
            print max(datosAjustados)
            return datosAjustados


        def graficar(self, array):
                plt.plot(array, color="green", linewidth=1.0, linestyle="-")
                plt.show()


