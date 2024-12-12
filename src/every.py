def every(any_list, predicate):

    result = True

    for el in any_list:
      
        result = predicate(el)


        if result == False:
            return result
        
    
    print("Result: ", result)
    
    return result