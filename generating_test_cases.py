import subprocess as sub
import sys
import os
import numpy as np

test_prefix = "test_o"
test_data_path = "/project/exaptation/fast_approx_pruning/test_data/test_o/"
tool_path = "/project/exaptation/Tools/"
mut_diff_command_path = "/project/exaptation/fast_approx_pruning/test_data/test_o"

mut_diff = "python3 "+ tool_path + "createDiffsFile.py --path " + test_data_path + " --reference EPI_ISL_402124_lowercase.fasta --fasta " + test_prefix + ".fa" + " --output " + test_prefix + ".mutdiff"
sub.call(mut_diff, shell=True)
Fasttree = tool_path + "FastTree -nt " + test_data_path + test_prefix + ".fa   > " + test_data_path + test_prefix + ".fastree "
sub.call (Fasttree, shell=True)
Phylip = "python3 "+ tool_path + "fasta2phylip.py  -i " + test_data_path + test_prefix + ".fa " + "-o  " + test_data_path + test_prefix + ".phy " + "-r "
sub.call (Phylip, shell=True)