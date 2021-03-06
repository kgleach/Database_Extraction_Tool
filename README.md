# Database_Extraction_Tool


### Outline of Program
The end goal of the project is to create a cohesive and intuitive set of GUIs which can be used to effectively sort through large databases for nuclear structural data and atomic binding data. This will allow for an easy, systematic study of excited nuclear states, atomic mass data, and beta decay transitions.

This program has 3 functions: 
1. Produce plots of nuclear states requested by the user.
2. Produce plots of nuclear states with beta decay data.
3. Produce a mass parabola for a given A value.



### How to run this program:
1. Run the `USE_THIS.py` script.
2. Click on the desired function. 
3. Input appropriate values and select options necessary before hitting the appropriate submit button.
4. Requested plots will appear in the GUI when it reopens, and actual data can be found in the `Outputs/gnuPlot` directory.



### How this program operates:
There are several scripts which interact with each other to produce the plots and outputs requested. When the user runs the `USE_THIS.py` program, a GUI opens asking which subscript the user wishes to run. All three options operate in the same manner, but with different requested inputs and different default values.

Upon selection of a subscript, the program will call `THIS_WORKS.py` with a specific option, which will in turn send this option to `isotopeDataExporting.py`. This script will call one of three GUIs, `GUI.py`, `Beta_GUI.py`, or `Parabola_GUI.py`, which will ask for input specific to the function desired. The `isotopeDataExporting.py` file will then run through the `dataClass.py` file which sorts through all 300 `ensdf.xxx` files and compiles the data into a usable form. The program will also run through `functions.py`, gathering the uncertainty values for each data point. This data is then sent back to `THIS_WORKS.py`.

Depending on the options provided by the user, the `THIS_WORKS.py` file may call `mass_data.py`, which searches through `mass16.txt` and gets atomic mass data with uncertainty, and adds it to the dataset.

Upon completing the dataset, the `THIS_WORKS.py` file calls `isotopeDataExporting.py` again to plot the data. This program then deletes all exterior empty data sets, allowing for cleaner plots, and plots the data in gnuplot with the line thickness being the uncertainty of the state.

Finally, the `THIS_WORKS.py` kills the program before calling it again fresh with terminal commands.



### Improvements/Problems:

- How to handle Theory and Sym inputs


## Version Tracking:

Version history can be found in the Change Log, [here.](http://github.com/ElectroweakGroup/Database_Extraction_Tool/blob/master/Changelog.txt)
>>>>>>> aa85c5c9e79df70089bfc4c3f4991c3f13123973
