# Practical loop scheduling / 1D partitioning activity

This repository is intended for use by students to practice concepts related to loop scheduling and notions of locality and overhead.
It contains a few scheduling algorithms and some support functions.
A set of activities using this repository is presented in the [activities section](#activities) below.

## How To

- The code in this repository is written using Python3.

- To run a code example, try `python3 complete_example.py`.

- To learn more about the schedulers and support functions, try the code below in your Python3 interpreter:

```python
>>> import simulator.schedulers as schedulers
>>> help(schedulers)
>>> import simulator.support as support
>>> help(support)
```

- To check if the code you downloaded or changed is still working properly, try the following commands:

```bash
$ cd unitary_tests
$ ./test_implemented_schedulers.py 
$ ./test_support.py
```

- To check if the new schedulers you have implemented are working as intended, try the following commands:

```bash
$ cd unitary_tests
$ ./test_other_schedulers.py 
```

## Activities

**Basic steps**

1. Run `python3 complete_example.py` and try to understand its results. Check how to write code to use this simple loop scheduling simulator.

2. Run experiments comparing the performance of the static scheduler with different chunk sizes and the Largest Processing Time (LPT) list scheduling algorithm.
Check how they differ in terms of makespan, number of calls to the scheduler, and locality.

3. Write the dynamic and guided schedulers (complete classes *OpenMPDynamic* and *OpenMPGuided* in [the schedulers file](simulator/schedulers.py)). Check if they pass the tests in [the unitary tests' file](unitary_tests/test_other_schedulers.py).

4. Run experiments comparing the static, dynamic, and guided schedulers with tens or hundreds of tasks and resources. Compare them using different chunk sizes.

5. Write the recursive bipartitioning algorithm for situations where the number of resources is a power of two (complete class *RecursiveBipartition*). Check if it passes the test in the unitary tests' file.

6. Run experiments comparing the recursive bipartition and LPT algorithms with tens or hundreds of tasks and resources. Compare their makespan, number of scheduler calls, and locality.

**Additional challenge**

7. Extend the recursive bipartition algorithm to work with arbitrary numbers of resources, and compare its results to the ones of the other schedulers.

8. Write Nicol's algorithm and compare it to the previous algorithms.
