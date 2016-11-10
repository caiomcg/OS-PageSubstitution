# OS-PageSubstitution

[![Build Status](https://travis-ci.org/caiomcg/OS-SchedulingSimulation.svg?branch=master)](https://travis-ci.org/caiomcg/OS-SchedulingSimulation)
<a href="https://scan.coverity.com/projects/caiomcg-os-schedulingsimulation"> <img alt="Coverity Scan Build Status" src="https://scan.coverity.com/projects/10188/badge.svg"/> </a>
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/caiomcg/OS-SchedulingSimulation/master/LICENSE)

A python simulation of FIFO(First In, First Out), OTM(Optimum Algorithm) and LRU(Least Recently Used) page substitution algorithms.

## Requirements ##

* Python interpreter.

## Build Instructions ##

* Clone the project.
* Execute main.py

```
$> git clone https://github.com/caiomcg/OS-PageSubstitution.git
$> cd OS-PageSubstitution
```

## Execution Instructions ##

### With a file ###
* Move to the debug folder.
* Run the script and pipe a file to it.

```
$> cd OS-PageSubstitution
$> ./main.py < input.txt
```

### Directly to the application ###
* Move to the repository folder.
* Run the script and type the input.
* Send EOF signal

```
$> cd OS-PageSubstitution
$> ./main.py
$> 0 20
$> 0 10
$> 4 6
$> 4 8
$> CTRL + D
```
