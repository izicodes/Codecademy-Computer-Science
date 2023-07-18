def append_sum(my_list):
  for i in range(3):
    last1 = my_list[-1]
    last2 = my_list[-2]
    num = last1 + last2
    my_list.append(num)

  return my_list  

print(append_sum([1, 1, 2]))