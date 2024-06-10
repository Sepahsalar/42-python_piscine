def NULL_not_found(object: any) -> int:

    if object is None:
        print("Nothing:", object, type(object))
    elif type(object) is float and object != object:
        print("Cheese:", object, type(object))
    elif type(object) is int and object == 0:
        print("Zero:", object, type(object))
    elif type(object) is str and object == '':
        print("Empty:", object, type(object))
    elif type(object) is bool and not object:
        print("Fake:", object, type(object))
    else:
        print("Type not found")
        return 1
    return 0
