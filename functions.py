import rasterio

#Armamos la funcion para cargar cualquier raster
def cargar_raster(nombre_raster): 
    raster = rasterio.open(nombre_raster) #Abrimos el fichero tif
    banda = raster.read(1) #Elegimos la banda con la que queremos trabajar
    
    return banda
