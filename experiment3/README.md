# Artificially generated sets of sets for Experiment 3

The sets of sets used for the construction of set-tries $S$ are generated from the collection of $N$ subsets of an alphabet $\Sigma$, where each subset is selected from $\mathcal{P}(\Sigma)$ uniformly at random, each by a given probability $p$. In other words, we traverse through all subsets of $\Sigma$ and add each set to $S$ with probability ~$p$.

The test set of sets $T$ of size $M$ is generated in a similar way to the generation of sets for the construction of the set-tries $S$. However, we construct $T$ so that all lengths of sets from $T$ have approximately the same number of instances. Note that the parameters $p$ and $M$ have a direct influence on the cardinality of a given set-trie or test set, respectively.

### Datasets of Experiment 3

The sets of sets used for the construction of set-tries in Experiment 3 are named "*s-trie_sigma=25_n=320000_No.K.txt*", where *K* has the values from 0 to 19. The 20 different sets of sets store $1.5\%$ of all possible subsets of $[0,24]$, i.e., approximately 500000 sets. 

The test sets of sets used in Experiment 3 have the name "*flat-input_sigma=25-T.txt*", where *T* can have the value *first*, *last*, *middle* and *spread*. Each of the test sets includes exactly 25 sets. Let $k$ stand for an index from $[0,24]$. The set *first* includes the sets that for all $k$ contain the indexes from the interval $[0,k]$. The set *last* contains the indexes from the interval $[k,24]$. The set \textsc{middle} includes the sets that contain the elements around the center index $12$. Finally, the set *spread* includes sets including the indexes that are spread as much as possible in the given range $[0,24]$. 