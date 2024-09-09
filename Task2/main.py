import requests
import geopandas as gpd

# Fetch the data from the API
url = "https://plovput.li-st.net/getObjekti/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Load the GeoJSON data into a GeoDataFrame
    geojson_data = response.json()
    gdf = gpd.GeoDataFrame.from_features(geojson_data)

else:
    print(f"Failed to fetch data from the API. Status code: {response.status_code}")
    exit()

# If needed: Reorder the columns to place 'geometry' last
# cols = [col for col in gdf.columns if col != 'geometry'] + ['geometry']
# gdf = gdf[cols]

# Set CRS in GeoDataFrame 
crs_name = geojson_data['crs']['properties']['name']
gdf.set_crs(crs_name, inplace=True)
# gdf.set_crs("EPSG:4326", inplace=True)

# Display total number of records
total_records = len(gdf)
print(f"Total number of records: {total_records}")

# Filter records where 'tip_objekta' is 16
filtered_gdf = gdf[gdf['tip_objekta'] == 16]
filtered_count = len(filtered_gdf)
print(f"Number of records with 'tip_objekta' = 16: {filtered_count}")

# Save the filtered records to a GeoJSON file
filtered_geojson_path = "filtered_data_from_api.geojson"
filtered_gdf.to_file(filtered_geojson_path, driver="GeoJSON")
print(f"Filtered records saved to {filtered_geojson_path}")
