ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}



ft_list[1] = 'World' #as you would expect

temp_list = list(ft_tuple) #tuples are immutable, so change to list, and go back to tuple 
temp_list[1] = 'France'
ft_tuple = tuple(temp_list)

ft_set.remove('tutu!') #no direct change of value possible, so remove and readd
ft_set.add('Paris!')

ft_dict['Hello'] = '42Paris!' #typical dictionary/map



print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

