from qgis.core import (
    QgsProject, QgsPrintLayout, QgsLayoutItemMap, QgsLayoutItemLabel,
    QgsLayoutItemLegend, QgsLayoutItemScaleBar, QgsLayoutItemPicture,
    QgsLayoutItemPage, QgsLayoutPoint, QgsLayoutSize, QgsUnitTypes,
    QgsApplication, QgsLayoutMeasurement, QgsRectangle
)
from qgis.PyQt.QtGui import QFont, QColor
from qgis.PyQt.QtCore import Qt

project = QgsProject.instance()

layers_bike = project.mapLayersByName("bike_friendly_segments_15")
layers_slope = project.mapLayersByName("slope")
layers_dem = project.mapLayersByName("dem_merged")

bike_layer = layers_bike[0] if layers_bike else None
slope_layer = layers_slope[0] if layers_slope else None
dem_layer = layers_dem[0] if layers_dem else None


if not (bike_layer and slope_layer and dem_layer):
    print("\n✗ ERROR: Missing required layers")
else:
    print("\n" + "=" * 60)
    print("CREATING PRINT LAYOUT")
    print("=" * 60)
    
    manager = project.layoutManager()
    layout_name = "Mapping_the_Unseen_City_Print_Layout"
    
    old_layout = manager.layoutByName(layout_name)
    if old_layout:
        manager.removeLayout(old_layout)
    
    layout = QgsPrintLayout(project)
    layout.initializeDefaults()
    layout.setName(layout_name)
    manager.addLayout(layout)
    
    page = layout.pageCollection().pages()[0]
    page.setPageSize("A4", QgsLayoutItemPage.Orientation.Landscape)

    # Title - X=10mm, Y=8mm, W=280mm, H=10mm
    title = QgsLayoutItemLabel(layout)
    title.setText("Mapping the Unseen City: Bike-Friendly Terrain in Washington, DC")
    title.setFont(QFont("Arial", 16, QFont.Bold))
    title.setHAlign(Qt.AlignmentFlag.AlignHCenter)
    title.setBackgroundEnabled(False)
    title.setFrameEnabled(False)
    title.attemptMove(QgsLayoutPoint(10, 8, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    title.attemptResize(QgsLayoutSize(280, 10, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    layout.addLayoutItem(title)

    # Subtitle - X=110mm, Y=15mm, W=67mm, H=4mm, font size 12
    subtitle = QgsLayoutItemLabel(layout)
    subtitle.setText("Slope threshold: ≤ 15°")
    subtitle.setFont(QFont("Arial", 12))
    subtitle.setHAlign(Qt.AlignmentFlag.AlignHCenter)
    subtitle.setBackgroundEnabled(False)
    subtitle.setFrameEnabled(False)
    subtitle.attemptMove(QgsLayoutPoint(110, 15, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    subtitle.attemptResize(QgsLayoutSize(67, 4, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    layout.addLayoutItem(subtitle)

    # Map - X=9mm, Y=25mm, W=280mm, H=175mm
    map_item = QgsLayoutItemMap(layout)
    map_item.attemptMove(QgsLayoutPoint(9, 25, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    map_item.attemptResize(QgsLayoutSize(280, 175, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    layout.addLayoutItem(map_item)
    map_item.setLayers([bike_layer, slope_layer, dem_layer])
    
    # Set exact extent: X min=315000, Y min=4300862, X max=337000, Y max=4315037
    extent = QgsRectangle(315000, 4300862, 337000, 4315037)
    map_item.setExtent(extent)
    
    map_item.setFrameEnabled(True)
    map_item.setFrameStrokeWidth(QgsLayoutMeasurement(0.5, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    map_item.setFrameStrokeColor(QColor(0, 0, 0))
    map_item.refresh()

    # North arrow - X=15mm, Y=160mm, W=15mm, H=15mm
    north = QgsLayoutItemPicture(layout)
    north_svg = ""
    for path in QgsApplication.svgPaths():
        candidate = path + "/arrows/NorthArrow_04.svg"
        import os
        if os.path.exists(candidate):
            north_svg = candidate
            break
    if north_svg:
        north.setPicturePath(north_svg)
    north.setBackgroundEnabled(False)
    north.setFrameEnabled(False)
    north.attemptMove(QgsLayoutPoint(15, 160, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    north.attemptResize(QgsLayoutSize(15, 15, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    layout.addLayoutItem(north)

    # Scale bar - X=15mm, Y=180mm, W=70mm, H=13mm
    scale_bar = QgsLayoutItemScaleBar(layout)
    scale_bar.setStyle("Line Ticks Up")
    scale_bar.setLinkedMap(map_item)
    scale_bar.setUnits(QgsUnitTypes.DistanceUnit.DistanceKilometers)
    scale_bar.setUnitsPerSegment(1)
    scale_bar.setNumberOfSegments(4)
    scale_bar.setNumberOfSegmentsLeft(0)
    scale_bar.setUnitLabel("km")
    scale_bar.setBackgroundEnabled(True)
    scale_bar.setBackgroundColor(QColor(255, 255, 255, 200))
    scale_bar.setFrameEnabled(True)
    scale_bar.setFrameStrokeColor(QColor(0, 0, 0))
    scale_bar.setFrameStrokeWidth(QgsLayoutMeasurement(0.3, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    scale_bar.attemptMove(QgsLayoutPoint(15, 180, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    scale_bar.attemptResize(QgsLayoutSize(70, 13, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    scale_bar.update()
    layout.addLayoutItem(scale_bar)

    # Legend - X=220mm, Y=150mm, W=61mm, H=43mm 
    legend = QgsLayoutItemLegend(layout)
    legend.setTitle("Legend")
    legend.setLinkedMap(map_item)
    legend.setAutoUpdateModel(False)
    
    # Clear root and build legend from scratch
    root = legend.model().rootGroup()
    root.clear()
    
    # Add ONLY bike and slope layers 
    root.addLayer(bike_layer)
    root.addLayer(slope_layer)
    
    # Set custom legend names using the custom property method
    for child in root.children():
        layer_name = child.name()
        if layer_name == "bike_friendly_segments_15":
            child.setCustomProperty("legend/title-label", "Bike-friendly segments")
        elif layer_name == "slope":
            child.setCustomProperty("legend/title-label", "Slope (≤ 15°)")
    
    # Style the legend box
    legend.setBackgroundEnabled(True)
    legend.setBackgroundColor(QColor(255, 255, 255))
    legend.setFrameEnabled(True)
    legend.setFrameStrokeColor(QColor(0, 0, 0))
    legend.setFrameStrokeWidth(QgsLayoutMeasurement(0.5, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    
    # Position and size
    legend.attemptMove(QgsLayoutPoint(220, 150, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    legend.attemptResize(QgsLayoutSize(61, 43, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    
    layout.addLayoutItem(legend)
    print(f"✓ Legend created with custom names")

    # Footer - X=10mm, Y=205mm, W=280mm, H=7mm
    footer = QgsLayoutItemLabel(layout)
    footer.setText("Data: USGS 3DEP DEM, OpenStreetMap/DC bike lanes | CRS: EPSG:26918 NAD83 / UTM Zone 18N")
    footer.setFont(QFont("Arial", 8))
    footer.setHAlign(Qt.AlignmentFlag.AlignCenter)
    footer.setBackgroundEnabled(False)
    footer.setFrameEnabled(False)
    footer.attemptMove(QgsLayoutPoint(10, 205, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    footer.attemptResize(QgsLayoutSize(280, 7, QgsUnitTypes.LayoutUnit.LayoutMillimeters))
    layout.addLayoutItem(footer)

    layout.refresh()
    
    print("✓ SUCCESS")
