def another_one(digits):
  i = len(digits) - 1
  
  while i >= 0 and digits[i] == 9:
    digits[i] = 0
    i -= 1
    
  if i >= 0:
    digits[i] += 1
    return digits
  else:
    new_list = [0] * (len(digits) + 1)
    new_list[0] = 1
    return new_list
  
  return len(digits)