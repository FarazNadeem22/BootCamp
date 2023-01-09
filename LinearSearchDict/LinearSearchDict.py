def linear_search_dictionary(dict_, target):
    for key, value in dict_.items():
        #print(key, value)
        if value == target:
            print(f"{target} found at key {key}")
            return key
    print(f"{target} is not in the dictionary")
    return -1


"""Driver"""
my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
_ = linear_search_dictionary(my_dictionary, 5)
_ = linear_search_dictionary(my_dictionary, 3)
_ = linear_search_dictionary(my_dictionary, 8)
