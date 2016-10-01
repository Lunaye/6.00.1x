def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    new_list = []
    for item in aList:
        if type(item) == type([]):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)
    return new_list
