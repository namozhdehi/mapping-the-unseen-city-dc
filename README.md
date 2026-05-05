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
  <li>QGIS 3.44</li>
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
<td>DEM</td>
<td>USGS 3DEP</td>
<td>Elevation surface</td>
</tr>
<tr>
<td>Slope</td>
<td>Derived from DEM</td>
<td>Terrain steepness</td>
</tr>
<tr>
<td>Bike Lanes</td>
<td>OSM / DC Data</td>
<td>Transportation layer</td>
</tr>
<tr>
<td>Output</td>
<td>Model result</td>
<td>Bike-friendly segments</td>
</tr>
</table>

<hr>

<h2>Coordinate System</h2>

<pre>EPSG:26918 — NAD83 / UTM Zone 18N</pre>

<p>This ensures:</p>
<ul>
<li>Units in meters</li>
<li>Accurate slope and distance calculations</li>
</ul>

<hr>

<h1>Part A — QGIS Model Builder Automation</h1>

<p>
<img src="outputs/model_screenshot.png" alt="Model Screenshot" width="100%">
</p>

<h3>Goal</h3>

<p>
Automatically identify bike lane segments located on terrain with slope ≤ 15° using a repeatable workflow.
</p>

<hr>

<h3>Workflow Overview</h3>

<p>This model converts terrain data into a transportation insight through a sequence of spatial operations.</p>

<ul>
<li><b>Slope Raster:</b> Provides terrain steepness</li>
<li><b>Bike Lanes:</b> Target transportation network</li>
<li><b>Buffer:</b> Limits analysis area for performance</li>
<li><b>Raster Clip:</b> Reduces processing load</li>
<li><b>Raster Calculator:</b> Classifies slope ≤ 15°</li>
<li><b>Polygonize:</b> Converts raster to vector</li>
<li><b>Extract:</b> Keeps only suitable terrain</li>
<li><b>Spatial Overlay:</b> Finds bike-friendly segments</li>
</ul>

<hr>

<h1>Part B — Python Print Layout Automation</h1>

<p>
<img src="outputs/final_print_layout.png" alt="Print Layout" width="100%">
</p>

<h3>Goal</h3>

<p>
Automatically generate a clean, professional, print-ready map layout using PyQGIS.
</p>

<hr>

<h3>Layout Design</h3>

<pre>
X: 15 mm
Y: 30 mm
Width: 265 mm
Height: 190 mm
</pre>

<p>This allows the map to cover ~98% of the page.</p>

<hr>

<h3>Layout Elements</h3>

<ul>
<li>Title and subtitle</li>
<li>Large map frame</li>
<li>Legend (bottom-right inside map)</li>
<li>Scale bar (bottom-left inside map)</li>
<li>North arrow (above scale bar)</li>
<li>Data attribution</li>
</ul>

<hr>

<h3>Design Decisions</h3>

<ul>
<li><b>Slope:</b> Used as background with reduced opacity</li>
<li><b>Bike segments:</b> Highlighted as main feature</li>
<li><b>Legend:</b> Simplified for clarity</li>
<li><b>Layout:</b> Clean and print-friendly</li>
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

<p>
This project demonstrates a complete GIS workflow:
</p>

<ul>
<li>Terrain analysis using LiDAR-derived DEM</li>
<li>Spatial filtering using slope threshold</li>
<li>Automation using QGIS Model Builder</li>
<li>Map production using Python</li>
</ul>

<p>
The result is a reproducible pipeline that transforms raw elevation data into a practical, transportation-focused insight.
</p>
