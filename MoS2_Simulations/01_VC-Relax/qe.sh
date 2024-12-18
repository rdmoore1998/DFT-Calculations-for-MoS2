#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=20
#SBATCH --time=00:20:00

module load quantum-espresso/6.6

set nodes = `scontrol show hostname "$SLURM_JOB_NODELIST"`

echo "job = ${SLURM_JOB_NAME}"
echo "nodes = $nodes"
echo "Start time = `date +%Y%m%d-%T`"

srun $(which pw.x) -in MoS2.in > MoS2.Energy.out

exit
