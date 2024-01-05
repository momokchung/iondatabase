#!/bin/bash
# Define your function
ssh_elf () {
source /user/kchung25/source_local.sh
cd $1 && ./$2 &
}

work_dir=$PWD
ssh elf$1 "$(typeset -f ssh_elf); ssh_elf $work_dir Clwater_run_sim.sh
"
