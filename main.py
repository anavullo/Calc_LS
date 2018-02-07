import functions #Importo el fichero con las funciones
import gdal

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

gdal.DEMProcessing('aspect.tf', 'fill_mde.tif', 'aspect') 
#Nombre de archivo de salida, nombre archivo de entrada, calculo que quiero





