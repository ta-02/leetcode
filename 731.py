class MyCalendarTwo:

    def __init__(self):
        self.booking = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlap:
            if not (e <= start or end <= s):
                return False

        for s, e in self.booking:
            if not (e <= start or end <= s):
                max_start = max(s, start)
                min_end = min(end, e)
                self.overlap.append((max_start, min_end))

        self.booking.append((start, end))
        return True
