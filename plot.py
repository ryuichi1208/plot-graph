#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy
import os
import pandas
import sys


def plot_graph(x=None, y=None):
    df = pandas.read_csv("./data/data01.csv", encoding="utf-8", header=0, index_col='time')
    plt.style.use('bmh')
    df.plot()
    plt.title("access/hour")
    plt.xlabel("time")
    plt.ylabel("access")
    plt.savefig("tmp_humid.png")
    plt.show()

def main():
    plot_graph(x="x", y="y")

if __name__ == "__main__":
    main()
