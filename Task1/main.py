import rasterio
import numpy as np

# Load the satellite image
# Read the bands needed for NDVI and NDMI
with rasterio.open('../data/response_bands.tiff') as src:
    band_4 = src.read(4)  # Red band 
    band_8 = src.read(8)  # Near-Infrared (NIR) band 
    band_11 = src.read(11)  # Shortwave Infrared (SWIR) band 

    # Number of bands for the image
    band_count = src.count
    print(f"The satellite image contains {band_count} bands.")

# Calculate NDVI
# NDVI = (NIR - Red) / (NIR + Red)
ndvi = (band_8.astype(float) - band_4.astype(float)) / (band_8 + band_4 + 1e-10)
# The small value 1e-10 is added to avoid division by zero

# Calculate NDMI
# NDMI = (NIR - SWIR) / (NIR + SWIR)
ndmi = (band_8.astype(float) - band_11.astype(float)) / (band_8 + band_11 + 1e-10)

# Scale Pixel values
# scale_factor = 10000

# Calculate NDVI and NDMI and scale the result by the scale factor
# ndvi = ((band_8.astype(float) - band_4.astype(float)) / (band_8 + band_4 + 1e-10)) * scale_factor
# ndmi = ((band_8.astype(float) - band_11.astype(float)) / (band_8 + band_11 + 1e-10)) * scale_factor


# Save NDVI and NDMI as GeoTIFF files
ndvi_output = 'ndvi_output.tiff'
ndmi_output = 'ndmi_output.tiff'

# Define the metadata for the output files (keep the same as input)
with rasterio.open('../data/response_bands.tiff') as src:
    meta = src.meta
    meta.update(dtype=rasterio.float32, count=1)

# Save NDVI
with rasterio.open(ndvi_output, 'w', **meta) as dst:
    dst.write(ndvi.astype(rasterio.float32), 1)

# Save NDMI
with rasterio.open(ndmi_output, 'w', **meta) as dst:
    dst.write(ndmi.astype(rasterio.float32), 1)

print(f"NDVI saved to {ndvi_output}")
print(f"NDMI saved to {ndmi_output}")

# Calculate average NDVI and NDMI for the entire image
mean_ndvi = np.nanmean(ndvi)  # Use nanmean to avoid NaN values from invalid operations
mean_ndmi = np.nanmean(ndmi)

print(f"Average NDVI: {mean_ndvi}")
print(f"Average NDMI: {mean_ndmi}")
