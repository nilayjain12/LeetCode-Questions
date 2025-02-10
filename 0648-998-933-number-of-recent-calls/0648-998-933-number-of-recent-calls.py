class RecentCounter:

    def __init__(self):
        # initialize a list to update the requests that comes on time t
        self.requests = []
        
    def ping(self, t: int) -> int:
        # initialize counter for counting requests
        counter = 0
        self.requests.append(t)

        for req in self.requests:
            if req >= t-3000 and req <=t:
                counter += 1
        
        return counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)