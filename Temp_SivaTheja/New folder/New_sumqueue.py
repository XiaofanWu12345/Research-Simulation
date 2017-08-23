#Draw new graphs that removes MaxSize_Pri11_22 and MaxSize_PriMinWt
import csv
import matplotlib.pyplot as plt

VLIST = [[1/2, 1/2, 1/2, 1/2]]
#a list of lists whose elements are the values of v in the order of v11, v22, v12, v21
#PLIST = ["MaxWt", "MaxSize_random", "MaxSize_Pri11_22", "MaxSize_PriMaxWt", "MaxSize_PriMinWt"]
PLIST = ["MaxWt", "MaxSize_random", "MaxSize_PriMaxWt"]
# a list of selection policies


def main(args):
    for Vs in VLIST:
        f = VLIST.index(Vs)
        plt.figure(f + 1)
        with open(str(Vs) + '.csv', 'r') as out:
            csvout = csv.reader(out)
            csvoutlist = [line for line in csvout]
            subfigure = [csvoutlist[i][2:] for i in [0,1,2,3]] # a list of lists who are the 1rst, 3rd, 5th line of the file
        for i in range(len(PLIST)):
            if (1): #Eliminate the two policies
                plt.plot(subfigure[0], subfigure[i+1],
                        label = PLIST[i], linewidth = 4 if i == 0 else 2,
                        markersize = 12 )
        plt.xlabel('Traffic Intensity')
        plt.ylabel(r'$ E\left[\sum_{i,j} Q_{i,j}\right]$')
        plt.title(r'$ E\left[\sum_{i,j} Q_{i,j}\right]$ vs Traffic Intensity')
                #+ str(VLIST[f]))
        plt.grid(True)
        plt.legend()
        plt.savefig("Remove2ps_Avgq_Vs " + str(VLIST[f]) + ".png")
        plt.savefig("Remove2ps_Avgq_Vs " + str(VLIST[f]) + ".eps")
        plt.savefig("Remove2ps_Avgq_Vs " + str(VLIST[f]) + ".svg")
        plt.show()

if __name__ == "__main__":
    import sys
    main(sys.argv)