ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# start
ft_list[1] = "world!"
ft_tuple = (ft_tuple[0], "Spain!")
ft_set.remove("tutu!")
ft_set.add("Malaga!")
ft_dict["Hello"] = "42Malaga!"
# end

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
