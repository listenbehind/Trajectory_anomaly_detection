#print(__doc__)
import numpy as np
import matplotlib.pyplot as plt
import glob # to list files on a directory

from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from PIL import Image, ExifTags # to read metadata on jpg files

'''
    Function to convert to other format
    13°23'30.8"S 72°02'56.3"W
    -13.391878, -72.048984
'''
def change_gps_format(grade, min_, sec, hemisphere):
    
    sec = sec / 60
    min_ = min_ + sec
    min_ = min_ / 60
    grade = grade + min_

    hemisphere = hemisphere.lower()
    if hemisphere == 'n' or hemisphere == 's':
        if hemisphere == 's':
            return grade * -1
        else:
            return grade * 1

    elif hemisphere == 'e' or hemisphere == 'w':
        if hemisphere == 'w':
            return grade * -1
        else:
            return grade * 1
    else:
        # Bad hemisphere data
        return -1


path = r'C:\Users\Gerar\OneDrive\Documents\Proyecto_Flicker\primeros scripts2019-12-25\'

files = [f for f in glob.glob(path + "**/*.jpg")]

# Filename to append
write_filename = "gps_photos_data.txt"

# The 'a' flag tells Python to keep the file contents
# and append (add line) at the end of the file.
myfile = open(write_filename, 'w')

for file_name in files:
    # To read metada from .png files
    img = Image.open(file_name)

    # Need to validate this line in order to avoid jpg files without GPS info
    metadata = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }

    print(metadata)
    # According to metada format .jpg file
    if 'GPSInfo' in metadata:  # Not all jpg files have GPSInfo
        # finding name file
        idx = file_name.rfind('\\') + 1
        file_proper_name = file_name[idx:]

        # 2: ((13, 1), (23, 1), (30896, 1000))
        latitude = metadata['GPSInfo'][2]
        lat_hemisphere = metadata['GPSInfo'][1]
        lat_grade = latitude[0][0]/latitude[0][1]
        lat_min =   latitude[1][0]/latitude[1][1]
        lat_sec =   latitude[2][0]/latitude[2][1]

        # 4: ((72, 1), (2, 1), (56496, 1000))
        longitude = metadata['GPSInfo'][4]
        lon_hemisphere = metadata['GPSInfo'][3]
        lon_grade = longitude[0][0]/longitude[0][1]
        lon_min =   longitude[1][0]/longitude[1][1]
        lon_sec =   longitude[2][0]/longitude[2][1]

        latitude = change_gps_format(lat_grade, lat_min, lat_sec, lat_hemisphere)
        longitude = change_gps_format(lon_grade, lon_min, lon_sec, lon_hemisphere)

        print(
            metadata['DateTime'], 
            latitude, 
            longitude,
            file_proper_name
            )

        # Add the line
        myfile.write(
            ''.join([
                str(metadata['DateTime']),' ',
                str(latitude), ' ',
                str(longitude),' ',
                str(file_proper_name),
            ])
        )
        myfile.write('\n')


# Close the file
myfile.close()

print("The code finished .. !!")

