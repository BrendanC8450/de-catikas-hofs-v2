def find(any_list, func):

    for el in any_list:
        # print("Before: ", el)
        if func(el):
            # print("El in if", el)
            return el
    # print(el)
    return el
