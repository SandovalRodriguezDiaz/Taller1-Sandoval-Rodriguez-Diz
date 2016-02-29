import math
import matplotlib.pylab as plt
import numpy as np

class Triangle:

        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = int(sampling * time)


        def generar(self):
            wavearray = []
            datos = 0
            for i in range(0, self.tamano):
                    A = (8 / math.pi**2)

                    for j in range (0, 100):
                        par = j % 2
                        if par:
                            val = (-1**((j-1)/2.0))/float(j)**2
                            value =  val * math.sin((j*math.pi*self.Frecuencia*i)/self.SamplingRate)
                            datos += value
                    frame = datos * A
                    wavearray.append(frame)
            FinalData = np.asarray(wavearray)

            return FinalData


        def leveladjust(self, datos, bits, level):
            peaklevel = max(abs(datos))
            valueLevel = (10**(level/20))*((2**16)/2.0)
            valueAdjust = valueLevel / float(peaklevel)
            datosAjustados = datos * valueAdjust
            return datosAjustados


        def graficar(self, array):
                plt.plot(array, color="green", linewidth=1.0, linestyle="-")
                plt.show()