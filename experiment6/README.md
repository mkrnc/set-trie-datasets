# MSWEB Dataset

The dataset [**msweb**]() stores the data about accessing the pages of two Web servers by random users.

The dataset is converted to a form of a multiset of sets and adapted to meet the required format of [set-trie](https://bitbucket.org/isavnik/settrie/) and [inverted index](https://github.com/nick-ak96/InvertedIndex) benchmark programs.

The *raw* datafile represents the whole dataset converted to the form of a set of sets in a numeric representation. The sets in the file are in the original order. The *raw* file is used for sampling *train* and *test* datasets. The *train* part is used to initialize the data structure and the *test* part is used for querying. Since [set-trie](https://bitbucket.org/isavnik/settrie/) ignores duplicates they were eliminated before sampling.

The *raw*, *train* and *test* files have the same format.
A line in the file represents a set. Each set consists of a sorted sequence of integer numbers separated by a coma.

### Sampling

The *raw* dataset is processed to eliminate duplicates and sampled randomly with the following proportions:

- [train](https://github.com/mkrnc/set-trie-datasets/blob/main/experiment6/msweb.data.train): 100%
- [test](https://github.com/mkrnc/set-trie-datasets/blob/main/experiment6/msweb.data.test): 20%