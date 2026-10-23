# GIS Vegetation Indexes & Remote Sensing Pipeline (Satellite & Drone)

A geospatial computing and remote sensing repository focused on processing multi-source raster datasets (ESA Sentinel-2 and UAV/Drone photogrammetry) to extract, analyze, and map vegetation indices. 

This toolkit demonstrates how to couple Python spatial libraries (`rasterio`, `numpy`) with environmental domain expertise to automate crop health metrics, pixel-level surface classifications, and flight data analytics.

## 🛠️ Tech Stack & Spatial Libraries
* **Python 3**
* **Rasterio** (Geospatial raster I/O, Coordinate Reference Systems management, and metadata extraction)
* **NumPy** (Array masking, vectorization, and statistical operations on pixel matrices)
* **Matplotlib** (Automated spatial layout rendering and grid generation)
* **QGIS** (Visual verification and map design)

## 🚀 Key Engineering & Analytics Features

### 1. UAV / Drone Photogrammetry Processing & Inspection
* **NGRDI Index Extraction:** Processes high-resolution orthomosaics generated via "home-grown" drone surveys using a **DJI Mini 4K**. Calculates the *Normalized Green Red Difference Index* (NGRDI) to assess canopy coverage using RGB spectral bands.
* **Spatial Metadata Parsing:** Dynamically extracts raster dimensions, band counts, exact spatial resolution scaling (meters per pixel), and spatial bounding boxes (West/East/South/North coordinates) directly from GeoTIFF headers.

### 2. High-Throughput Satellite Pixel Analytics (Sentinel-2)
* **Robust Masking Pipeline:** Filters out `NoData` tags, handles floating-point `NaN` system anomalies, and clamps values strictly within the physical NDVI boundaries (`-1.0` to `1.0`) using NumPy boolean masking.
* **Automated Canopy Classification:** Runs vectorized calculations over satellite matrices (e.g., a 10m resolution Sentinel-2 scene of a viticultural zone) to dynamically output Mean, Max, and Min NDVI metrics.
* **Zonal Vegetated Area Calculation:** Automatically computes the exact percentage of active vegetation surface based on a hardcoded agronomical threshold (`NDVI > 0.3`).
