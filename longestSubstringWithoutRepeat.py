# time = O(N)
# space = O(N) => space complexity of map

def lengthOfLongestSubstring(s):
    string_map = {}
    n = len(s)
    left = 0
    right = 0
    substring_length = 0
    while(left < n and right < n):
        element = s[right]
        if element in string_map:
            left = max(left,string_map[element] + 1)
        string_map[element] = right
        substring_length = max(substring_length, right - left + 1)
        right = right + 1
    print(substring_length)



s = "pwwkew"
lengthOfLongestSubstring(s)
