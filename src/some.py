def some(any_list, predicate):

    result = False

    for el in any_list: 
 
        result = predicate(el)        

        if result == True:
            return result
    
    return result
