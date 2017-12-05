# Heuristieken Smartgrid

Smartgrid is a project where green energy is produced by houses, but there is an overproduction of green energy. This overproduction can be stored into batteries. There are three dummy-districts, with each five batteries. 

# Motivation
The goal of this project is to connect the houses with the batteries in the most optimal way. The most optimal solution shoudl have the least costs.  

# Prerequisites
The package used in this project is:
- mathplotlib.pyplot is a library which produces figures in a variety of formats, helps to represent the way the houses are                         connected to the batteries in a plot.

# Installation 
The following algorithms are set up to retrieve the most optimal solution:
- Hillclimber with random start 
- Buiten naar binnen
- Randompick
- Hillclimber

## Hillclimber with random start
The algorithm each time starts with a random sequence of houses of a certain district.

## Buiten naar binnen
The houses are connected to the batteries, starting with the houses that are at the utmost end of the grid.

## Randompick
A random sequence of houses of a certain district are connected to the batteries. Each time looking for the optimal solution, by connecting the houses to the batteries in a certain way. Then comparing the result to the previous result and save that result with the lowest cost.

## Hillclimber










