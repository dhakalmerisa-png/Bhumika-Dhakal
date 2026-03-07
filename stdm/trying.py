import csv
with open('student.csv', 'w',newline='') as csvfile:
    w = csv.writer(csvfile)
    w.writerow(['Name','Age','Grade'])
    w.writerow(['Bhumi',20,'A'])
    w.writerow(['Merisa',22,'B'])    