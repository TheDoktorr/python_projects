# N-body solar system written in Python.

## Imports:
 matplotlib     - plotting    
 numpy          - array maths    
 os             - used to run terminal commands    
 platform       - used to determine operating system    
 pickle         - binary file storage     
 
 spiceypy       - transformation matrices     
 astrpoy        - gets data from specified ephemeris           - source: https://github.com/poliastro/poliastro/archive/main.zip     
 poliastro      - gets mass constants for planetary bodies     

If using a environment manager, packages such numpy and matplot can be installed via CLI or GUI,    
  1) verify the correct environment is used,    
```
conda info --envs
 conda activate env-name
```
  2) list and install packages,   
```
conda list
conda isntall pkg-name
```
 
Other packages can be obtained through pip, Python's package manager:    
`pip install jplephem spiceypy`      
Poliastro must be obtained from Github,   
`pip install https://github.com/poliastro/poliastro/archive/main.zip`      

## File structure:
Constants.py  and Particle.py       
- These handle mass constants, and the particle class used for all planetary bodies
                   
Setup.py
- The main computation file, this handles class creation, intialising variables as well as user input for simulation parameters       
   -> prompted when running Simulation.py as it contains a while loop
- Also contains Kepler's 3rd law calculations as this occurs after the simulation has run
                   
Simulation.py
- The main simulation loop, graphing and outputs. This is the file you run.               
- contains code and data saving used for graphs in the report, this is commented out as it's computationally expensive


## Known issues:                   
- `invalid escape sequence \o` - this occurs when file paths containing \o are commented out, or not properly formated with a raw string             
- errors regarding file paths - this should work in the final release but occasionally python through errors finding the .pkl files despite them being in the directory                                    
- "Even when not re-running the simualation, I still have to enter simulation parameters?" - This was an oversight in implementation order causing the same `while True:` loop to run despite no intent to run the sim.                 
- Graphs included in sim file. - due to variable storage, they cannot be in their own file, as this would be depenedent on Setup.py **and** Simulation.py, which creates circular dependencies.
- Kepler's law calculated outside of class - due to using post-sim. data, there's definitely a better way of doing this...
- .pkl cache file can become quite large, when doing long simulations (~ 1 GB) 

## How to setup:
1) install necessary pacakges
2) run Simulation.py
3) wait for ephemeris to download if not ran before
4) follow on screen dialogue
