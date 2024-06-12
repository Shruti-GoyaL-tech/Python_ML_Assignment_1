import csv

# Open the CSV file
with open('C:/Users/Shruti/Desktop/Python ML Internship/demo.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        print(row)
