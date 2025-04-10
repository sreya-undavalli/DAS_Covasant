"""
flatten(lst)        Flattens the list 
                    ie input = [1,2,3, [1,2,3,[3,4],2]]
                    output = [1,2,3,1,2,3,3,4,2]
                    """
flattened_list=[]
def flatten(lst):
    for item in lst:
        if type(item) is list:
            flatten(item)
        else:
            flattened_list.append(item)
    return flattened_list

lst = [1,2,3, [1,2,3,[3,4],2]]
print(flatten(lst))


DAY 3 -Q2
lst = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
def convert (lst):
    for item in lst:
        if type(item) is list:
            convert(item)
             
        else:
            lst[lst.index(item)]=[int(x) for x in (item[1:-1:2])]
    return lst
             
print(convert(lst))
