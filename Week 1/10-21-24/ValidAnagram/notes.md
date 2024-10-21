## Problem Understanding
- **Summary**: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
- **Input**: Two strings, 't', and 's'
- **Output**: True or False

## Approach
- **Initial Thoughts**: Seems like a typical map problem
- **Approach Taken**: Mapped each letter to amount of times occured, and then checked if the maps were the same

<!-- ## Approach 2
- **Initial Thoughts**: 
- **Approach Taken**: 
- **Why This Approach**:  -->

## Challenges
- **Obstacles Faced**: Testing my inputs, installed the LeetCode extension. 
<br> Edit: That never ended up working but its okay.
- **Edge Cases**: None

## Optimization
- **Time Complexity**: O(n), O(1) * n * 2
- **Space Complexity**: O(n), two sets with size of n

## Alternative Solutions
- Sorting and checking if they are equal, however this is slow.
- In hindsight, using an array would have been better, because there are only 26 values and there is no reason to hash them. 

## Key Takeaways
- Maps are nice for string problems, especially for a counter.

## Additional Resources
- N/A
