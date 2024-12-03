import csv
import random

# Function to generate simulated sensor readings
def generate_sensor_readings(num_readings):
    readings = []
    for _ in range(num_readings):
        # Generate 4 random sensor values (between 0 and 1023)
        sensor_values = [random.randint(0, 1023) for _ in range(4)]
        # Calculate x speed based on sensor values (sum of sensor values)
        speed_x = sum(sensor_values) * 0.1  # Adjust multiplier to scale speed
        # Generate random speed in y axis (between -100 and 100)
        speed_y = random.uniform(-100, 100)
        # Append sensor values and speeds to the readings
        readings.append(sensor_values + [speed_x, speed_y])
    return readings

# Number of readings to generate
num_readings = 1000

# Generate simulated sensor readings
sensor_data = generate_sensor_readings(num_readings)

# Write data to CSV file
with open('sensor_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Sensor1', 'Sensor2', 'Sensor3', 'Sensor4', 'Speed_X', 'Speed_Y'])  # Write header
    for reading in sensor_data:
        writer.writerow(reading)
        
print(f"{num_readings} simulated sensor readings written to sensor_data.csv")
