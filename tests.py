from ValidAnagram import Solution

def str():
    """Returns a string input from the user."""
    return input()

def int():
    """Returns an integer input from the user."""
    return int(input())

def list_int():
    """Returns a list of integers from space-separated input."""
    return list(map(int, input().split()))

# Test function template
def test_solution():
    solution = Solution()

if __name__ == "__main__":
    test_solution()
