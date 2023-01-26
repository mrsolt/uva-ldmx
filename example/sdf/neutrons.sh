#!/bin/bash

#SBATCH --partition=shared
#
#SBATCH --job-name=test
#SBATCH --output=log/output_%a.txt
#SBATCH --error=log/output_%a.txt
#
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --mem-per-cpu=1g
#
#SBATCH --time=0-00:10:00
#
#SBATCH --gpus 1

source $LDMX_BASE/scripts/ldmx-env.sh

ldmx fire neutrons.py ${SLURM_ARRAY_TASK_ID} /scratch/mrsolt/neutron_${SLURM_ARRAY_TASK_ID}.root
