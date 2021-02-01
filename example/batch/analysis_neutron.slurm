#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --output=log/neutron_analysis_%a.out
#SBATCH --partition=standard
#SBATCH -A hep_aag

source "$LDMX_BASE/ldmx-sw/scripts/ldmx-env.sh"

ldmx fire $LDMX_UVA/example/config/HcalAna.py $ANALYSIS_DIR/neutron_analysis_${SLURM_ARRAY_TASK_ID}.root $NEUTRON_DIR/neutron_${SLURM_ARRAY_TASK_ID}.root
