"""
FelipedelosH
2026
"""
class Paginator:
    def __init__(self, total, page, page_size):
        self.total = total
        self.page = page
        self.page_size = page_size

    @property
    def total_pages(self):
        if self.page_size <= 0:
            return 0
        return (self.total + self.page_size - 1) // self.page_size

    @property
    def has_next(self):
        return self.page < self.total_pages

    @property
    def has_prev(self):
        return self.page > 1

    def to_dict(self):
        return {
            "page": self.page,
            "page_size": self.page_size,
            "total": self.total,
            "total_pages": self.total_pages,
            "has_next": self.has_next,
            "has_prev": self.has_prev
        }