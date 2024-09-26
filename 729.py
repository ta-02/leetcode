class MyCalendar:

    def __init__(self):
        self.booking = []

    def book(self, start: int, end: int) -> bool:
        for t in self.booking:
            if not (end <= t[0] or start >= t[1]):
                return False
        self.booking.append((start, end))
        return True
