def all_thing_is_obj(object: any) -> int:

    object_type = str(type(object))

    match object_type:
        case "<class 'list'>":
            print("List : " + object_type)
        case "<class 'tuple'>":
            print("Tuple : " + object_type)
        case "<class 'set'>":
            print("Set : " + object_type)
        case "<class 'dict'>":
            print("Dict : " + object_type)
        case "<class 'str'>":
            print(object + " is in the kitchen : " + object_type)
        case _:
            print("Type not found")

    return 42

# tester.py file
# from find_ft_type import all_thing_is_obj

# ft_list = ["Hello", "tata!"]
# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello" : "titi!"}

# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("Brian")
# all_thing_is_obj("Toto")
# print(all_thing_is_obj(10))

# Expected oputput
# $>python tester.py | cat -e
# List : <class 'list'>$
# Tuple : <class 'tuple'>$
# Set : <class 'set'>$
# Dict : <class 'dict'>$
# Brian is in the kitchen : <class 'str'>$
# Toto is in the kitchen : <class 'str'>$
# Type not found$
# 42$
# $>