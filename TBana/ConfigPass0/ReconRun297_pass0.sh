#!/bin/bash

#SBATCH --partition=shared
#
#SBATCH --job-name=test
#SBATCH --output=/scratch/mrsolt/TBreco/pass0/Data/log/output_run297_%a.txt
#SBATCH --error=/scratch/mrsolt/TBreco/pass0/Data/log/output_error_run297_%a.txt
#
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --mem-per-cpu=1g
#
#SBATCH --time=0-04:00:00
#
#SBATCH --gpus 1

source $LDMX_BASE/ldmx-sw/scripts/ldmx-env.sh

ldmx fire /sdf/group/ldmx/users/mrsolt/ldmx-sw/Hcal/exampleConfigs/tb_reco_pass1.py /sdf/group/ldmx/data/hcal-tb/aligned/decoded/decoded_hcal_run_297_20220426_051552.root --output_dir /scratch/mrsolt/TBreco/pass0/Data/
