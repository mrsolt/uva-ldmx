#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --output=test.out
#SBATCH --partition=standard
#SBATCH -A hep_aag

source "$LDMX_BASE/ldmx-sw/scripts/ldmx-env.sh"

ldmx fire <config file>
