

'''
mark_dict -> **kwargs
'''
def marks(**mark_dict):
    # kwargs is a dictionary with all the key value pairs which were passed to marks 
    print(mark_dict)
    print(type(mark_dict))
    for item in mark_dict.keys():
        print(f"The marks of {item} is {mark_dict[item]}")

marks(John=34, Jane=54, Jack=34, Dean=90, Mark=45)