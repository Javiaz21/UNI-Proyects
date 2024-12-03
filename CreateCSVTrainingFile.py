import serial
import csv

# Set up serial connection
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to match your Arduino's serial port

# Open CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write header to CSV file
    writer.writerow(['Value1', 'Value2', 'Value3', 'Value4'])
    
    # Define the number of iterations
    num_iterations = 10
    
    # Loop for a limited number of iterations
    for _ in range(num_iterations):
        # Read data from Arduino
        data = ser.readline().decode().strip()
        
        # Split the received string into individual values
        values = data.split(',')
        
        # Check if received data has 4 values
        if len(values) == 4:
            # Write values to CSV file
            writer.writerow(values)
            print("Data written to CSV:", values)
        else:
            print("Invalid data received:", data)

# Close serial connection
ser.close()
