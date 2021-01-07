# HCal Neutrals Batch Scripts
These scripts submit jobs to the slurm batch system on Rivanna using the config files from the [config/HCalNeutrals](https://github.com/mrsolt/uva-ldmx/tree/main/config/HCalNeutrals) directory.
They submit 100 jobs of 10,000 events each.

```bash
sbatch --array=0-99 kaons.slurm
```
```bash
sbatch --array=0-99 neutrons.slurm
```

The ```${SLURM_ARRAY_TASK_ID}``` passes each integer from the specified array (0 through 99 inclusively in this case). This set a different run number (and hence, a different seed) for each job submission.

Sometimes, you may want to run a different version of the container. For instance, you may want to use a different version of Geant4. This must be passed to the slurm batch system. Let's say you need Geant4.10.5 (and you have already created the .sif file), you would add the following to your .slurm file.

```bash
source "$LDMX_BASE/ldmx-sw/scripts/ldmx-env.sh" - t geant4.10.5
```

To run analysis scripts on the output files you just created, do the following.

```bash
sbatch --array=0-99 analysis_k0.slurm
```
```bash
sbatch --array=0-99 analysis_neutron.slurm
```

TODO: These scripts are specific to the specified directories and needs to be generalized.
