
# Flight Distances Exercise
# =========================
# 
# Flying Circus Airlines flies between the following cities (with distances):
# 
# <pre>
#     Atlanta-Chicago:                    590.0
#     Atlanta-Dallas:                     720.0
#     Atlanta-Houston:                    700.0
#     Atlanta-New York:                   750.0
#     Austin-Dallas:                      180.0
#     Austin-Houston:                     150.0
#     Boston-Chicago:                     850.0
#     Boston-Miami:                      1260.0
#     Boston-New York:                    190.0
#     Chicago-Denver:                     920.0
#     Chicago-Houston:                    940.0
#     Chicago-Los Angeles:               1740.0
#     Chicago-New York:                   710.0
#     Chicago-Seattle:                   1730.0
#     Dallas-Denver:                      660.0
#     Dallas-Los Angeles:                1240.0
#     Dallas-New York:                   1370.0
#     Denver-Los Angeles:                 830.0
#     Denver-New York:                   1630.0
#     Denver-Seattle:                    1020.0
#     Houston-Los Angeles:               1370.0
#     Houston-Miami:                      970.0
#     Houston-San Francisco:             1640.0
#     Los Angeles-New York:              2450.0
#     Los Angeles-San Francisco:          350.0
#     Los Angeles-Seattle:                960.0
#     Miami-New York:                    1090.0
#     New York-San Francisco:            2570.0
#     San Francisco-Seattle:              680.0
# </pre>
# 
# We can represent this data in a dictionary mapping the pair of cities to the distance between them. Because the distance between cities isn't directional information, a set of the cities (without any order) seems like the right way to store the keys (pairs of cities). 
# 
# Question 1
# ----------
# Do you remember why a regular set cannot be a key in a dictionary? We will therefore use frozen sets instead. Build a frozen set with Atlanta and Chicago and another one with Atlanta and Dallas. Make a dictionary called `flight_distances` mapping these sets to their distances (590 and 720 respectively).


# your code goes here


# Question 2
# ----------
# 
# We have built for you the full dictionary `flight_distances`. Use it to print the distance from Seattle to Chicago.


flight_distances = {
    frozenset(['Atlanta', 'Chicago']): 590.0,
    frozenset(['Atlanta', 'Dallas']): 720.0,
    frozenset(['Atlanta', 'Houston']): 700.0,
    frozenset(['Atlanta', 'New York']): 750.0,
    frozenset(['Austin', 'Dallas']): 180.0,
    frozenset(['Austin', 'Houston']): 150.0,
    frozenset(['Boston', 'Chicago']): 850.0,
    frozenset(['Boston', 'Miami']): 1260.0,
    frozenset(['Boston', 'New York']): 190.0,
    frozenset(['Chicago', 'Denver']): 920.0,
    frozenset(['Chicago', 'Houston']): 940.0,
    frozenset(['Chicago', 'Los Angeles']): 1740.0,
    frozenset(['Chicago', 'New York']): 710.0,
    frozenset(['Chicago', 'Seattle']): 1730.0,
    frozenset(['Dallas', 'Denver']): 660.0,
    frozenset(['Dallas', 'Los Angeles']): 1240.0,
    frozenset(['Dallas', 'New York']): 1370.0,
    frozenset(['Denver', 'Los Angeles']): 830.0,
    frozenset(['Denver', 'New York']): 1630.0,
    frozenset(['Denver', 'Seattle']): 1020.0,
    frozenset(['Houston', 'Los Angeles']): 1370.0,
    frozenset(['Houston', 'Miami']): 970.0,
    frozenset(['Houston', 'San Francisco']): 1640.0,
    frozenset(['Los Angeles', 'New York']): 2450.0,
    frozenset(['Los Angeles', 'San Francisco']): 350.0,
    frozenset(['Los Angeles', 'Seattle']): 960.0,
    frozenset(['Miami', 'New York']): 1090.0,
    frozenset(['New York', 'San Francisco']): 2570.0,
    frozenset(['San Francisco', 'Seattle']): 680.0,
}



# your code goes here


# Question 3
# ----------
# 
# Compute the total distance flying from Austin to Houston to San Francisco and compare it to the distance if you fly Austin to Dallas to Los Angeles to San Francisco.


# your code goes here


# Question 4
# ----------
# 
# Flying Circus Airlines adds a direct flight between Austin and San Francisco, which is 1500 miles.  Update the flight distances data structure to reflect this. 


# your code goes here


# Question 5
# ----------
# 
# Flying Circus Airlines cancels the service from Boston to Miami.  Remove it from the flight distances.


# your code goes here


# Question 6
# ----------
# 
# Below, we have built for you the list of cities that Flying Circus Airlines reaches. (The question `Bonus 1` after this one will get you to build it yourself if you know about looping.) Another company, SouthBy Airlines, flies to the second list of cities given below. The CEO of SouthBy is trying to evaluate if it makes sense to buy Flying Circus Airlines. <br>
# 1. How many cities would be covered if both companies decided to merge? <br>
# 2. Is Flying Circus Airlines bringing any new cities to the table? <br>
# 3. To see if Flying Circus share holders will approve the merger, list the cities that are currently not covered by them and that would be covered by the merged company.<br>
# 4. To evaluate the efficiency of the future merger, compute how many cities are reached by only one of the 2 companies currently.


flying_circus_cities = ['Houston', 'Chicago', 'Miami', 'Boston', 'Dallas', 'Denver', 'New York', 
                        'Los Angeles', 'San Francisco', 'Atlanta', 'Seattle', 'Austin']
southby_cities = ['Chicago',  'Los Angeles', 'New York', 'Boston', 'Orlando', 'Dallas', 
                  'Toronto', 'Denver', 'Miami', 'San Francisco', 'Houston', 'Atlanta', 'Seattle', 
                  'Vancouver']



# your code goes here


# You will need to be familiar with loops and functions to do the remaining bonus questions.
# 
# Bonus 1
# -------
# 
# Build the set of cities that Flying Circus Airlines flies to programatically. You should have a set containing exactly the cities listed in flying_circus_cities above.

# Hint: Use a `for` loop over the keys of the dictionary above and the union operation on sets to build that set. 


# your code goes here


# Bonus 3
# -------
# 
# Write a function that takes a list of cities that are directly connected, and computes the total distance to fly between those cities:
# 
#     def total_distance(city_list):
#         ...


# your code goes here



print total_distance(["Austin", "Houston", "San Francisco"])
print total_distance(["Austin", "Dallas", "Los Angeles", "San Francisco"])


# Copyright 2008-2016, Enthought, Inc.  
# Use only permitted under license.  Copying, sharing, redistributing or other unauthorized use strictly prohibited.  
# http://www.enthought.com
