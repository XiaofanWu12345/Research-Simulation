import csv
# Read dat from csv files
def readData(filename):
    with open(filename, 'r') as out:
        csvout = csv.reader(out)
        csvoutlist = list(csvout)
        subfigure_sumqueue = [csvoutlist[i][2:] for i in [0,1,3,5,11]] #,7,9
        subfigure_epsilonqueue = [csvoutlist[i][2:] for i in [0,2,4,6,12]] #,8,10
    return [subfigure_sumqueue, subfigure_epsilonqueue]

