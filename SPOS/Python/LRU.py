from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def refer(self, page_number):
        if page_number in self.cache:
            # Move the page to the end to mark it as most recently used
            self.cache.move_to_end(page_number)
        else:
            # Check if the cache is full
            if len(self.cache) >= self.capacity:
                # Remove the least recently used page (first item in OrderedDict)
                self.cache.popitem(last=False)
            # Add the new page to the cache
            self.cache[page_number] = None

    def display_cache_contents(self):
        print("LRU Cache Contents:")
        for page_number in self.cache:
            print(page_number, end=" ")
        print("\n")

if __name__ == "__main__":
    # Example pages and cache size
    pages = [1, 2, 3, 4, 1, 5, 6, 2, 7, 8, 7, 8, 9, 3, 9, 5, 1]
    cache_size = 3

    lru_cache = LRUCache(cache_size)

    for page_number in pages:
        lru_cache.refer(page_number)
        lru_cache.display_cache_contents()
