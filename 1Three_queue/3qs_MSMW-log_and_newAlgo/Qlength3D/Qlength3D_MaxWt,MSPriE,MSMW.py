#Queue length Scatter Plot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import read
import csv

VLIST = [[1/2, 0, 1/2, 1/2]]
PLIST = ["MaxWt", "Pri_E", "MaxSize_PriMaxWt"]
LABELS = ["MaxWeight", "MSC", "MSMW"]

def main(args):
    for Vs in VLIST:
        f = VLIST.index(Vs)
        fig = plt.figure(f + 1)
        xyzs = read.readData(str(Vs) + '.csv')[0][1:]
        ax = fig.add_subplot(111, projection='3d')
        xs = [float(num) for num in xyzs[0]]
        ys = [float(num) for num in xyzs[1]]
        zs = [float(num) for num in xyzs[2]]
        ax.scatter(xs, ys, zs, c='b', marker='o')
        ax.set_xlabel(LABELS[0])
        ax.set_ylabel(LABELS[1])
        ax.set_zlabel(LABELS[2])
        plt.grid(True)
        plt.legend(fontsize=16)
        fig.savefig("Queue Lengths 3D " + str(VLIST[f]) + ".png")
        plt.show()

if __name__ == "__main__":
    import sys
    main(sys.argv)