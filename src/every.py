def every(any_list, func):

    result = True

    for el in any_list:
      
        result = func(el)

        if result == False:
            return result
        
    
    print("Result: ", result)
    
    return result