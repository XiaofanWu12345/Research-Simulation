#Draw new graphs that removes MaxSize_Pri11_22 and MaxSize_PriMinWt
import csv
import matplotlib.pyplot as plt
import read

VLIST = [[1/2, 1/2, 1/2, 1/2]]
#a list of lists whose elements are the values of v in the order of v11, v22, v12, v21
#PLIST = ["MaxWt", "MaxSize_random", "MaxSize_Pri11_22", "MaxSize_PriMaxWt", "MaxSize_PriMinWt"]
PLIST = ["MaxWt", "MaxSize_random", "MaxSize_PriMaxWt", "MaxSize_PriMaxWtLog"]
LABELS = ["MaxWeight", "MaxSize", "MSMW", "MSMWLog"]
# a list of selection policies


def main(args):
    for Vs in VLIST:
        f = VLIST.index(Vs)
        plt.figure(f + 1)
        subfigure = read.readData(str(Vs) + '.csv')[1]
        stylelist = ['solid', 'dashed', 'dashdot', 'dotted']
        markerlist = ['.',',','o','^']
        for i in range(len(PLIST)):
            plt.rc('text', usetex=True)
            plt.rc('font', family='serif')
            plt.plot(subfigure[0], subfigure[i+1],
                    label = LABELS[i], linewidth = 4 if i == 0 else 2,
                    linestyle = stylelist[i], marker = markerlist[i], markersize = 5 )
        y = [float(S)**2/2 for S in subfigure[0]]
        plt.plot(subfigure[0], y,
                label = "Universal lower bound", linewidth = 3,
                linestyle = 'dotted', markersize = 5 )
        plt.xlabel(r'\text{Traffic Intensity }'
                   r'$(\rho)$',
                   fontsize=16)
        plt.ylabel(r'$(1-\rho) E\left[\sum_{i,j} Q_{i,j}\right]$', fontsize=16)
        plt.title(r'$(1-\rho)E\left[\sum_{i,j} Q_{i,j}\right]$'
                  r' \text{ vs Traffic Intensity}',
                  fontsize=16)
                        #+ str(VLIST[f]))
        plt.subplots_adjust(left=0.12, right=0.97, top=0.9, bottom=0.1)
        plt.grid(True)
        plt.legend(fontsize=16)
        plt.savefig("EpsilonXAvgq_Vs " + str(VLIST[f]) + ".png")
        #plt.savefig("EpsilonXAvgq_Vs " + str(VLIST[f]) + ".eps")
        #plt.savefig("EpsilonXAvgq_Vs " + str(VLIST[f]) + ".svg")
        plt.show()

if __name__ == "__main__":
    import sys
    main(sys.argv)