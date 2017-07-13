# Add Tag to Feature Class

Add Tag to Feature Class is a script tool that runs in ArcMap or ArcCatalog (versions 10.1+). It adds a string of text, or "tag", to the beginning of a feature class (it will not work on other data types such as shapefiles or coverages).


## Using the Tool
- Add the toolbox, `Rename Files.tbx`, to your ArcToolbox in ArcCatalog or ArcMap
- Go into the properties of the "Add Tag to Feature Class" script tool and in the Source tab set the path to the `Add_Tag_to_File.py` file provided in this repo

If the tag entered into the tool is `Jan2014` and the feature class entered is `Land_Use`, then the tool will rename the feature class to `Jan2014_Land_Use`.

**********
**WARNING:**
The tool changes the actual feature class' name, and DOES NOT copy out the feature class to a new location. Please make a backup of your data before running this tool, or ANY tool on your data.
**********

## Walkthrough Video:
You can open the video walkthrough ([Add_Tag_to_Feat_Class_Tool_WALKTHROUGH.swf](Add_Tag_to_Feat_Class_Tool_WALKTHROUGH.swf)) with any browser. "Open with" your Chrome, Firefox, etc. browser. The walkthrough video contains no audio.

--------------------------------
## `Batch...` for multiple Feature Class renaming

The most useful feature of this tool is that you can also run this tool as a Batch process just by right clicking > `Batch...` on the tool once you've added it in ArcToolbox.

This enables you to rename whole datasets at a time rather than one file at a time.
Use the `Batch...` `Fill` function by right clicking on certain columns to fill columns with info that is the same for multiple rows.  

For example, If you want to add "Jan2014" to the beginning of an entire dataset of feature classes:
- create the correct number of entries in the Batch tool
- select all and drag & drop the feature classes into the correct column
- drag & drop the dataset location into the correct column
- right click > `Fill` (once you've unhighlighted the row(s))
- Enter the tag you want to add in the first row, and `Fill` the Tag column.
-----------------------------------
last updated 2017-07-12 RiggsC
