class MemoryBlock:
    def __init__(self, size, allocated=False, process_id=None):
        self.size = size
        self.allocated = allocated
        self.process_id = process_id

def next_fit(memory_blocks, process_size):
    start_index = 0
    current_index = start_index

    while True:
        block = memory_blocks[current_index]
        if not block.allocated and block.size >= process_size:
            block.allocated = True
            block.process_id = "P"  # You can use the actual process ID here
            return True

        current_index = (current_index + 1) % len(memory_blocks)

        # If we have traversed the entire list without finding a suitable block, break the loop
        if current_index == start_index:
            break

    return False

def display_memory_status(memory_blocks):
    print("Memory Block\tSize\tStatus\tProcess ID")
    for i, block in enumerate(memory_blocks, start=1):
        print(f"{i}\t\t\t{block.size}\t{'Allocated' if block.allocated else 'Free'}\t{block.process_id}")

if __name__ == "__main__":
    # Example memory blocks
    memory_blocks = [
        MemoryBlock(100),
        MemoryBlock(50),
        MemoryBlock(200),
        MemoryBlock(75),
        MemoryBlock(300),
    ]

    # Example processes with their sizes
    processes = [30, 100, 75, 130]

    # Allocate memory for each process using Next Fit
    for process_size in processes:
        success = next_fit(memory_blocks, process_size)
        if success:
            print(f"Allocated {process_size} units to process.")
        else:
            print(f"Failed to allocate {process_size} units. No suitable block found.")

    # Display final memory status
    display_memory_status(memory_blocks)
