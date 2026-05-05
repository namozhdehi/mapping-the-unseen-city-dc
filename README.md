# Mapping the Unseen City  
## LiDAR-Driven Bike-Friendly Terrain Analysis in Washington, DC

![Final Print Layout](outputs/final_print_layout.png)

## Project Overview

Urban mobility is not only about where roads, sidewalks, and bike lanes exist. Terrain also affects how comfortable, safe, and accessible a route feels. A bike lane may look useful on a flat map, but LiDAR-derived elevation data can reveal hidden terrain challenges such as steep slopes and difficult elevation changes.

This project uses QGIS, a LiDAR-derived DEM, slope analysis, QGIS Graphical Modeler, and Python print layout automation to identify existing bike lane segments in Washington, DC that are located on terrain with slope less than or equal to 15 degrees.

The goal is to turn raw elevation and transportation data into a decision-ready GIS output that can support urban mobility planning, bike infrastructure review, and portfolio-level geospatial analysis.

---

## Final Result

The final output highlights bike-friendly bike lane segments over a terrain/slope background.

Key output:

- Bike-friendly segments identified from existing bike lane data
- Slope-based suitability threshold: slope ≤ 15°
- Automated QGIS model for repeatable analysis
- Python-generated print layout with title, legend, scale bar, north arrow, and attribution

---

## Tools and Technologies

- QGIS 3.44.7 Solothurn
- QGIS Graphical Modeler
- QGIS Python Console / PyQGIS
- GDAL
- GeoPackage
- USGS 3DEP DEM
- OpenStreetMap / DC bike lane data
- EPSG:26918 NAD83 / UTM Zone 18N

---

## Data Sources

| Dataset | Source | Purpose |
|---|---|---|
| DEM | USGS 3DEP | LiDAR-derived elevation surface |
| Slope Raster | Generated from DEM in QGIS | Measures terrain steepness |
| Bike Lanes | OpenStreetMap / DC bike lane data | Transportation features analyzed |
| Final Bike-Friendly Segments | Model output | Bike lanes located on suitable terrain |

---

## Coordinate Reference System

All analysis layers were aligned to:

```text
EPSG:26918 - NAD83 / UTM Zone 18N
