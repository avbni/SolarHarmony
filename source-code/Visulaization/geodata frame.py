import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile
shapefile_path = r"C:\Users\Swapnil\Pictures\Swapnil\KJ Somaiya TY\MIni Project (Sem-6)\Indian-solar-panel-placement\Data\Map"
gdf = gpd.read_file(shapefile_path)

# Plot the shapefile
fig, ax = plt.subplots()
gdf.plot(ax=ax, color='blue')

# Function to handle mouse click event
def onclick(event):
    print(f'Clicked at ({event.xdata:.2f}, {event.ydata:.2f})')

# Connect the mouse click event to the figure
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Show the plot
plt.title('Click on a point to get its coordinates')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()