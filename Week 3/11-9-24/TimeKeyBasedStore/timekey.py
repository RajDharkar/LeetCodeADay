class TimeMap(object):

    def __init__(self):
        # Dictionary to store the key and list of (value, timestamp) tuples
        self.store = {}

    def set(self, key, value, timestamp):
        """
        Store the key with the value and timestamp.
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key, timestamp):
        """
        Retrieve the value at or before the given timestamp.
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store or not self.store[key]:
            return ""
        
        values = self.store[key]
        
        # Binary search for the largest timestamp less than or equal to the given timestamp
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return values[right][0] if right >= 0 else ""