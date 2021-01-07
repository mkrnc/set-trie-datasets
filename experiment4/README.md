# Hepatitis and Lymphography Dataset

The dataset is generated using the data mining tool [fdep](http://people.cs.bris.ac.uk/~flach/fdep/) with the datasets [Hepatitis](https://archive.ics.uci.edu/ml/datasets/hepatitis) and [Lymphography](https://archive.ics.uci.edu/ml/datasets/Lymphography) from UCI Machine Learning Repository being its input.

The **fdep** tool was used to generate the following datasets:

- **hepat-p0.1**: complete positive cover for **Hepatitis** dataset with pruning level 0.1
- **lymph-p0.1**: complete positive cover for **Lymphograpy** dataset with pruning level 0.1
- **hepat-p0**: complete negative cover for **Hepatitis** dataset with pruning level 0.1
- **lymph-p0**: complete negative cover for **Lymphograpy** dataset with pruning level 0.1

The *raw* datafile represents the whole dataset in the form of a set of sets in a numeric representation. The sets in the file are in the original order. The *raw* file is used for sampling *train* and *test* datasets. The *train* part is used to initialize the data structure and the *test* part is used for querying.

The *raw*, *train* and *test* files have the same format.
A line in the file represents a set. Each set consists of a sorted sequence of integer numbers separated by a coma.

Each of the above datasets was split into *train* and *test* parts:

- **hepat-p0.1**:
	- [hepat-p0.1.train](https://github.com/mkrnc/set-trie-datasets/blob/main/experiment4/hepat-p0.1.train): 80%
	- [hepat-p0.1.test](https://github.com/mkrnc/set-trie-datasets/blob/main/experiment4/hepat-p0.1.test): 20%
- **lymph-p0.1**: 
	- [lymph-p0.1.train](https://github.com/mkrnc/set-trie-datasets/blob/main/experiment4/lymph-p0.1.train): 80%
	- [lymph-p0.1.test](https://github.com/mkrnc/set-trie-datasets/blob/main/experiment4/lymph-p0.1.test): 20%
- **hepat-p0**: 
	- [hepat-p0.train](https://github.com/mkrnc/set-trie-datasets/blob/main/experiment4/hepat-p0.train): 80%
	- [hepat-p0.test](https://github.com/mkrnc/set-trie-datasets/blob/main/experiment4/hepat-p0.test): 20%
- **lymph-p0**:
	- [lymph-p0.train](https://github.com/mkrnc/set-trie-datasets/blob/main/experiment4/lymph-p0.train): 80%
	- [lymph-p0.test](https://github.com/mkrnc/set-trie-datasets/blob/main/experiment4/lymph-p0.test): 20%

