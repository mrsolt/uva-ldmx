#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --output=log/neutron_%a.out
#SBATCH --partition=standard
#SBATCH -A ldmx

source "$LDMX_BASE/ldmx-sw/scripts/ldmx-env.sh"

ldmx fire $LDMX_UVA/example/config/neutrons.py ${SLURM_ARRAY_TASK_ID} $NEUTRON_DIR/neutron_${SLURM_ARRAY_TASK_ID}.root
