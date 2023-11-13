class Page:
    def __init__(self, page_number):
        self.page_number = page_number
        self.referenced = 0  # Counter to keep track of page references

def fifo(pages, page_frames):
    page_table = {}  # Dictionary to store the pages in page frames
    page_order = []  # List to maintain the order of pages in the frames

    page_faults = 0

    for page_number in pages:
        if page_number not in page_table:
            page_faults += 1

            if len(page_table) == page_frames:
                removed_page = page_order.pop(0)
                del page_table[removed_page]

            page_table[page_number] = Page(page_number)
            page_order.append(page_number)

    return page_faults

if __name__ == "__main__":
    # Example pages and page frames
    pages = [1, 2, 3, 4, 1, 5, 6, 2, 7, 8, 7, 8, 9, 3, 9, 5, 1]
    page_frames = 3

    total_page_faults = fifo(pages, page_frames)

    print(f"Total Page Faults using FIFO: {total_page_faults}")
