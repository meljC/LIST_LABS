# Task 1

## Description

The main.py script loads a satellite image (Sentinel-2 L2A), calculates certain indices, and displays parameters. The image is in the /data folder (response_bands.tiff).
 
1. calculates the NDVI (Normalized Difference Vegetation Index)
2. calculates the NDMI (Normalized Difference Moisture Index)
3. Saves the NDVI and NDMI as separate .tiff (or .geotiff) files 
4. Calculates the average value of NDVI and NDMI for the entire image and display the result 
5. Displays the number of bands for the image 

## Requirements:

. 'rasterio' 
- 'NumPy'