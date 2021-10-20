import subprocess as sub
import sys
import os
import numpy as np


#test prefixes
test_prefix_4a = "test_4a"
test_prefix_amb = "test_amb"
test_prefix_n = "test_n"
test_prefix_no_change = "test_no_change"
test_prefix_lb_1_perc = "test_lb_1_perc"
test_prefix_lb_5_perc = "test_lb_5_perc"
test_prefix_lb_10_perc = "test_lb_10_perc"
test_prefix_R = "Root_tree"
test_prefix_lb_1_change = "test_lb_1_change"
test_prefix_lb_5_change = "test_lb_5_change"
test_prefix_lb_10_change = "test_lb_10_change"

tool_path = "/project/exaptation/Tools/"
root_tree_path = "/project/exaptation/fast_approx_pruning/phylo_likelihood_mut_diff/"

#Commands

prefix_list = ["test_4a", "test_amb", "test_n", "test_no_change", "test_lb_1_perc", "test_lb_5_perc", "test_lb_10_perc", "test_lb_1_change", "test_lb_5_change", "test_lb_10_change"]
for test_prefix in prefix_list:
    test_data_path = "/project/exaptation/fast_approx_pruning/test_data/" + test_prefix + "/"
    mut_diff = "python3 "+ tool_path + "createDiffsFile.py --path " + test_data_path + " --reference EPI_ISL_402124_lowercase.fasta --fasta " + test_prefix + ".fa" + " --output " + test_prefix + ".mut_diff"
    sub.call(mut_diff, shell=True)
    Fasttree = tool_path + "FastTree -nt " + test_data_path + test_prefix + ".fa > " + test_data_path + test_prefix + ".fastree "
    sub.call (Fasttree, shell=True)
    Phylip = "python3 "+ tool_path + "fasta2phylip.py  -i " + test_data_path + test_prefix + ".fa " + "-o  " + test_data_path + test_prefix + ".phy " + "-r "
    sub.call (Phylip, shell=True)
    Rooted_tree = "Rscript " + root_tree_path + test_prefix_R + ".R "
    sub.call (Rooted_tree, shell=True)
