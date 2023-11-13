class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.order = []
        self.capacity = capacity
        self.page_hits = 0
        self.page_faults = 0

    def refer(self, page_number):
        if page_number in self.cache:
            # Page hit: Move the page to the end to mark it as most recently used
            self.order.remove(page_number)
            self.order.append(page_number)
            self.page_hits += 1
        else:
            # Page fault: Check if the cache is full
            if len(self.cache) >= self.capacity:
                # Remove the least recently used page (first item in order list)
                removed_page = self.order.pop(0)
                del self.cache[removed_page]
            # Add the new page to the cache and order list
            self.cache[page_number] = None
            self.order.append(page_number)
            self.page_faults += 1

    def display_cache_contents(self):
        print("LRU Cache Contents:", end=" ")
        for page_number in self.order:
            print(page_number, end=" ")
        print("\n")

    def display_page_counters(self):
        print(f"Page Hits: {self.page_hits}")
        print(f"Page Faults: {self.page_faults}")


if __name__ == "__main__":
    # User input for pages and cache size
    pages = list(map(int, input("Enter the sequence of page references (space-separated): ").split()))
    cache_size = int(input("Enter the cache size: "))

    lru_cache = LRUCache(cache_size)

    for page_number in pages:
        lru_cache.refer(page_number)
        lru_cache.display_cache_contents()

    lru_cache.display_page_counters()
