import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def ts_deviceDataGen(mattressDF,freq=1):
    """used for ts_device generation"""
    i = 0
    value = []
    for i in range(0, len(mattressDF)):
        new_v = i*(1/freq) + np.random.randn()*0.05-0.025
        # used for generating random bad values
        # if np.random.randn()>0.5:
        #     new_v = 6666666666
        value.append(new_v*1000)
        i += 1
    mattressDF["ts_device"] = value


def createDF(csvRoot):
    mattress = pd.read_csv(csvRoot)
    #not in use, used for generating test dataset
    #mattress = mattress.head(10)
    mattress['datetime'] = pd.to_datetime(mattress['ts_server'], unit='s')

    #populating "ts_device"
    #ts_deviceDataGen(mattress, 2)
    #mattress.to_csv("data/mattress_A5_10elementShortErrors.csv",index=False)
    return mattress


def sum_pressure(df, index):
    cells = df.data[index][1:-1].split(', ')
    cells = [ int(x) for x in cells ]
    weight = sum(cells)
    return weight

def plot_pressure(df, index):
    if index is not None:
        cells = df.data[index][1:-1].split(', ')
        cells = [int(x) for x in cells]
        cells_array = np.array(cells)
        cells_array = np.reshape(cells_array, (22, 13))
        df_cells = pd.DataFrame(cells_array)



    # Choose the colormap
    cmap = 'RdBu_r'


    # Draw the heatmap with the mask and correct aspect ratio
    plt.subplots(figsize=(10,12))
    plt.tick_params(axis='both', which='major', labelsize=11)
    heatMap = sns.heatmap(df_cells, cmap=cmap, vmax=255.0, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, label="big")
    heatMap.set_title('Frame = ' + str(index) +
                      ',Datetime = ' + str(df.datetime[index]) +
                      ', sum_pressure = ' + str(sum_pressure(df, index)),fontsize=11)

    fig = heatMap.get_figure()
    fig.savefig("pics/HM{index}.svg".format(index=index), bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    mattressDF = createDF("data/mattress_A5.csv")