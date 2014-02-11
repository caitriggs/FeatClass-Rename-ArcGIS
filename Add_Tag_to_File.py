"""
Description: Rename fileGDB feature class by adding a text tag to beginning of feature class name.
created by Caitlin Riggs, last updated 2014-02-11

"""

# Import system modules
import arcpy, os
from arcpy import env

# Get user's workspace geodatabase
arcpy.env.workspace = arcpy.GetParameterAsText(0)

# Set local variables for Rename_management
in_data =  arcpy.GetParameterAsText(1)
tag = arcpy.GetParameterAsText(2)

# Get base file name without extension: me.shp -> me
in_data = os.path.splitext(os.path.basename(in_data))[0]

# Add tag to beginning of base file name
out_data = tag + "_" + in_data

# Execute Rename
arcpy.Rename_management(in_data, out_data)

# End Message
arcpy.AddMessage("**  " + os.path.basename(in_data) + " renamed to " + os.path.basename(out_data) + "  **")
