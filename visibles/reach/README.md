# LDMX Reach Calculations

Reach contours for LMDX for the minimal dark photon can be constructed with some given assumptions. These assumptions are configurable in the params.py file and the parameters are explained in the file (To Do: explain these better). To select either a subdetector system or the entire detector, change the corresponding parameter (Ecal/Hcal/Combined) to True in the file. If you only want a CSV file with $\epsilon^2$ instead of $\epsilon$ (to input into ldmx_reach.py only), set plotoutput to False and eps2 to True. In order to produce a reach contour, you must have all the .py files in this directory. Then, run the following command.

```bash
python3 uva-ldmx/visibles/reach/reach.py <params.py file>
```

where the default params.py file in this directory is used if no file is specified. There are two output files (which can be turned on and off) - 
a pdf file of basic plots and a csv file with the mass and $\epsilon$ values of the contour.

The output csv files from above can be used to compare several contours. Be sure to use CSV files that contain $\epsilon$, not $\epsilon^2$, if you plan to use the -e flag (below). To compare the contours of interest and output a pdf image, run the following 
command with the desired inputs.

```bash
python3 uva-ldmx/visibles/reach/plotcontours.py <csv file 1> <csv file 2> ... <csv file n> <label 1> <label 2> ... <label n>
```

where options are -t for the title (default none), -e to use $\epsilon^2$ (default $\epsilon$), and -o for output file base name (default 'plot').
