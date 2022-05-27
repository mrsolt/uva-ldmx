#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --time=4:00:00
#SBATCH --output=log/mAp_050_eps1e5_%a.out
#SBATCH --partition=standard
#SBATCH -A ldmx 

source "$LDMX_BASE/ldmx-sw/scripts/ldmx-env.sh"

ldmx python3 $UVA_LDMX_DIR/ap_LHE_parser.py -o /project/hep_aag/ldmx/ap/visibles/LHE/mAp_050/ -n mAp_050_eps1e5_${SLURM_ARRAY_TASK_ID} -m 0.05 -e 1.e-5 -l /project/hep_aag/ldmx/ap/visibles/visibles/mAp_050_850K_06Aug21/mAp_050_850K_06Aug21_${SLURM_ARRAY_TASK_ID}_decayed_1/unweighted_events.lhe
