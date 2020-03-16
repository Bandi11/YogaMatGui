import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def createDF(csvRoot):
    mattress = pd.read_csv(csvRoot)
    mattress['datetime'] = pd.to_datetime(mattress['ts_server'], unit='s')
    return mattress


def sum_pressure(df, index):
    cells = df.data[index][1:-1].split(', ')
    cells = [ int(x) for x in cells ]
    weight = sum(cells)
    return weight

def plot_pressure(df, index):
    cells = df.data[index][1:-1].split(', ')
    cells = [int(x) for x in cells]
    cells_array = np.array(cells)
    cells_array = np.reshape(cells_array, (22, 13))
    df_cells = pd.DataFrame(cells_array)



    # Choose the colormap
    cmap = 'RdBu_r'


    # Draw the heatmap with the mask and correct aspect ratio
    plt.subplots(figsize=(25, 25))
    plt.tick_params(axis='both', which='major', labelsize=25)
    heatMap = sns.heatmap(df_cells, cmap=cmap, vmax=255.0, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, label="big")
    heatMap.set_title('Frame = ' + str(index) +
                      ',Datetime = ' + str(df.datetime[index]) +
                      ', sum_pressure = ' + str(sum_pressure(df, index)),fontsize=20)

    fig = heatMap.get_figure()
    fig.savefig("pics/HM{index}.svg".format(index=index), bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    mattressDF = createDF("data/mattress_A5.csv")