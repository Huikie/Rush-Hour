# Rush Hour

In Rush Hour, a sliding block logic game developed by ThinkFun, you have to battle the gridlock as you slide the blocking vehicles out of the way for the red car to exit.

For more information about the game and some visualizations please [click here](https://www.thinkfun.com/products/rush-hour/)

The full assignment can be found on the [Heuristieken](http://heuristieken.nl/wiki/index.php?title=Rush_Hour) website.

## Getting Started

### Prerequisites

The codebase has been written in [Python3.7.0](https://www.python.org/downloads/). In requirements.txt you can find all necessary packages to run the code successfully. You can easily install these packages using pip, simply run the command below:

```
pip install -r requirements.txt
```

### Structure

All python algorithms can be found in the folder code/algorithms, the code belonging to the board can be found in the folder code/classes and the state-space calculations and results in the folder results.

### Testing

To run the algorithms a standard command layout has to be used. The command always starts with "python main.py", then the name of the board you want to run ("... .txt"), followed by the algorithm ("breathfirst" or "randombound") and in the case of randombound the amount of iterations the algorithm should run (for example 100).

An example command that runs the *randombound* algorithm on game 1:

```
python main.py game_1.txt randombound 100
```

An example command that runs the *breadthfirst* algorithm on game 1:

```
python main.py game_1.txt breathfirst
```

## Authors

* Hidde van Oijen
* Marijn Meijering
* Daan Huikeshoven

**Team worthless Without coffee**

## Acknowledgments (Special thanks to)

* Bas Terwijn
* Minor programming at the University of Amsterdam
