# OS-PageSubstitution

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
