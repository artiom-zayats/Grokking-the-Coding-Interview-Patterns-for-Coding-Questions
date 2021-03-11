'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''


#mycode
def longest_substring_with_k_distinct(arr, k):
  start = 0
  mx_len = float("-inf")
  dic = dict()
  ## sliding window
  for end in range(len(arr)):
    right_char = arr[end]
    if right_char not in dic:
      dic[right_char] = 0
    dic[right_char] += 1
    ##shrink the window
    while len(dic) > k:
      left_char = arr[start]
      dic[left_char] -= 1
      if dic[left_char] == 0:
        del dic[left_char]
      start += 1
    mx_len = max(mx_len,end-start+1)

  if mx_len == float("-inf"):
    return 0
  
  return mx_len



def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)),4)
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)),2)
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)),5)


main()


'''
Time Complexity 

Space Complexity
'''