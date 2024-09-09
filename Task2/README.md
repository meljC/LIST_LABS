# Task 2

## Description

This project provides a Python script for fetching, analyzing, and processing navigational objects data from the provided API. The script fetches the data in GeoJSON format, processes it using `geopandas`, and saves filtered records into a separate `.geojson` file.

## Features

- Fetches GeoJSON data from the [Plovput API](https://plovput.li-st.net/getObjekti/).
- Counts the total number of navigational safety objects in the dataset.
- Filters the records where the `tip_objekta` is equal to `16`.
- Saves the filtered records to a separate GeoJSON file.

## Requirements

- `requests`
- `geopandas`

The notebook 'visualize.ipynb' loads the downloaded '.geojson' file

