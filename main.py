import functions #Importo el fichero con las funciones

flow_acc = functions.cargar_raster('flowacc.tif') 
#Llamo desde el fichero 'functions' a mi funcion 'cargar_raster', 
#abro mi raster especifico, con el que quiero trabajar.

#Una Otra forma de hacer lo anterior..

import functions as fn

flow_acc = fn.cargar_raster('flowacc.tif')



