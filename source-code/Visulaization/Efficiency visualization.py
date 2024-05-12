import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def calculate_solar_power(DNI, DHI, GHI, solar_zenith_angle):
    """
    Calculate solar power incident on the solar panel.
    """
    return DNI * np.cos(np.radians(solar_zenith_angle)) + DHI + GHI

def calculate_clear_sky_power(clearsky_DNI, clearsky_DHI, clearsky_GHI):
    """
    Calculate clear sky solar power incident on the solar panel.
    """
    return clearsky_DNI + clearsky_DHI + clearsky_GHI

def temperature_correction(solar_power, temperature):
    """
    Correct solar power based on temperature.
    """
    # This is a simple correction formula, you may need to use a different formula
    # based on the specifications of your solar panels.
    return solar_power * (1 - 0.005 * (temperature - 25))

def calculate_optimal_tilt_angle(latitude, temperature):
    """
    Calculate optimal tilt angle for solar panels based on latitude and temperature.
    """
    # Empirical formula for optimal tilt angle
    tilt_angle = latitude * 0.87 + temperature * 0.03 - 14.3
    
    # Ensure the tilt angle is within a reasonable range (0 to 90 degrees)
    tilt_angle = max(0, min(tilt_angle, 90))
    
    return tilt_angle

def calculate_efficiency(solar_power, clear_sky_power):
    """
    Calculate solar panel efficiency.
    """
    return (solar_power / clear_sky_power) * 100

# Specify the path to the folder containing all CSV files
data_folder_path = r"C:\Users\Swapnil\Pictures\Swapnil\KJ Somaiya TY\MIni Project (Sem-6)\Indian-solar-panel-placement\Data\Test data"

# Prompt user for latitude and longitude inputs
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))

# Create an empty list to store efficiency plots for each year
yearly_plots = []

# Create an empty DataFrame to store combined filtered data
combined_filtered_df = pd.DataFrame()

# Loop through each CSV file in the folder
for file in os.listdir(data_folder_path):
    if file.endswith(".csv"):
        filepath = os.path.join(data_folder_path, file)
        df = pd.read_csv(filepath)
        # Filter data based on latitude and longitude
        filtered_df = df[(df['Latitude'] == latitude) & (df['Longitude'] == longitude)]
        if not filtered_df.empty:
            # Print the filename of the selected dataset
            print(f"Selected dataset for latitude {latitude}, longitude {longitude}: {file}")
            # Print the filtered dataset itself
            #print(filtered_df)
            # Concatenate filtered data to combined DataFrame
            combined_filtered_df = pd.concat([combined_filtered_df, filtered_df])

# Create a datetime column
combined_filtered_df['Datetime'] = pd.to_datetime(combined_filtered_df[['Year', 'Month', 'Day', 'Hour', 'Minute']])

# Calculate solar power incident on the solar panel
combined_filtered_df['Solar Power'] = calculate_solar_power(combined_filtered_df['DNI'], combined_filtered_df['DHI'], combined_filtered_df['GHI'], combined_filtered_df['Solar Zenith Angle'])

# Calculate clear sky solar power incident on the solar panel
combined_filtered_df['Clear Sky Power'] = calculate_clear_sky_power(combined_filtered_df['Clearsky DNI'], combined_filtered_df['Clearsky DHI'], combined_filtered_df['Clearsky GHI'])

# Correct solar power based on temperature
combined_filtered_df['Corrected Solar Power'] = temperature_correction(combined_filtered_df['Solar Power'], combined_filtered_df['Temperature'])

# Calculate solar panel efficiency
combined_filtered_df['Efficiency'] = calculate_efficiency(combined_filtered_df['Corrected Solar Power'], combined_filtered_df['Clear Sky Power'])

#Calculate average efficiency
combined_avg_efficiency = combined_filtered_df['Efficiency'].mean()

# Calculate optimal tilt angle
optimal_tilt_angle = calculate_optimal_tilt_angle(latitude, combined_filtered_df['Temperature'].mean())

# Print combined average efficiency
plt.axhline(y=combined_avg_efficiency, color='red', linestyle='--', label=f'Average Efficiency: {combined_avg_efficiency:.2f}%')


# Plotting efficiency over time
plt.plot(combined_filtered_df['Datetime'], combined_filtered_df['Efficiency'], label='Combined Efficiency', color='blue', linewidth=1)

# Add title and labels
plt.title(f'Solar Panel Efficiency Over Time for Latitude {latitude}, Longitude {longitude}')
plt.xlabel('Datetime')
plt.ylabel('Efficiency (%)')
plt.grid(True)
plt.legend()

# Add optimal tilt angle annotation
plt.text(0.01, 0.99, f'Optimal Solar Panel Tilt Angle: {optimal_tilt_angle:.2f} degrees',
         transform=plt.gca().transAxes, fontsize=10, color="green", verticalalignment='top')

# Show the plot
plt.show()
