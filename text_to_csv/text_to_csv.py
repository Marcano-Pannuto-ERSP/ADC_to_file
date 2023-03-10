import csv
import sys

def get_temp_data(line):
    temp = line.split("<")[1]
    temp = temp.split(">")[0]
    return temp

def text_to_csv():
    origFile = sys.argv[1]		# name of file that we are going to convert to csv file
    f1 = open(origFile, "r")		# open for reading

    # open csv file for writing - should be a new file
    newFile = sys.argv[2]
    f2 = open(newFile, "w", newline = '')
    
    # parse the lines from the original file and write them to csv file
    writer = csv.writer(f2)
    # for now just write the original lines
    writer.writerow(["temperature"])	#csv header
    for line in f1:
        temp_data = get_temp_data(line)
        writer.writerow([temp_data])

text_to_csv()
