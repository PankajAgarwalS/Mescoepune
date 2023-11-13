def optimal_page_replacement(pages, page_frames):
    page_faults = 0
    page_table = {}  # Dictionary to store the pages in page frames

    for i, page in enumerate(pages):
        if page not in page_table:
            page_faults += 1

            if len(page_table) < page_frames:
                page_table[page] = i  # Store the index of the next reference for each page
            else:
                # Find the page in page frames with the maximum index of the next reference
                page_to_replace = min(page_table, key=page_table.get)
                del page_table[page_to_replace]
                page_table[page] = i

    return page_faults

if __name__ == "__main__":
    # Example pages and page frames
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    page_frames = 3

    total_page_faults = optimal_page_replacement(pages, page_frames)

    print(f"Total Page Faults using Optimal: {total_page_faults}")
