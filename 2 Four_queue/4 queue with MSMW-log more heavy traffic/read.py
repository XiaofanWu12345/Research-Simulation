import csv
# Read dat from csv files
def readData(filename):
    with open(filename, 'r') as out:
        csvout = csv.reader(out)
        csvoutlist = [line for line in csvout]
        subfigure_sumqueue = [csvoutlist[i][2:] for i in [0,1,3,5,7]]
        subfigure_epsilonqueue = [csvoutlist[i][2:] for i in [0,2,4,6,8]]
    return [subfigure_sumqueue, subfigure_epsilonqueue]

