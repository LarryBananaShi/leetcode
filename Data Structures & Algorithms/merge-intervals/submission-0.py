class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # first, sort the intervals. If sorted, possible overlapping intervals will be next to eachother
        # next, given interval A and interval B next to eachother, there is an overlap if the lower of B <= limit of A
        # (part of interval B sit within or be merged with A)
        # the new interval is the maximum of the limit of A and B, with the lower being the lower of A
        # continue through entire list

        # ex. A is [1,2], B is [2, 4]
        # 2 <= 2. max(2, 4) = 4. new interval is [1, 4]

        # bucket sort, overly complicated?
        # max_val = 0
        # for interval in intervals:
        #     if interval[0] > max_val:
        #         max_val = interval[0]

        # buckets = [[] for _ in range(max_val + 1)]

        # for interval in intervals:
        #     buckets[interval[0]].append(interval)

        # sorted_buckets = []
        # for bucket in buckets:
        #     sorted_buckets.extend(bucket)

        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
            

        return merged
            