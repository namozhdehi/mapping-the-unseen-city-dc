# Mapping the Unseen City  
## LiDAR-Driven Bike-Friendly Terrain Analysis in Washington, DC

![Final Map](outputs/final_print_layout.png)

---

## Project Overview

Urban mobility is not only about where roads and bike lanes exist. Terrain plays a critical role in how usable and comfortable these routes are. A bike lane on a steep slope may technically exist but may not be practical for many users.

This project uses LiDAR-derived elevation data, slope analysis, QGIS Model Builder, and Python automation to identify **existing bike lane segments that are located on bike-friendly terrain (≤ 15° slope)** in Washington, DC.

The workflow transforms raw terrain data into a decision-ready GIS output using both **model automation (Part A)** and **layout automation (Part B)**.

---

## Final Outputs

### Model (QGIS Graphical Modeler)
![Model Screenshot](outputs/model_screenshot.png)

### Final Print Layout
![Print Layout](outputs/final_print_layout.png)

---

## Tools and Technologies

- QGIS 3.44 (Solothurn)
- QGIS Graphical Modeler
- PyQGIS (Python Console)
- GDAL
- GeoPackage
- USGS 3DEP DEM
- OpenStreetMap / DC Bike Data
- CRS: EPSG:26918 (NAD83 / UTM Zone 18N)

---

## Data Sources

| Dataset | Source | Purpose |
|--------|--------|--------|
| DEM | USGS 3DEP | Elevation surface |
| Slope | Derived from DEM | Terrain steepness |
| Bike Lanes | OSM / DC Data | Transportation layer |
| Output | Model result | Bike-friendly segments |

---

## Coordinate System

All layers were aligned to:


EPSG:26918 — NAD83 / UTM Zone 18N


This ensures:
- Units in meters
- Accurate slope and distance calculations

---

# Part A — QGIS Model Builder Automation

## Goal

Automatically identify **existing bike lane segments located on terrain with slope ≤ 15°** using a repeatable workflow.

---

## Model Workflow

### Step 1 — Slope Raster Input

**Task:** Add raster input `Slope Raster`

**Concept:**  
Slope raster stores terrain steepness in degrees.

**Purpose:**  
Used to classify terrain suitability for biking.

---

### Step 2 — Bike Lane Input

**Task:** Add vector input `Bike Lanes`

**Concept:**  
Vector line layer representing transportation features.

**Purpose:**  
Final output will be filtered bike lane segments.

---

### Step 3 — Buffer Bike Lanes

**Task:**

Distance: 50 meters
Dissolve: Yes


**Concept:**  
Buffer creates an area around features.

**Purpose:**  
Reduces analysis area to improve performance.

---

### Step 4 — Clip Slope Raster

**Task:** Clip raster using bike buffer

**Output:**

slope_clipped_to_bike_area


**Concept:**  
Raster clipping reduces dataset size.

**Purpose:**  
Speeds up raster processing and polygonization.

---

### Step 5 — Raster Calculator

**Expression:**

A <= 15


**Output:**

slope_bike_friendly_15


**Concept:**  
Raster classification converts continuous values to binary.

**Purpose:**  
Defines bike-friendly terrain:
- 1 = suitable
- 0 = not suitable

---

### Step 6 — Polygonize Raster

**Task:** Convert raster to polygons

**Output:**

slope_bike_friendly_15_polygon


**Concept:**  
Raster → vector conversion

**Purpose:**  
Enables spatial comparison with bike lanes

---

### Step 7 — Extract Suitable Terrain

**Condition:**

DN = 1


**Output:**

slope_bike_friendly_15_only


**Concept:**  
Filter attribute values

**Purpose:**  
Keep only bike-friendly terrain polygons

---

### Step 8 — Extract Bike-Friendly Segments

**Task:** Spatial extraction

**Output:**

bike_friendly_segments_15


**Concept:**  
Spatial overlay (intersect)

**Purpose:**  
Identify bike lanes on suitable terrain

---

# Part B — Python Print Layout Automation

## Goal

Automatically generate a **professional map layout** using PyQGIS.

---

## Layout Elements

The automated layout includes:

- Title and subtitle
- Map frame (98% page coverage)
- Legend (bottom-right inside map)
- Scale bar (bottom-left inside map)
- North arrow (above scale bar)
- Data attribution

---

## Map Position

The map frame is positioned as:


X: 15 mm
Y: 30 mm
Width: 265 mm
Height: 190 mm


---

## Layout Design

- Landscape A4 format
- Slope raster used as background
- Bike-friendly segments emphasized as primary layer
- Legend simplified to:


Bike-friendly segments
Slope (≤ 15°)


- Scale bar:

0–4 km


- White background + black border for legend and scale bar

---

## Python Workflow Summary

The script:

1. Loads required layers:
   - slope
   - dem_merged
   - bike_friendly_segments_15

2. Creates layout:

Mapping_the_Unseen_City_Print_Layout


3. Sets page to landscape

4. Adds map with correct extent

5. Applies layer styling:
   - Bike lines: dark green (#006D2C)
   - Slope: semi-transparent

6. Adds layout elements:
   - Title
   - Legend
   - Scale bar
   - North arrow

7. Exports final layout

---

## Cartographic Design Decisions

### Slope Background
Used as contextual terrain layer without overpowering the map.

### Bike-Friendly Segments
Primary focus of the map, styled for visibility.

### Legend
Simplified to only meaningful layers.

### Scale Bar & North Arrow
Placed inside map for compact layout.

---

## Repository Structure


mapping-the-unseen-city-dc/

README.md

qgis/
Bike_Friendly_Terrain_Analysis_Clean.model3
Mapping_the_Unseen_City_DC.qgz

scripts/
Mapping_the_Unseen_City_Print_Layout.py

outputs/
model_screenshot.png
final_print_layout.png
final_map_export.png
final_map_export.pdf


---

## Summary

This project demonstrates a complete GIS workflow:

- Terrain analysis using LiDAR-derived DEM
- Spatial filtering using slope threshold
- Automation using QGIS Model Builder
- Visualization using Python-based layout generation

The result is a reproducible workflow that transforms raw elevation data into actionable transportation insight.
