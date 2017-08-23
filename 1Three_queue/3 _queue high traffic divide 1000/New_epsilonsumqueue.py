#Draw new graphs that removes MaxSize_Pri11_22 and MaxSize_PriMinWt
import csv
import matplotlib.pyplot as plt
import read

VLIST = [[1/2, 0, 1/2, 1/2]]
#a list of lists whose elements are the values of v in the order of v11, v22, v12, v21
#PLIST = ["MaxWt", "MaxSize_random", "MaxSize_Pri11_22", "MaxSize_PriMaxWt", "MaxSize_PriMinWt"]
PLIST = ["MaxWt", "Pri_E", "MaxSize_PriMaxWt"]
# a list of selection policies


def main(args):
    for Vs in VLIST:
        f = VLIST.index(Vs)
        plt.figure(f + 1)
        subfigure = read.readData(str(Vs) + '.csv')[1]
        stylelist = ['solid', 'dashed', 'dashdot']
        for i in range(len(PLIST)):
            plt.plot(subfigure[0], subfigure[i+1],
                    label = PLIST[i], linewidth = 4 if i == 0 else 2,
                    linestyle = stylelist[i], markersize = 12 )
        y = [float(S)**2/2 for S in subfigure[0]]
        plt.plot(subfigure[0], y,
                label = "Universal lower bound", linewidth = 3,
                linestyle = 'dotted', markersize = 12 )
        plt.xlabel('Traffic Intensity')
        plt.ylabel(r'$(1-2\lambda) E[\sum_{i,j} Q_{i,j}]$')
        plt.title(r'$(1-2\lambda) E[\sum_{i,j} Q_{i,j}]$ vs Traffic Intensity')
                #+ str(VLIST[f]))
        plt.grid(True)
        plt.legend()
        plt.savefig("EpsilonXAvgq_Vs " + str(VLIST[f]) + ".png")
        plt.savefig("EpsilonXAvgq_Vs " + str(VLIST[f]) + ".eps")
        plt.savefig("EpsilonXAvgq_Vs " + str(VLIST[f]) + ".svg")
        plt.show()

if __name__ == "__main__":
    import sys
    main(sys.argv)