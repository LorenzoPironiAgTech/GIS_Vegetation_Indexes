import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show

file_tiff = 'NGRDI_orto.tif'

with rasterio.open(file_tiff) as src:
    print(f'Dimensioni file: {src.height} x {src.width}')
    print(f'Numero di bande: {src.count}')
    print(f'Sistema di riferimento: {src.crs}')

    res_x, res_y = src.res
    print(f'Risoluzione: {res_x:.4f}m x {res_y:.4f}m')

    bounds = src.bounds
    print(f'''Ovest: {bounds.left:.2f}, Est: {bounds.right:.2f}
Sud: {bounds.bottom:.2f}, Nord: {bounds.top:.2f}''')

    fig, ax = plt.subplots(figsize=(10, 8))
    show(src, ax=ax, title='NGRDI_orto.tif')
    plt.xlabel('Est (m)')
    plt.ylabel('Nord (m)')
    plt.grid(True, alpha=0.3)
    plt.show()
