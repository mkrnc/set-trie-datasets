import os
from random import random

# global settings
dir_workspace = "/Users/miki/Projects/set_trie_comparison/new_comparison"
dir_exp = dir_workspace + "/exp_msweb_no_duplicates_train100"
dir_original_data = dir_exp + "/data/raw/"
dir_prepared_data = dir_exp + "/data/prepared/"
dir_results = dir_exp + "/data/results/"
dir_plots = dir_exp + "/plots/"
settrie = {
    "path_bin": dir_workspace + "/src/settrie/src/set2",
    "methods": [ "-m1", "-m2","-m3", "-m4" ]
}
iindex = {
    "path_bin": dir_workspace + "/src/InvertedIndex/src/inverted_index",
    "methods": ["sb", "asb","sp","asp"]
}
src_scripts = dir_exp + "/scripts/script.sh"
# ratio to split raw data to test/train datasets
ratio = .8
ext_train = ".train"
ext_test = ".test"

def split_files():
    print("Preparing test datasets...")
    file_pairs = []
    if not os.path.isdir(dir_prepared_data):
        print("Direcotry\n" + dir_prepared_data + "\n does not exists")
        return
    for f in os.listdir(dir_original_data):
        with open(dir_original_data + f, "r") as raw_file:
            with open(dir_prepared_data + f + ext_train, "w") as train_file:
                with open(dir_prepared_data + f + ext_test, "w") as test_file:
                    for line in raw_file:
                        if random() < ratio:
                            train_file.write(line)
                        else:
                            test_file.write(line)
        file_pairs.append(f)
    return file_pairs

def remove_files_from_dir(dir):
    if os.path.isdir(dir):
        for f in os.listdir(dir):
            remove_file(dir + f)

def remove_file(file):
    if os.path.isfile(file):
        print("Deleting a file\n" + file)
        os.system("rm " + file)

def clean_workspace():
    print("Clean up...")
    remove_files_from_dir(dir_prepared_data)
    remove_files_from_dir(dir_results + "settrie/")
    remove_files_from_dir(dir_results + "iindex/")
    remove_files_from_dir(dir_plots)
    remove_file(src_scripts)

def create_script(datasets):
    print("Creating a script...")
    with open(src_scripts, "w") as script_file:
        script_file.write('#!/bin/bash\n')
        for ds in datasets:
            f_train = dir_prepared_data + ds + ext_train
            f_test = dir_prepared_data + ds + ext_test
            for method in settrie["methods"]:
                f_result = dir_results + "settrie/" + ds
                script_file.write(settrie["path_bin"] + " " + method + " " + f_test + " < " + f_train + " > " + f_result + "." + method + "\n")
            for method in iindex["methods"]:
                f_result = dir_results + "iindex/" + ds
                script_file.write(iindex["path_bin"] + " < " + f_train + " " + f_test + " " + method + " > " + f_result + "." + method + "\n")


#clean_workspace()
#datasets = split_files()
datasets = []
for f in os.listdir(dir_original_data):
    datasets.append(f)
create_script(datasets)
