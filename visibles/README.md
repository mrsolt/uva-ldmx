# LDMX Visibles

Instructions for running the visible A' decay simulations starting from dark brem LHE files to produce root files in the ldmx-sw format.

## Instructions for Creating LHE files

Run the following command on dark brem files to produce both decay and brem LHE files:

```bash
python3 ap_LHE_parser.py <options>
```

This will produce three files in the <output directory> to be used in the next step:
output file base name_brem.lhe (brem file)
output file base name_decay.lhe (decay file)
output file base name_decay.dat (data file)

options:
-h = print help
-l = input LHE file
-o = output directory
-n = output files base name
-e = epsilon (default 1e-5)
-m = A prime mass in GeV (default 0.050 GeV)
-y = minimum z value for decay in mm (default 0 mm)
-z = maximum z value for decay in mm (default 7000 mm)
-u = uniform decay (default False)

##Instructions for Creating A' Files

Source the ldmx environment.

```bash
source ldmx-sw/scripts/ldmx-env.sh
```

Run the following command.

```bash
ldmx fire ap_producer.py <run number> <dark brem file> <ap decay file> <output file> <max events>
```

where the <dark brem file> and <ap decay file> come from the previous step. This will create a root <output file> in the standard ldmx-sw format. You will have to set the maximum number of events to a value at or below the number of events in the LHE files, or it will crash.

This process takes a lot of time. If you are running a batch job, you should set the time to at least 8 hours.

##Running Visible Simulation on UVA Rivanna

Example slurm files for running the above two steps on the Rivanna batch system are in the batch directory. Note the location of the input files and output files including the log file.
