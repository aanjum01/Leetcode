def weakest_strong_link(strength):
  
  m = len(strength) # number of rows
  n = len(strength[0]) #number of columns
  
  min_rows = [0] * m
  
  max_cols = [0] * n
  
  for i in range(m):
    min_rows[i] = min(strength[i])
  
  for j in range(n):
    current_max = 0
    for i in range(m):
      current_max = max(current_max, strength[i][j])
    max_cols[j] = current_max
  
  for i in range(m):
    for j in range(n):
      if strength[i][j] == min_rows[i] and strength[i][j] == max_cols[j]:
        return strength[i][j]
        
  return -1
      