# Artificially generated sets of sets for Experiment 2

The sets of sets used for the construction of set-tries $S$ are generated from the collection of $N$ subsets of an alphabet $\Sigma$, where each subset is selected from $\mathcal{P}(\Sigma)$ uniformly at random, each by a given probability $p$. In other words, we traverse through all subsets of $\Sigma$ and add each set to $S$ with probability ~$p$.

The test set of sets $T$ of size $M$ is generated in a similar way to the generation of sets for the construction of the set-tries $S$. However, we construct $T$ so that all lengths of sets from $T$ have approximately the same number of instances. Note that the parameters $p$ and $M$ have a direct influence on the cardinality of a given set-trie or test set, respectively.

### Datasets of Experiment 2

The sets of sets used for the generation of set-tries in Experiment 2 are named "*s-trie_sigma=G_p=P.txt*", where the size *G* of the alphabet $\Sigma$ has the values 14, 17, 20, 23, and 26, and the probability *P* has the values 1.0% and 2.0%. 

The test sets of sets used in Experiment 1 have the name "*flat-input_sigma=G_M=50000.txt*", where the size *G* of the alphabet $\Sigma$ has the values 14, 17, 20, 23, and 26. The number of test sets is 50000 in all datasets.