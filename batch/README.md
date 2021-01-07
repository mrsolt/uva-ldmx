# SLURM Batch System
Rivanna uses the SLURM batch system. The instructions here are specific to the LDMX framework, and more general instructions can be found on the Rivanna [SLURM Job Manager](https://www.rc.virginia.edu/userinfo/rivanna/slurm/).

An example is shown in template.slurm where you would replace ```<config file>``` with the config file of your choice. Note for the SLURM batch system, you must pass the entire environment through the job submission script since it does not pass either the environment you are currently working in or your bashrc. Since you are working inside the container, you can simply source the ldmx-env.sh script in you job submission script.

```bash
source "$LDMX_BASE/ldmx-sw/scripts/ldmx-env.sh"
```

In addition, make sure to source the ldmx-env.sh script before job submission in order to properly set the ```LDMX_BASE``` path. In order to submit a job, simply use the ```sbatch``` command.

```bash
sbatch <slurm file>
```

## Other Useful Commands

To check the status of your jobs:
```bash
squeue -u <computing id>
```

To cancel a job:
```bash
scancel <job id>
```

To incorporate job arrays:
```bash
sbatch --array=<array>
```
```<array>``` would be the desired array. For instance, you would input 1-100 to pass integers 1 through 100, inclusively. In the .slurm file where you would want to pass the integer from the array, you would add ```%a``` in the SBATCH lines and ```${SLURM_ARRAY_TASK_ID}``` in the command lines.
