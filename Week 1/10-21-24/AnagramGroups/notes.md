## Problem Understanding
- **Summary**: Given an array of strings str, group all the anagrams together in sublists.

## Approach
- **Initial Thoughts**: Probobly some sort of hashset, with a similar idea like that last problem. 
- **Approach Taken**: HashSet of HashMap(s) due to its time complexity.

## Approach 2
- **Approach Taken**: Sort the strings and check if they are already seen
- **Why This Approach**:  Realized you can't hash a hashset lol

## Challenges
- **Obstacles Faced**: Needed to use a second approach
- **Edge Cases**: None

## Optimization
- **Time Complexity**: O(n log m), n strings and we sort it m times.
- **Space Complexity**: O(n), only one dictionary

## Alternative Solutions
- Brute forcing
- Some sort of weird hashmap impl

## Key Takeaways
- You can't hash a dictionary

## Additional Resources
- N/A
