<h1>Mapping the Unseen City</h1>
<h2>LiDAR-Driven Bike-Friendly Terrain Analysis in Washington, DC</h2>

<p>
  <img src="outputs/final_print_layout.png" alt="Final Map" width="100%">
</p>

<hr>

<h2>Project Overview</h2>

<p>
Urban mobility is not only about where roads and bike lanes exist. Terrain plays a critical role in how usable and comfortable these routes are. A bike lane may technically exist on a map, but steep slopes can make it difficult or impractical for many users.
</p>

<p>
In this project, I used LiDAR-derived elevation data, slope analysis, QGIS Model Builder, and Python automation to identify <b>existing bike lane segments located on bike-friendly terrain (≤ 15° slope)</b> in Washington, DC.
</p>

<p>
The workflow transforms raw elevation data into a clear, decision-ready GIS output by combining:
</p>

<ul>
  <li>Automated spatial analysis (Part A)</li>
  <li>Automated map production (Part B)</li>
</ul>

<hr>

<h2>Tools and Technologies</h2>

<ul>
  <li>QGIS 3.44 (Solothurn)</li>
  <li>QGIS Graphical Modeler</li>
  <li>PyQGIS (Python Console)</li>
  <li>GDAL</li>
  <li>GeoPackage</li>
  <li>USGS 3DEP DEM</li>
  <li>OpenStreetMap / DC Bike Data</li>
  <li>CRS: EPSG:26918 (NAD83 / UTM Zone 18N)</li>
</ul>

<hr>

<h2>Data Sources</h2>

<table border="1" cellpadding="6">
<tr>
<th>Dataset</th>
<th>Source</th>
<th>Purpose</th>
</tr>
<tr>
<td>DEM (LiDAR-derived)</td>
<td>
<a href="https://www.usgs.gov/3d-elevation-program" target="_blank">
USGS 3DEP (3D Elevation Program)
</a>
</td>
<td>Elevation surface</td>
</tr>
<tr>
<td>Slope Raster</td>
<td>Derived from DEM in QGIS</td>
<td>Terrain steepness</td>
</tr>
<tr>
<td>Bike Lanes</td>
<td>
<a href="https://www.openstreetmap.org" target="_blank">
OpenStreetMap
</a>
</td>
<td>Transportation layer</td>
</tr>
<tr>
<td>Output</td>
<td>Model result</td>
<td>Bike-friendly segments</td>
</tr>
</table>

<p><b>Note:</b> DEM and slope raster files are not included due to large size. Download them from the links above.</p>

<hr>

<h2>Coordinate System</h2>

<pre>EPSG:26918 — NAD83 / UTM Zone 18N</pre>

<ul>
<li>Meter-based units</li>
<li>Accurate slope + distance analysis</li>
</ul>

<hr>

<h1>Part A — QGIS Model Builder Automation</h1>

<p>
<img src="outputs/model_screenshot.png" alt="Model Screenshot" width="100%">
</p>

<h3>Goal</h3>

<p>
Automatically identify bike lane segments located on terrain ≤ 15° using a scalable and optimized workflow.
</p>

<hr>

<h3>Workflow Steps</h3>

<h4>Step 1 — Add Slope Raster</h4>
<ul>
<li>Input: slope raster</li>
<li>Concept: raster stores terrain steepness per pixel</li>
<li>Purpose: foundation for terrain suitability analysis</li>
</ul>

<h4>Step 2 — Add Bike Lanes</h4>
<ul>
<li>Input: bike_utm (line layer)</li>
<li>Purpose: target features for analysis</li>
</ul>

<h4>Step 3 — Buffer Bike Lanes (Performance Optimization)</h4>
<ul>
<li>Distance: 50 meters</li>
<li>Dissolve: Yes</li>
<li>Purpose: limit analysis area → major speed improvement</li>
</ul>

<h4>Step 4 — Clip Slope Raster</h4>
<ul>
<li>Output: slope_clipped_to_bike_area</li>
<li>Purpose: reduce raster size and processing time</li>
</ul>

<h4>Step 5 — Raster Calculator</h4>
<pre>A <= 15</pre>
<ul>
<li>Output: slope_bike_friendly_15</li>
<li>Purpose: classify terrain into bike-friendly vs not</li>
</ul>

<h4>Step 6 — Polygonize Raster</h4>
<ul>
<li>Output: slope_bike_friendly_15_polygon</li>
<li>Purpose: convert raster → vector for overlay</li>
</ul>

