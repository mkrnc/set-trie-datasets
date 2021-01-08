# Artificially generated sets of sets for Experiment 1

The sets of sets used for the construction of set-tries $S$ are generated from the collection of $N$ subsets of an alphabet $\Sigma$, where each subset is selected from $\mathcal{P}(\Sigma)$ uniformly at random, each by a given probability $p$. In other words, we traverse through all subsets of $\Sigma$ and add each set to $S$ with probability ~$p$.

The test set of sets $T$ of size $M$ is generated in a similar way to the generation of sets for the construction of the set-tries $S$. However, we construct $T$ so that all lengths of sets from $T$ have approximately the same number of instances. Note that the parameters $p$ and $M$ have a direct influence on the cardinality of a given set-trie or test set, respectively.

### Datasets of Experiment 1

The sets of sets used for the generation of set-tries in Experiment 1 are named `*s-trie_sigma=25_n=N.txt*`, where the size of the alphabet $\Sigma$ is 25, and *N* has the values 10000, 20000, 40000, 80000, 160000, and 320000. 

The test sets of sets used in Experiment 1 have the name `*flat-input_sigma=25_M=M.txt*`, where $\sigma$ is 25, and *M* has the values 15000 and 50000. 