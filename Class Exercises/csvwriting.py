# csvwriting.py
# Import module
import csv
import math

# Create file
csvfile = open('csvexample.csv', 'w')

# Create csvwriter
csvwriter = csv.writer(csvfile, delimited=',')

# Write information
csvwriter.writerow(['a', 'b', 'hypoteneuse'])
for a in range(1, 101):
    for  b in range(1,101):
        hypoteneuse = math.sqrt(a ** 2 + b ** 2)
        csvwriter.writerow([a,b, hypoteneuse])
        
# Close file
csvfile.close()