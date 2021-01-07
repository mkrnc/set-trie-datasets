import os
from random import random
from matplotlib import pyplot as plt

# global settings
dir_workspace = "/Users/miki/Projects/set_trie_comparison/new_comparison"
dir_exp = dir_workspace + "/exp_msnbc_no_duplicates"
dir_original_data = dir_exp + "/data/raw/"
dir_results = dir_exp + "/data/results/"
dir_plots = dir_exp + "/plots/"
settrie = {
    "methods": [ "-m1", "-m2","-m3", "-m4" ]
}
iindex = {
    "methods": ["sb", "asb","sp","asp"]
}
subset = [ "-m1", "sb" ]
superset = [ "-m2", "sp" ]
subset_all = [ "-m3", "asb" ]
superset_all = [ "-m4", "asp" ]

def get_datasets():
    file_pairs = []
    for f in os.listdir(dir_original_data):
        file_pairs.append(f)
    return file_pairs

def normalised(d):
    d1={}
    for k in d:
        d1[k]={}
        for op in d[k]:
            d1[k][op]={}
            for j in d[k][op]:
                d1[k][op][j]=d[k][op][j][1]/d[k][op][j][0]
    return d1

def domain_analyze():
    res = analyze_experiment()
    return normalised(res)

def analyze_experiment():
    results = {}
    datasets = get_datasets()
    for ds in datasets:
        results[ds] = {}
        for method in settrie["methods"]:
            f_result = dir_results + "settrie/" + ds + "." + method
            results[ds][method] = analyze_result(f_result)
        for method in iindex["methods"]:
            f_result = dir_results + "iindex/" + ds + "." + method
            results[ds][method] = analyze_result(f_result)
    return results

def analyze_result(result_file):
    if not os.path.isfile(result_file):
        print("File " + result_file + " does not exist!")
    results = {}
    with open(result_file, "r") as f:
        for line in f:
            split = line.split(';')
            if len(split) == 4:
                input_length = len(split[0].split(','))
                value = int(split[3][4:])
                if input_length in results:
                    results[input_length][0] += 1
                    results[input_length][1] += value
                else:
                    results[input_length] = [1, value]
    return results

########### aux functions for plottings

def select_color(method):
    if method in settrie["methods"]:
        return u'darkolivegreen'
    else:
        return u'darkred'

def random_marker(method):
    if method in settrie["methods"]:
        return "o"
    else:
        return "p"
    #markers_list=["o", "p", "s" , "x" , "+" , "*" , "D", "d","H", "h"  ,"1" , "2" , "3" , "4" ]
    #return markers_list[int(random()*len(markers_list))]

def leg(method):
    if method in settrie["methods"]:
        return "Set Trie"
    else:
        return "Inverted Index"

def select_title(method):
    if method in subset:
        return "Subset existence"
    elif method in superset:
        return "Superset existence"
    elif method in subset_all:
        return "Find all subsets"
    elif method in superset_all:
        return "Find all supersets"

def tit(pair):
    if pair == subset:
        return "Subset existence", "subset_ex"
    if pair == superset:
        return "Superset existence", "superset_ex"
    if pair == subset_all:
        return "Find all subsets", "subset_all"
    if pair == superset_all:
        return "Find all subsets", "superset_all"

def tit_cols(pair1, pair2):
    if pair1 == subset and pair2 == superset:
        return "Existence", "cols_ex"
    if pair1 == subset_all and pair2 == superset_all:
        return "Find all", "cols_all"
    raise "Invalid pair"

###########

def draw(results, exp_type, export = False):
    plt.close('all')
    for ds in results:
        plt.figure()
        for m in exp_type:
            x, y = map(list, zip(*sorted(results[ds][m].items())))
            plt.plot(x, y, color = select_color(m), marker = random_marker(m), markerfacecolor = select_color(m), label = leg(m))
            plt.legend(loc = 5)
            plt.xlabel('length of input')
            plt.ylabel('time $[ns]$')
            plt.title(select_title(m))
            plt.yscale('symlog')
            t, suffix = tit(exp_type)
        if export:
            filename = dir_plots + ds + "_" + suffix
            plt.savefig(filename + ".pdf")
            plt.savefig(filename + ".png")
        else:
            plt.show()

