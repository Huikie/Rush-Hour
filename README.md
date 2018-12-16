# Rush Hour

In Rush Hour, a sliding block logic game developed by ThinkFun, you have to battle the gridlock as you slide the blocking vehicles out of the way for the red car to exit.

For more information and pictures please [click here](https://www.thinkfun.com/products/rush-hour/)

## Getting Started

### Prerequisites

The codebase has been written in [Python3.7.0](https://www.python.org/downloads/). In requirements.txt you can find all necessary packages to run the code successfully. You can easily install these packages using pip, simply use the instructions below:

```
pip install -r requirements.txt
```

### Structure

All python algorithms can be found in the folder algorithms, the code belonging to the board and cars can be found in the folder classes, the state-space calculations in the folder state-space and the results in the results folder.

### Testing

To run the algorithms a standard command layout has to be used. The command always starts with "python main.py", then the name of the board you want to run ("... .txt"), followed by the algorithm ("breathfirst" or "randombound") and in the case of randombound the amount of iterations the algorithm should run (for example 1000).

An example command that uses game_1 and the randombound algorithm:

```
python main.py game_1.txt randombound 1000
```

An example command that uses game_1 and the breadthfirst algorithm:

```
python main.py game_1.txt breathfirst
```

## Authors

* Hidde van Oijen
* Marijn Meijering
* Daan Huikeshoven

Team worthless Without coffee

## Acknowledgments

* Bas Terwijn
* Minor programming at the University of Amsterdam
