"""
My Calendar I (Medium)
Solved in O(n) time complexity and O(n) space complexity
"""

class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        if len(self.events) == 0:
            self.events.append([start, end])
            return True
        
        for s, e in self.events:
            if start < e and s < end:
                return False

        self.events.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)