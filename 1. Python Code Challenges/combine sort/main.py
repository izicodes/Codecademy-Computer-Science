def combine_sort(list1, list2):
  newList = list1 + list2
  newList.sort()
  return newList


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))