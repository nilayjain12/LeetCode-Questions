class LRUCache:
    def __init__(self, capacity: int):
        self.dict_queue = {}  # Stores key-value pairs
        self.queue = deque()  # Stores key order for LRU tracking
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dict_queue:
            # Move key to most recently used position
            self.queue.remove(key)
            self.queue.append(key)
            return self.dict_queue[key]
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        if key in self.dict_queue:
            # Update the value
            self.dict_queue[key] = value
            # Move key to most recently used position
            self.queue.remove(key)
            self.queue.append(key)
        else:
            if len(self.dict_queue) >= self.capacity:
                # Evict the least recently used item
                lru_key = self.queue.popleft()
                del self.dict_queue[lru_key]

            # Insert new key-value pair
            self.dict_queue[key] = value
            self.queue.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)