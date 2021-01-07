#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --time=4:00:00
#SBATCH --output=log/neutron_analysis_geant10.2_%a.out
#SBATCH --partition=standard
#SBATCH -A hep_aag 

source "$LDMX_BASE/ldmx-sw/scripts/ldmx-env.sh"

ldmx fire /sfs/qumulo/qhome/gtf9nz/ldmx/ldmx-analysis/config/HCalNeutralAna.py /sfs/qumulo/qhome/gtf9nz/ldmx/HCalNeutrals/EffCheck/neutron_geant4.10.2/neutron_geant4.10.2_analysis_${SLURM_ARRAY_TASK_ID}.root /scratch/gtf9nz/ldmx/1gev_neutrals/neutrons/geant_10.2/neutron_1GeV_840_geant10.2_${SLURM_ARRAY_TASK_ID}.root 
