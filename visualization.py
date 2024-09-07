from astropy.io import fits
import matplotlib.pyplot as plt
import pandas

def show_image():
    #Mostra a imagem do HDU na posição x
    x = 2 #Apenas um exemplo
    hdulist = fits.open('Maps/HERSCHEL/anonymous1725578900/hpacs1342220557_20hpppmapb_00_1469433805960.fits')
    image_data = hdulist[x].data
    plt.imshow(image_data, cmap='gray')
    plt.colorbar()
    plt.show()
    return None

def show_data_frame():
    x = 9 #Apenas um exemplo
    #Imprime um data_frame com informações da posição x da consulta
    hdulist = fits.open('Maps/HERSCHEL/anonymous1725578900/hpacs1342220557_20hpppmapb_00_1469433805960.fits')
    table_data = hdulist[x].data
    data_frame = pandas.DataFrame(table_data)
    print(data_frame.head())
    return None