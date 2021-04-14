'''
Problem Statement 
Given an array of numbers sorted in ascending order, 
find the element in the array that has the minimum difference with the given ‘key’.

Example 1:

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 

Example 2:

Input: [4, 6, 10], key = 4
Output: 4

Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: 10

Example 4:

Input: [4, 6, 10], key = 17
Output: 10
'''

#mycode

def search_min_diff_element(arr, key):
  #TODO my code
  l,r = 0,len(arr)-1
  mn = (float("inf"),-1)
  while l<=r:
    mid = (l+r)//2
    diff = arr[mid]-key
    if abs(diff) < mn[0]:
      mn = abs(diff),mid
    if diff == 0:
      break
    if diff < 0 :
      l = mid +1
    else:
      r = mid - 1

  return arr[mn[1]]

def search_min_diff_element2(arr, key):
  # TODO: Write your code here
  if key <= arr[0]:
    return arr[0]
  if key >= arr[-1]:
    return arr[-1]
  
  start, end = 0, len(arr)-1
  while start <= end:
    mid = (start + end) //2

    if arr[mid] < key:
      start = mid + 1
    elif arr[mid] > key:
      end = mid - 1
    else:
      return arr[mid]
    
    
  if abs(arr[start] - key) >= abs(arr[end]-key):
    return arr[end]
  else:
    return arr[start]



def main():
  print("minde")
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))
  print(search_min_diff_element(sorted([-1, -3, -8, -10, -15]), 12))
  print(search_min_diff_element(sorted([1, 3, 8, 10, 15]), -12))



main()


#answer
def search_min_diff_element(arr, key):
  if key < arr[0]:
    return arr[0]
  n = len(arr)
  if key > arr[n - 1]:
    return arr[n - 1]

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < arr[mid]:
      end = mid - 1
    elif key > arr[mid]:
      start = mid + 1
    else:
      return arr[mid]

  # at the end of the while loop, 'start == end+1'
  # we are not able to find the element in the given array
  # return the element which is closest to the 'key'
  if (arr[start] - key) < (key - arr[end]):
    return arr[start]
  return arr[end]


def main():
  print("corect")
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))
  print(search_min_diff_element(sorted([-1, -3, -8, -10, -15]), 12))
  print(search_min_diff_element(sorted([1, 3, 8, 10, 15]), -12))


main()



'''
Time complexity 
Since, we are reducing the search range by half at every step, 
this means the time complexity of our algorithm will be O(logN) 
where ‘N’ is the total elements in the given array.

Space complexity 
The algorithm runs in constant space O(1).
'''