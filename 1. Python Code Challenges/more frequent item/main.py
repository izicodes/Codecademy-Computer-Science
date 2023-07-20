def more_frequent_item(my_list, item1, item2):
  freq1 = my_list.count(item1)
  freq2 = my_list.count(item2)

  if freq1 > freq2 or freq1 == freq2:
    return item1
  else:
    return item2


print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))