from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np
import json


app = Flask(__name__)

# Define efficiency factors for different types of solar panels
efficiency_factors = {
    'Monocrystalline Panels': 0.24,
    'PERC (Passive Emitter and Rear Cell) Panels': 0.21,
    'Polycrystalline Panels': 0.17,
    'Thin Film Panels': 0.13
}

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

# Efficiency calculation function with solar panel type as input
def calculate_efficiency(solar_power, clear_sky_power, efficiency_factor):
    # Calculate efficiency considering the efficiency factor
    return (solar_power / clear_sky_power) * 100 * efficiency_factor


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator')
def local_page():
    return render_template('calculator.html')

@app.route('/calculate_efficiency', methods=['POST'])
def calculate_efficiency2():
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude']) 
    
    # Specify the path to the folder containing all CSV files
    data_folder_path = r"C:\Users\Swapnil\Pictures\Swapnil\KJ Somaiya TY\MIni Project (Sem-6)\FINAL\Test data"

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

    # Calculate optimal tilt angle
    optimal_tilt_angle = calculate_optimal_tilt_angle(latitude, combined_filtered_df['Temperature'].mean())
    
   # Calculate monthly average efficiency for each panel type
    monthly_avg_efficiency = {}
    for panel_type, efficiency_factor in efficiency_factors.items():
        # Calculate efficiency for the current panel type
        efficiency = calculate_efficiency(combined_filtered_df['Corrected Solar Power'], combined_filtered_df['Clear Sky Power'], efficiency_factor)
        # Aggregate data by month and calculate average efficiency for each month
        monthly_avg_efficiency[panel_type] = efficiency.groupby(combined_filtered_df['Datetime'].dt.month).mean().to_dict()

    optimal_tilt_angle_rounded = round(optimal_tilt_angle, 2)
    return render_template('result.html', panel_tilt=optimal_tilt_angle_rounded ,monthly_avg_efficiency=monthly_avg_efficiency)

if __name__ == '__main__':
    app.run(debug=True)
