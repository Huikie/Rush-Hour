# results

The results of running the random bound and breadth first algorithms can be found in this folder. All files are saved with a .txt extension and are written in English. Only the file complexity of rush hour is written in Dutch. All the results were generated on a computer with the following specifications:

* **CPU** - i7 5820k
* **Ram** - 32GB at 2400MHz
* **OS** - Windows 10 Professional

## File content

### breadthfirst.txt

In the breadth first file the results of running the breadth first algorithm can be found. Besides the breadth first algorithm results, the file also includes random bound results for each board. For each board the random bound was set on 10000 iterations.

### randombound.txt

In this file more extensive random bound calculations have been done than the ones mentioned in the breadth first file. Here the results can be found of running the random bound algorithm 100 times on every board. Each time the algorithm was run with 1000 iterations. This instead of running the algorithm one time with 10000 iterations in the breadth first file. Only for game 7 was the algorithm run 50 times with 1000 iterations (due to the required calculation time).

### state-space.txt

In the state-space file the minimal objective function and maximal state-space function can be found. We've applied these functions to every board, giving an indication of the minimal and maximal moves needed to solve a board. Also for the first three board the total state space has been calculated.

### complexity_of_rush_hour.txt

In this file we attempt to shed some light on the question of: what makes a rush hour board difficult? This file is in Dutch.


*Disclaimer: Upon reproduction results might vary from the ones mentioned here. In case of the breadth first algorithm this might be due to a difference in hardware. In case of the random bound algorithm, this variation might be due to chance*