<h4>Step 7 — Extract DN = 1</h4>
<ul>
<li>Output: slope_bike_friendly_15_only</li>
<li>Purpose: keep only suitable terrain</li>
</ul>

<h4>Step 8 — Extract by Location</h4>
<ul>
<li>Output: bike_friendly_segments_15</li>
<li>Purpose: final bike-friendly segments</li>
</ul>

<hr>

<h3>Key Improvements (Important)</h3>

<ul>
<li>Used <b>buffer + raster clipping</b> to reduce processing time drastically</li>
<li>Avoided processing full DEM (critical for performance)</li>
<li>Ensured CRS consistency (EPSG:26918)</li>
<li>Converted raster to vector for proper spatial overlay</li>
</ul>

<hr>

<h1>Part B — Python Print Layout Automation</h1>

<p>
<img src="outputs/final_print_layout.png" alt="Print Layout" width="100%">
</p>

<h3>Goal</h3>

<p>
Automatically generate a clean, professional, print-ready map using PyQGIS.
</p>

<hr>

<h3>Workflow Steps</h3>

<h4>Step 1 — Load Layers</h4>
<ul>
<li>slope</li>
<li>dem_merged</li>
<li>bike_friendly_segments_15</li>
</ul>

<h4>Step 2 — Create Layout</h4>
<ul>
<li>Name: Mapping_the_Unseen_City_Print_Layout</li>
<li>Page: A4 Landscape</li>
</ul>

<h4>Step 3 — Add Map</h4>
<pre>
X: 15 mm
Y: 30 mm
Width: 265 mm
Height: 190 mm
</pre>

<ul>
<li>Covers ~98% of page</li>
<li>Uses current map canvas extent</li>
</ul>

<h4>Step 4 — Apply Styling</h4>
<ul>
<li>Bike segments: dark green (#006D2C)</li>
<li>Slope: semi-transparent</li>
<li>DEM: background context</li>
</ul>

<h4>Step 5 — Add Legend</h4>
<ul>
<li>Position: bottom-right inside map</li>
<li>White background + black border</li>
<li>Only 2 items:</li>
<ul>
<li>Bike-friendly segments</li>
<li>Slope (≤ 15°)</li>
</ul>
</ul>

<h4>Step 6 — Add Scale Bar</h4>
<ul>
<li>Position: bottom-left inside map</li>
<li>0–4 km</li>
<li>White background + black frame</li>
</ul>

<h4>Step 7 — Add North Arrow</h4>
<ul>
<li>Position: above scale bar</li>
<li>No background</li>
</ul>

<hr>

<h3>Key Improvements (Important)</h3>

<ul>
<li>Ensured map fits inside page (no overflow)</li>
<li>Placed all elements INSIDE map for compact layout</li>
<li>Cleaned legend (removed unnecessary layers)</li>
<li>Added consistent styling and hierarchy</li>
<li>Removed clutter (notes, extra text)</li>
</ul>

<hr>

<h2>Repository Structure</h2>

<pre>
mapping-the-unseen-city-dc/

├── <a href="./README.md">README.md</a>

├── qgis/
│   ├── <a href="./qgis/Bike_Friendly_Terrain_Analysis_Clean.model3">Bike_Friendly_Terrain_Analysis_Clean.model3</a>
│   └── <a href="./qgis/Mapping_the_Unseen_City_DC.qgz">Mapping_the_Unseen_City_DC.qgz</a>

├── scripts/
│   └── <a href="./scripts/Mapping_the_Unseen_City_Print_Layout.py">Mapping_the_Unseen_City_Print_Layout.py</a>

├── outputs/
│   ├── <a href="./outputs/model_screenshot.png">model_screenshot.png</a>
│   ├── <a href="./outputs/final_print_layout.png">final_print_layout.png</a>
│   ├── <a href="./outputs/final_map_export.png">final_map_export.png</a>
│   └── <a href="./outputs/final_map_export.pdf">final_map_export.pdf</a>
</pre>

<hr>

<h2>Summary</h2>

<ul>
<li>End-to-end GIS workflow</li>
<li>Terrain + transportation integration</li>
<li>Performance optimization</li>
<li>Automation (Model + Python)</li>
</ul>

<p>
This project demonstrates how raw elevation data can be transformed into actionable transportation insight using automated GIS workflows.
</p>
