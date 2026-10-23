import numpy as np

with rasterio.open("NDVI_prataporci_Res_10m.tif") as src:
    ndvi = src.read(1)  # Legge la prima banda come array NumPy
    nodata = src.nodata

# Maschera e pulizia dei dati
mask = (ndvi != nodata) & (~np.isnan(ndvi)) & (ndvi >= -1.0) & (ndvi <= 1.0)
ndvi_clean = ndvi[mask]

# Calcoli
if ndvi_clean.size > 0:
    pct_veg = (np.sum(ndvi_clean > 0.3) / ndvi_clean.size) * 100
    print(f"NDVI medio: {np.mean(ndvi_clean):.2f}")
    print(f"NDVI max: {np.max(ndvi_clean):.2f}")
    print(f"NDVI min: {np.min(ndvi_clean):.2f}")
    print(f"Superficie vegetata (NDVI > 0.3): {pct_veg:.1f}%")
