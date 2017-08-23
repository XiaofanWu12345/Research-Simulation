#Draw new graphs that removes MaxSize_Pri11_22 and MaxSize_PriMinWt
import csv
import matplotlib.pyplot as plt

VLIST = [[1/2, 1/2, 1/2, 1/2], [3/4, 3/4, 1/4, 1/4], [0.6, 0.6, 0.4, 0.4]]
#a list of lists whose elements are the values of v in the order of v11, v22, v12, v21
PLIST = ["MaxWt", "MaxSize_random", "MaxSize_Pri11_22", "MaxSize_PriMaxWt", "MaxSize_PriMinWt", "MaxArrival_PriMaxWt"]
# a list of selection policies


def main(args):
    for Vs in VLIST:
        f = VLIST.index(Vs)
        plt.figure(f + 1)
        with open(str(Vs) + '.csv', 'r') as out:
            csvout = csv.reader(out)
            csvoutlist = [line for line in csvout]
            subfigure = [csvoutlist[i][2:] for i in range(0, len(csvoutlist), 2)] # a list of lists who are the 1rst, 3rd, 5th line of the file
        for i in range(len(PLIST)):
            if (i != PLIST.index("MaxSize_Pri11_22")) and (i != PLIST.index("MaxSize_PriMinWt")): #Eliminate the two policies
                plt.plot(subfigure[0], subfigure[i+1],
                        label = PLIST[i], linewidth = 4 if i == 0 else 2,
                        markersize = 12 )
        plt.xlabel('Traffic Intnesity')
        plt.ylabel('Epsilon Times Average Total Queue Length -- (1 - S) * E[Q11 + Q22 + Q12 + Q21]')
        plt.title('(1 - S) * E[Q11 + Q22 + Q12 + Q21] vs Traffic Intensity, Vs Value: '
                + str(VLIST[f]))
        plt.grid(True)
        plt.legend()
        plt.savefig("Remove2ps_EpsilonXAvgq_Vs " + str(VLIST[f]) + ".png")
        plt.savefig("Remove2ps_EpsilonXAvgq_Vs " + str(VLIST[f]) + ".eps")
        plt.savefig("Remove2ps_EpsilonXAvgq_Vs " + str(VLIST[f]) + ".svg")
        plt.show()

if __name__ == "__main__":
    import sys
    main(sys.argv)