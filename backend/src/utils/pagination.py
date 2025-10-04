def paginate(query, page, page_size):
    """
    Paginates the given query.

    Args:
        query: The query to paginate.
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        A tuple containing the paginated items and the total count.
    """
    total_count = query.count()
    items = query.offset((page - 1) * page_size).limit(page_size).all()
    return items, total_count

def get_total_pages(total_count, page_size):
    """
    Calculates the total number of pages.

    Args:
        total_count (int): The total number of items.
        page_size (int): The number of items per page.

    Returns:
        int: The total number of pages.
    """
    if page_size <= 0:
        return 0
    return (total_count + page_size - 1) // page_size  # Ceiling division
