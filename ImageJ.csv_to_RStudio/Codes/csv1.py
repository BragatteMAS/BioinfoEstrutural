#ref: https://www.youtube.com/watch?v=lXHzCoF18YQ

import csv
import os

# Read .csv
#file = 'ALIHHNTYL_5K_S1.csv'
#with open(file, 'r') as f:
#	csv_reader = csv.reader(f, delimiter=',')
#	next(csv_reader, None)
#	for row in csv_reader:
#		print(row)

#Edit .csv
#with open('testout.csv', 'w', newline='') as f:
#	csv_writer = csv.writer(f, delimiter=',')
#	csv_writer.writerow(['red', '214.586', '253', '49.056'])
#	csv_writer.writerow(['green', '214.338', '253', '49.382'])
#	csv_writer.writerow(['blue', '223.356', '253', '43.390'])

# Combine data
files = os.listdir()
line_count = 0

for file in files:
	print(file)
	if file.endswith ('.csv'):
		with open(file, 'r') as f1:
			csv_reader = csv.reader(f1, delimiter=',')
			with open('testout1.csv', 'a', newline='') as f2:
				csv_writer = csv.writer(f2, delimiter=',')
				if line_count == 0:
					csv_writer.writerow(['filename', 'channel','mean','mode','std.dev.'])
					line_count += 1

				next(csv_reader,None)
				for row in csv_reader:
					data = [file[:-10]] + row
					csv_writer.writerow(data)
		print('file processed')
