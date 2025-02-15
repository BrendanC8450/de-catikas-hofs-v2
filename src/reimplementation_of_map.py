"""
Purpose: Reimplement the function, map

Inputs:
- A function, which will be invoked with each element in turn and 
return a new value.
- A collection, which the function can map over.

Return:
Same data type as collection passed in.

Limit: Only accepts lists, sets or tuples
"""


def reimplementation_of_map(collection, func):

    # Change collection to a list
    if type(collection) is not list:
        collection = list(collection)
    
    for idx, el in enumerate(collection):
        
        collection[idx] = func(el)

    return collection