# Heuristieken Smartgrid

Smartgrid is a project where green energy is produced by houses, but there is an overproduction of green energy. This overproduction can be stored into batteries. There are three dummy-districts, with each five batteries. 

# The assignment
The goal of this project is to connect the houses with the batteries in the most optimal way. The most optimal solution should have the least costs. The assignment consists of 4 parts:

a) Connect all the houses of the three districts to a battery. The maximumcapacity of the houses may not exceed the capacity of the batteries.

The batteries are 5000 per piece and the cables 9 per grid-segment. The cables lay on the gridlines, and the distance between a house and a battery is calculated using the manhattan distance.

b) Calculate the costs of the configurated district in a). Try to optimize your grid and find an as good as possible configuration of the cables.

The batteries may not be located on the best possible places. Relocating the batteries complicates the case, but the principal still wants to try it.

c) Relocate the batteries and try to realise a better result. 

The company SmartBatteryCompany has recently developed three types of batteries, with different capacities and prices.

| Batterytype  | Capacity 	| Price |
| -----------  | :--------: | :---: |
| PowerStar 	 |    450 	  |  900  |
| Imerse-II 	 |    900 	  | 1350  |
| Imerse-III 	 |   1800 	  | 1800  |

Try to achieve a better configuration for the district with these batteries, you can use as many as you want and they can be located on each gridpoint without a house.

d) Optimize the smartGrid for the districts.

# Installation
The project can be retrieved by copying the code in the files, and installing the required packages.

## Prerequisites
The packages used in this project are:
- mathplotlib.pyplot is a library which produces figures in a variety of formats, helps to represent the way the houses are                             connected to the batteries in a plot. To install matplotlib.pyplot, type the following in your terminal:

   - python -mpip install -U pip
   - python -mpip install -U matplotlib
   
- cycler
- numpy
- pyparsing
- pytz
- six
- python-dateutil


# Algorithms
The following algorithms are set up to retrieve the most optimal solution:
- Cable list
- Cable list sneller en korter
- Verre huizen eerst
- Buiten naar binnen
- Hillclimber nieuw
- Batterijen plaatsen met random start
- Batterijen plaatsen mbv hillclimber
- Batterijen plaatsen met combinatie van random restart en hillclimber
- Batterij allerlei
