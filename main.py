import functions #Importo el fichero con las funciones
import gdal
import numpy as np

flow_acc = functions.cargar_raster('flowacc.tif') 
#Llamo desde el fichero 'functions' a mi funcion 'cargar_raster', 
#abro mi raster especifico, con el que quiero trabajar.

#Una Otra forma de hacer lo anterior..

import functions as fn

flow_acc = fn.cargar_raster('flowacc.tif')


#Queremos multiplicar flow_acc por el area del pixel (lado), para calcular 
# el area de contribucion aguas arriba (a)

lado = 5

a = flow_acc * lado**2 #Con dos * es la potencia

##Calculo de la longitud efectiva de curva de nivel (b)

#Tengo que generar una capa (aspect), para el calculo de b

gdal.DEMProcessing('aspect.tif', 'fill_mde.tif', 'aspect') 
#Nombre de archivo de salida, nombre archivo de entrada, calculo que quiero


#Cargo aspect y la paso a radianes
#Puede tirar error de que no tiene nada, entonces hay que reiniciar el nucleo

aspect = fn.cargar_raster('aspect.tif') 
aspect_rad = aspect * np.pi/180

#Calculamos los demas valores para calcular b

aspect_sen = np.sin(aspect_rad)
aspect_cos = np.cos(aspect_rad)

aspect_sen_pos = np.abs (aspect_sen) #Al querer solo valores positivos
aspect_cos_pos = np.abs (aspect_cos)