def draw_cols(results, exp_type1, exp_type2, export = False):
    plt.close('all')
    for ds in results:
        f, (plt1, plt2) = plt.subplots(1, 2, sharey=True, figsize=(14, 6))
        f.text(0.5, 0.04, 'length of input', ha='center', va='center')
        f.text(0.06, 0.5, 'time $[ns]$', ha='center', va='center', rotation='vertical')
        #plt.xlabel('length of input')
        #plt.ylabel('time $[ns]$')
        for m in exp_type1:
            x, y = map(list, zip(*sorted(results[ds][m].items())))
            plt1.plot(x, y, color = select_color(m), marker = random_marker(m), markerfacecolor = select_color(m), label = leg(m))
            plt1.legend(loc = 5)
            plt1.set_title(select_title(m))
        for m in exp_type2:
            x, y = map(list, zip(*sorted(results[ds][m].items())))
            plt2.plot(x, y, color = select_color(m), marker = random_marker(m), markerfacecolor = select_color(m), label = leg(m))
            plt2.legend(loc = 5)
            plt2.set_title(select_title(m))
        plt.yscale('symlog')
        if export:
            t, suffix = tit_cols(exp_type1, exp_type2)
            filename = dir_plots + ds + "_" + suffix
            plt.savefig(filename + ".pdf")
            plt.savefig(filename + ".png")
        else:
            plt.show()

def draw_all(results, exp_type1, exp_type2, exp_type3, exp_type4, export = False):
    plt.close('all')
    for ds in results:
        f, ((plt1, plt2), (plt3, plt4)) = plt.subplots(2, 2, sharey=True, sharex=True, figsize=(14, 12))
        f.text(0.5, 0.04, 'length of input', ha='center', va='center')
        f.text(0.06, 0.5, 'time $[ns]$', ha='center', va='center', rotation='vertical')
        for m in exp_type1:
            x, y = map(list, zip(*sorted(results[ds][m].items())))
            plt1.plot(x, y, color = select_color(m), marker = random_marker(m), markerfacecolor = select_color(m), label = leg(m))
            plt1.legend(loc = 5)
            plt1.set_title(select_title(m))
        for m in exp_type2:
            x, y = map(list, zip(*sorted(results[ds][m].items())))
            plt2.plot(x, y, color = select_color(m), marker = random_marker(m), markerfacecolor = select_color(m), label = leg(m))
            plt2.legend(loc = 5)
            plt2.set_title(select_title(m))
        for m in exp_type3:
            x, y = map(list, zip(*sorted(results[ds][m].items())))
            plt3.plot(x, y, color = select_color(m), marker = random_marker(m), markerfacecolor = select_color(m), label = leg(m))
            plt3.legend(loc = 5)
            plt3.set_title(select_title(m))
        for m in exp_type4:
            x, y = map(list, zip(*sorted(results[ds][m].items())))
            plt4.plot(x, y, color = select_color(m), marker = random_marker(m), markerfacecolor = select_color(m), label = leg(m))
            plt4.legend(loc = 5)
            plt4.set_title(select_title(m))
        plt.yscale('symlog')
        if export:
            suffix = "all"
            filename = dir_plots + ds + "_" + suffix
            plt.savefig(filename + ".pdf")
            plt.savefig(filename + ".png")
        else:
            plt.show()



res = domain_analyze()
draw(res, subset, True)
draw(res, superset, True)
draw(res, subset_all, True)
draw(res, superset_all, True)

draw_cols(res, subset, superset, True)
draw_cols(res, subset_all, superset_all, True)

draw_all(res, subset, superset, subset_all, superset_all, True)
