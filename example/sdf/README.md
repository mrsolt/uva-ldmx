# SLAC SDF System

Many large samples are stored on the SDF file system at SLAC. In order to access these, you will need both a SLAC Windows and Unix account. Instructions on using SDF can be found here: https://sdf.slac.stanford.edu/public/doc/#/ 

The batch system on SDF uses SLURM, the same as Rivanna, and hence the instructions for running the batch system are similar (below).

In order to use the desired directories in Singularity, you must explicitly mount the directories you wish to work in and read/write files. Rivanna automatically mounts the /project and /scratch directories, while the SLAC SDF file system does not. In order to mount custom directories, for instance you may want your /scratch directory and the ldmx/data directory mounted, change the following line in ldmx-env.sh before sourcing.

```bash
--bind ${csv_list} ${LDMX_SINGULARITY_IMG} "$@"
```

```bash
--bind /scratch/<your username>,/sdf/group/ldmx/data,${csv_list} ${LDMX_SINGULARITY_IMG} "$@"
```

More details on mounting and defining bind paths in Singularity can be found here: https://docs.sylabs.io/guides/3.5/user-guide/bind_paths_and_mounts.html 

# Using the Batch Script
The neutrons.sh sample script in this directory submits jobs to the slurm batch system on SDF. This script submits 100 jobs of 10,000 events each. You will have to source ldmx-env.sh first and change the respective paths of the config, input, output, and log files. Only use "shared" for the partition.

To run a batch job on SDF:

```bash
sbatch --array=0-99 neutrons.sh
```

The ```${SLURM_ARRAY_TASK_ID}``` passes each integer from the specified array (0 through 99 inclusively in this case). This sets a different run number (and hence, a different seed) for each job submission.
