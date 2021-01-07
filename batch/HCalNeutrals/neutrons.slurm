#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --time=4:00:00
#SBATCH --output=log/neutron_1GeV_840_geant10.2_%a.out
#SBATCH --partition=standard
#SBATCH -A hep_aag 

source "$LDMX_BASE/ldmx-sw/scripts/ldmx-env.sh"

ldmx fire neutrons.py ${SLURM_ARRAY_TASK_ID} /scratch/gtf9nz/ldmx/1gev_neutrals/neutrons/geant_10.2/neutron_1GeV_840_geant10.2_${SLURM_ARRAY_TASK_ID}.root 
