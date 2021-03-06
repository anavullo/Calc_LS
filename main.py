import functions #Importo el fichero con las funciones
import gdal
import numpy as np
import rasterio

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

#Calculo final de b

b = 5 + (aspect_sen_pos + aspect_cos_pos)

##Calculo de Ae, area especifica de captacion
a_e = a / b


##Calculo de la pendiente en grados

gdal.DEMProcessing('splope.tif', 'fill_mde.tif', 'slope')
#Como me volvio a generar un tif sin nada, reinicie el nucleo poniendo 'exit' en la terminal

#Pasamos a radianes

slope = fn.cargar_raster('splope.tif')
slope_rad = slope * np.pi/180
slope_sen = np.sin (slope_rad)


##Con todo calculado, generamos LS, que es nuestro objetivo
m = 0.4
n = 1

ls = (m + 1) * (a_e / 22.13) ** m * (slope_sen / 0.896) ** n     


##Importamos LS como raster
 
mde = rasterio.open('fill_mde.tif')
profile = mde.profile #Me quedo con las configuraciones de fill_mde
 
 #Abriendo un fichero para escribir con ese perfil

capa_ls =  rasterio.open('capa_ls.tif', 'w', **profile) 
#Nombre de archivo de salida, configuro para que pueda editar el fichero,
#Tengo que especificarle un monton de cosas, ancho, alto, etc. Por eso, pongo
#el **profile, que lo que hace es copiarme esas caracteristicas y ponerlas
#a mi nuevo raster de salida.
 
#Como me volvio a generar un tif sin nada, reinicie el nucleo poniendo 'exit' en la terminal
 
capa_ls.write(ls, 1)
capa_ls.close()
