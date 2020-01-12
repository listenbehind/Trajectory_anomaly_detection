#print(__doc__)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

trajectoriesFile = open("D:\\DataSets\\Pregrado\\Arqueologicos\\dataset.txt", encoding="utf-8")

linex = []
liney = []

for line in trajectoriesFile:
    line = line.split(";")
    #line.remove('\n')

    #print(line.encode("utf-8"))
    if line[0] != 'None' and line[1] != 'None':
        linex.append(line[0])
        liney.append(line[1])

#extracting headers
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

