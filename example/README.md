# Running A General Example Script

This analysis

Copy the following files to ldmx-analysis:
cp python/HcalAnalyzer.py ldmx-analysis/python/
cp src/HcalAnalyzer.cxx ldmx-analysis/src/Analysis/
cp include/HcalAnalyzer.h ldmx-analysis/include/Analysis/

TODO: put these files in the main ldmx-analysis branch so that they don't need to be copied.

See instructions on how to build ldmx-sw and ldmx-analysis.


# Using the Config Files
The following config files shoot 10,000 neutrons at 1 GeV at the front face of the HCal. You can run the script by doing the following:

```bash
ldmx fire config/neutrons.py <run number> neutron.root
```

Note the run number sets the seed, so when running multiple jobs the run number needs to be different for each job submission (see below). Next, run the analysis.

```bash
ldmx fire config/HcalAna.py neutron_analysis.root neutron.root
```

# Using the Batch Scripts
These scripts submit jobs to the slurm batch system on Rivanna using the config files from config directory in the examples directory. You will have to change the  $LDMX_UVA, $NEUTRON_DIR, $ANALYSIS_DIR scripts to 
They submit 100 jobs of 10,000 events each.

```bash
sbatch --array=0-99 neutrons.slurm
```

The ```${SLURM_ARRAY_TASK_ID}``` passes each integer from the specified array (0 through 99 inclusively in this case). This set a different run number (and hence, a different seed) for each job submission.

To run analysis scripts on the output files you just created, do the following.

```bash
sbatch --array=0-99 analysis_neutron.slurm
```

You can use the root function hadd to combine these output files into a single file.


# HCal Neutral Analysis Files
The ineff.py script plots the inefficiency as a function of interaction length in the HCal.

```bash
python ineff.py -l <label> <outfile base name> <input file>
```

