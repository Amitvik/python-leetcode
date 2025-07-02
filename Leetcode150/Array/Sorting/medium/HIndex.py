"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.



Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1


Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""
from operator import index
from typing import List


class Solution:

    def hIndexNlogN(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, citation in enumerate(citations):
            if citation < i + 1:
                return i
        return len(citations)

    def hIndex(self, citations: List[int]) -> int:
        n =  len(citations)
        bucket = [0] * (n + 1)
        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1

        total = 0
        for i in range(n, -1, -1):
            total += bucket[i]
            if total >= i:
                return i

        return 0


    def hIndexInefficient(self, citations: List[int]) -> int:
        citation_dict: dict[int: int] = {}  # {citation:count}
        citations_len = len(citations)

        for i, citation in enumerate(citations):
            if citation > citations_len:
                citation = citations_len


            citation_dict[citation] = citation_dict.get(citation, 0) + 1

        h_index = 0
        index = 0
        while index <= citations_len:
            accumulator = 0
            limit = index
            i = index
            while i <= citations_len:
                accumulator += citation_dict.get(i, 0)
                if accumulator >= limit:
                    h_index = max(h_index, limit)
                    break
                i += 1
            index+=1

        return h_index


    def main(self):

        print(self.hIndex(citations=[3, 0, 6, 1, 5]))
        print(self.hIndex(citations=[1, 3, 1]))
        print(self.hIndex([1]))
        print(self.hIndex([0, 0, 2]))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
