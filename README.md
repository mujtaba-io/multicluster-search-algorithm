# multicluster search algorithm

This idea came to my mind that we can categorize given data into multiple separate clusters based on similarity functions or any given criteria. We can then perform search very efficiently on a big dataset by simply checking the similarity of the search query based on same criteria and then searching only in those clusters which are similar to the search query. This will reduce the search time drastically.

However, this algorithm is not very efficient for small datasets as the time taken to cluster the data will be more than the time taken to search the data. But for large datasets, this algorithm will be very efficient.

Also, I believe alot of data will not be indexed/detected by this algorithm if the criteria for clustering is ambiguous. Since it can be the case when en entity which is in reality similar to a given search query is not found to be similar by the choosen similarity function.

## algorithm

1. We make a database of all the data we have, by applying similarity function of each data part, and classifying data into clusters. We further classify each cluster into multiple sub-clusters, since we can have a huge dataset, so top-level clustering is not enough.
2. We take search query as input, and apply the same similarity function on it, and classify its "direction/orientation" in the cluster space.
3. We then search only in those clusters which are similar to the search query, and then we search only in those sub-clusters which are similar to the search query, with more and more precision.
4. We then return the search results.

## implementation & testing

I am going to use my own [words-dataset](https://github.com/mujtaba-io/words-dataset), which is a simple list of english language words in a linear list. I will be making clusters of that data, and will apply search on it.

I will be calculating time it took to search based on this technique vs the linear search.


