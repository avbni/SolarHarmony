import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# Path to the directory containing shapefiles
shapefile_path = 'C:/Users/Swapnil/Pictures/Swapnil/KJ Somaiya TY/MIni Project (Sem-6)/Indian-solar-panel-placement/Data/Shapefiles'

# Create a new map figure
plt.figure(figsize=(10, 8))
ax = plt.axes(projection=ccrs.PlateCarree())

# Add coastlines from shapefile
ax.add_feature(ccrs.cartopy.feature.COASTLINE, edgecolor='black')

# Add country borders from shapefile
ax.add_feature(ccrs.cartopy.feature.BORDERS, linestyle=':', edgecolor='black')

# Plot your data on the map (e.g., scatter plot, etc.)

# Show the plot
plt.show()
