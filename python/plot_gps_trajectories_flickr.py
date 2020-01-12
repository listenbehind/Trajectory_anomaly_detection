#print(__doc__)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

readed_file = pd.read_csv(r"C:\Users\gquis\OneDrive\Documents\Proyecto_Flicker\points_trajectory.csv",error_bad_lines=False, encoding="utf-8")

##print(type(readed_file))
##print(readed_file.head())

groups = readed_file.groupby('user_id')

print(groups.first())

#Ploteando (x,y)

for trajectory_id, group in groups:
    group=group.sort_values(['fecha'],ascending=True)

    #print(group['latitud'])
    plt.plot(group['latitud'],group['logitud'],'o--', linewidth=2, markersize=4)
    #plt.show()









#commands with series
'''
series_sizes = groups.size()
print(type(series_sizes))
size_array = series_sizes.sort_values(ascending=True)
print(size_array)
'''

'''
linex.pop(0)
liney.pop(0)

#print(linex)
#print(liney)

#conver list of strings to numbers
linex = list(map(float, linex))
liney = list(map(float, liney))

#Ploteando (x,y)
#plt.plot(linex,liney,'o--', linewidth=2, markersize=8)
plt.plot(linex,liney,'o', linestyle='none', markersize=4)
 

#path = r"C:\\Users\\gquis\\OneDrive\\Documents\\Python projects\\Trajectory_processing\\Trajectory_clustering\\Summarization\\trajectories\\"
#path = path + str(imageID)
#imageID = imageID + 1

#plt.savefig(path)

plt.show()
plt.close()

#print(linex)
#print(liney)
print("TrajectoryList process finished!")

'''

