#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     10/02/2020
# Copyright:   (c) Admin 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import os


def main(folder, remove):
    arcpy.env.workspace = folder
    filelist = []

    # Create a list of all files ending with the chosen extension
    for item in os.listdir(folder):
        if item.endswith(remove):
            filelist.append(item)
        else:
            pass

    # Remove the extension if a copy doesn't exist.
    for item in filelist:
        all_removed = os.path.splitext(item)[0]
        exists = os.path.isfile(folder + "/" + all_removed)

        # remove the extension
        if exists == False:
            newname = os.path.splitext(item)[0]
            arcpy.Rename_management(item, newname)
            arcpy.AddMessage("Renamed " + str(item) + " as " + str(newname))

        # prompt that a copy already exists
        elif exists == True:
            arcpy.AddMessage(str(item) + " already exists ...")

        else:
            pass


if __name__ == '__main__':
    # Get the parameters needed form the arc toolbox
    folder = arcpy.GetParameterAsText(0) # Folder with files to be altered
    remove = arcpy.GetParameterAsText(1) # String of extension to remove
    main(folder, remove)


