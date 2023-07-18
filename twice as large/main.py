def twice_as_large(num1,num2):
  num2 = num2 * 2
  if num1 > num2:
    return True
  else:
    return False 
  
print(twice_as_large(10, 5))
# should print False

print(twice_as_large(11, 5))
# should print True  