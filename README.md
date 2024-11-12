# Bursts-Detection-Algorithm

## Overview
This project implements a bursts detection algorithm using two different approaches: the Viterbi algorithm and the Bellman-Ford algorithm. The aim is to identify periods of increased activity (bursts) in a sequence of time-stamped events.

## Features 
- Viterbi Algorithm: Finds the optimal sequence of states that minimizes the cost of transitions, useful for detecting bursts in data streams.
- Bellman-Ford Algorithm: Another approach to solve the shortest path problem in a graph, adapted here for bursts detection.
- Customizable parameters for adjusting burst sensitivity (-s) and transition cost (-g).

## File Structure
- bursts.py: The main Python script implementing the bursts detection algorithm
- two_states.txt: A sample input file with timestamps for a system operating in two states
- three_states_1.txt: A sample input file with timestamps for a system operating in three states (first variation)
- three_states_2.txt: A sample input file with timestamps for a system operating in three states (second variation)
- four_states.txt: A sample input file containing timestamps for a system with four states

## Usage
To run the program, use the following command:

```
python bursts.py [-s S] [-g GAMMA] [-d] {viterbi, trellis} offsets_file
```
### Parameters
- -s S: Sets the parameter s of the algorithm (default is s = 2).
- -g GAMMA: Sets the parameter gamma for transition cost (default is gamma = 1).
- -d: Enables diagnostic mode for detailed output.
- {viterbi, trellis}: Choose between viterbi for the Viterbi algorithm and trellis for the Bellman-Ford algorithm.
- offsets_file: Path to the input file containing event timestamps.

### Example Commands
#### 1. Using the Viterbi Algorithm:
```
python bursts.py viterbi two_states.txt
```
#### 2.Using the Bellman-Ford Algorithm with custom parameters:
```
python bursts.py trellis three_states.txt -s 3 -g 0.5
```
#### 3.With Diagnostic Mode Enabled:
```
python bursts.py viterbi offsets_file.txt -d
```

## Example Output

### Example 1: Using the Viterbi Algorithm
#### Command
```
python bursts.py viterbi two_states.txt
```

#### Expected Output
```
0 [0.0 30.0)
1 [30.0 35.0)
0 [35.0 40.0)
```
This indicates that the system was in state 0 from time 0.0 to 30.0, switched to state 1 from 30.0 to 35.0, and returned to state 0 from 35.0 to 40.0.

### Example 2: Using the Bellman-Ford Algorithm with Diagnostic Mode
#### Command:
```
python bursts.py trellis two_states.txt -d
```

#### Expected Output
```
(1, 0) inf -> 3.74 from (0, 0) 0.00 + 0.00 + 3.74
(1, 1) inf -> 7.50 from (0, 0) 0.00 + 2.20 + 5.30
...
(9, 5) 62.48 -> 61.26 from (8, 2) 20.65 + 6.59 + 34.03
(9, 6) 99.98 -> 98.77 from (8, 2) 20.65 + 8.79 + 69.33
10 [0, 0, 0, 0, 1, 1, 1, 1, 1, 0]
0 [0.0 30.0)
1 [30.0 35.0)
0 [35.0 40.0)
```
This detailed output shows the step-by-step cost calculation for each state transition during the execution of the Bellman-Ford algorithm.

## Project Requirements
- Python 3.
- Use only the standard libraries (sys, argparse, math, collections.deque).

## License
This project is developed as part of an academic assignment for the course in algorithms at the Athens University of Economics and Business.




  
