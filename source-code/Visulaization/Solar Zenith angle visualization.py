import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/Swapnil/Pictures/Swapnil/KJ Somaiya TY/MIni Project (Sem-6)/Indian-solar-panel-placement/Data/Test data/3057510_19.37_72.58_2017.csv')

# Combine date and time columns into a single datetime column
df['Datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])

# Plot DNI over time
plt.figure(figsize=(10, 6))
plt.plot(df['Datetime'], df['Solar Zenith Angle'], color='red', linewidth=1)
plt.title('Solar Zenith Angle Over Time')
plt.xlabel('Datetime')
plt.ylabel('Solar Zenith Angle')
plt.grid(True)
plt.tight_layout()
plt.show()