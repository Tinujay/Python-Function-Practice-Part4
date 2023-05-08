#1. Write a Python function called max_num()to find the maximum of three numbers.
def max_num(num1, num2, num3):
    return max(num1, num2, num3)

print(max_num(5, 2, 9))

#2. Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(nums):
    total = 1  #when multiplying with the first number to 1, the                     result will be the number itself
    for num in nums:
        total *= num
    return total

print(mult_list([2, 1, 3, 5]))

#3. Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return string[::-1]

print(rev_string('hello'))

#4. Write a Python function called num_within() to check whether a number falls in a given range. The function accepts the number, beginning of range, and end of range (inclusive) as arguments. 
#don't really understand?
def num_within(x,a,b):
  return x in range(a,b+1)

#5. Write a Python function called pascal() that prints out the first n rows of Pascal's triangle. The function accepts the number n, the number of rows to print.
#don't really understand, need to look over 
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)