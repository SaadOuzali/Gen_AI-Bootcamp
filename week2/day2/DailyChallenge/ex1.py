import math


class Pagination:
    def __init__(self, items: list = None, page_size=10):
        self.page_size = page_size
        self.items = items if items is not None else []
        self.current_page = 0
        self.total_number_of_pages = (
            math.ceil(len(self.items) / self.page_size) if self.items else 0
        )

    def get_visible_items(self):
        start = self.current_page * self.page_size
        end = self.page_size + start
        return self.items[start:end]

    def go_to_page(self, page_num):
        if 1 <= page_num <= self.total_number_of_pages:
            self.current_page = page_num - 1
            start = self.current_page * self.page_size
            end = self.page_size + start
            return self.items[start:end]
        else:
            raise ValueError("page num is out of range ")

    def first_page(self):
        self.current_page = 0
        return self

    def last_page(self):
        if self.total_number_of_pages > 0:
            self.current_page = self.total_number_of_pages - 1
            return self

    def next_page(self):
        if self.current_page < self.total_number_of_pages - 1:
            self.current_page += 1
            return self

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            return self

    def __str__(self):

        visible_items = self.get_visible_items()
        if not visible_items:
            return "No items to display."

        items_str = "\n".join(str(item) for item in visible_items)
        return f"Page {self.current_idx + 1}/{self.total_pages}:\n{items_str}"
