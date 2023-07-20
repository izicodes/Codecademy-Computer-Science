def double_index(my_list, index):
  if index >= len(my_list):
    return my_list
  else:
    my_new_list = my_list[0:index]

  my_new_list.append(my_list[index]*2)
  my_new_list = my_new_list + my_list[index+1:]
  return my_new_list

print(double_index([3, 8, -10, 12], 2))