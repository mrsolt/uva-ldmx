#!/bin/bash

#SBATCH --partition=shared
#
#SBATCH --job-name=test
#SBATCH --output=/scratch/mrsolt/TBreco/pass0/MC/log/output_pi-_4GeV_%a.txt
#SBATCH --error=/scratch/mrsolt/TBreco/pass0/MC/log/output_error_pi-_4GeV_%a.txt
#
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --mem-per-cpu=1g
#
#SBATCH --time=0-04:00:00
#
#SBATCH --gpus 1

source $LDMX_BASE/ldmx-sw/scripts/ldmx-env.sh

ldmx fire /sdf/group/ldmx/users/mrsolt/ldmx-sw/Hcal/exampleConfigs/tb_sim_pass1.py --nevents 10000 --particle pi- --energy 4. --runnumber ${SLURM_ARRAY_TASK_ID} --output_dir /scratch/mrsolt/TBreco/pass0/MC/
