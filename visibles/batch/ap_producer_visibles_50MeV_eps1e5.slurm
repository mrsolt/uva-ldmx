#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --time=8:00:00
#SBATCH --output=log/mAp_produced_050_eps1e5_%a.out
#SBATCH --partition=standard
#SBATCH -A ldmx 

source "$LDMX_BASE/ldmx-sw/scripts/ldmx-env.sh"

ldmx fire $UVA_LDMX_DIR/ap_producer.py ${SLURM_ARRAY_TASK_ID} /project/hep_aag/ldmx/ap/visibles/LHE/mAp_050/mAp_050_eps1e5_${SLURM_ARRAY_TASK_ID}_brem.lhe /project/hep_aag/ldmx/ap/visibles/LHE/mAp_050/mAp_050_eps1e5_${SLURM_ARRAY_TASK_ID}_decay.lhe /project/hep_aag/ldmx/ap/visibles/produced/mAp_050/mAp_050_eps1e5_${SLURM_ARRAY_TASK_ID}.root 33000
