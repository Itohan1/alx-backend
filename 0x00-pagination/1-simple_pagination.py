#!/usr/bin/env python3
"""
   Write a function named index_range
   that takes two integer arguments
   page and page_size.

   The function should return a tuple
   of size two containing a start
   index and an end index corresponding
   to the range of indexes to return
   in a list for those particular
   pagination parameters.

   Page numbers are 1-indexed,
   i.e. the first page is page 1.
"""
from typing import Tuple
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
           Implement a method named get_page
           that takes two integer arguments page
           with default value 1 and page_size
           with default value 10
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = list(csv.reader(open('Popular_Baby_Names.csv')))
        result = self.index_range(page, page_size)
        instance = [i for i in data[result[0]:result[1]]]
        return instance

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Start and end indexes"""

        start_index = (page - 1) * page_size
        end_index = page_size + start_index
        return (start_index, end_index)
