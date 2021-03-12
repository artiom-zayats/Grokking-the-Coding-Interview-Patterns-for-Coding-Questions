'''
Problem Statement 
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
'''

#mycode
def non_repeat_substring_slow(str):
  seen = {}
  start = 0
  result = float("-inf")
  for end in range(len(str)):
    right_ch = str[end]
    if right_ch not in seen:
      seen[right_ch] = 0
    seen[right_ch]+=1

    def condition(dic):
      for v in dic.values():
        if v > 1:
          return False
      return True

    while not condition(seen):
      left_ch = str[start]
      seen[left_ch]-=1
      if seen[left_ch] == 0:
        del seen[left_ch]
      start+=1
    result = max(result,end-start+1)

  if result == float("-inf"):
    return 0
  return result

#mycode
def non_repeat_substring(str):
  seen = {}
  start = 0
  result = float("-inf")
  for end in range(len(str)):
    right_ch = str[end]

    if right_ch in seen:
      last_seen = seen[right_ch]
      start = max(start,last_seen+1)
    
    seen[right_ch] = end
    result = max(result,end-start+1)


  if result == float("-inf"):
    return 0
  return result

#answer
def non_repeat_substring2(str):
  window_start = 0
  max_length = 0
  char_index_map = {}

  # try to extend the range [windowStart, windowEnd]
  for window_end in range(len(str)):
    right_char = str[window_end]
    # if the map already contains the 'right_char', shrink the window from the beginning so that
    # we have only one occurrence of 'right_char'
    if right_char in char_index_map:
      # this is tricky; in the current window, we will not have any 'right_char' after its previous index
      # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
      window_start = max(window_start, char_index_map[right_char] + 1)
    # insert the 'right_char' into the map
    char_index_map[right_char] = window_end
    # remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)
  return max_length


def main():

  for i in ["aabccbb","abbbb","abccde"]:
    print("Length of the longest substring:",non_repeat_substring(i),"=?",non_repeat_substring2(i))


main()


'''
Time Complexity 
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input string.

Space Complexity 
The space complexity of the algorithm will be O(K) where KK is the number of distinct characters in the input string. 
This also means K<=N, because in the worst case, the whole string might not have any repeating character so the entire string will be added to the HashMap. 
Having said that, since we can expect a fixed set of characters in the input string (e.g., 26 for English letters), we can say that the algorithm runs in fixed space O(1); in this case, we can use a fixed-size array instead of the HashMap.
'''