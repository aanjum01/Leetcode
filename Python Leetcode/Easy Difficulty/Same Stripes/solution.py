def is_same_stripes(matrix):
  same_diagonal_elements = {}
  
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      key = i - j
      same_diagonal_elements.setdefault(key, []).append(matrix[i][j])
	
    for key in same_diagonal_elements:
        print(same_diagonal_elements[key])
        values = same_diagonal_elements[key]
        
        if len(set(values)) != 1:
            return False


    return True
