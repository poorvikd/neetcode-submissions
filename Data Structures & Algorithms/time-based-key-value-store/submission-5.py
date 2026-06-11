class TimeMap:

    def __init__(self):
        self.db = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:    
        self.db[key].append([value,timestamp])
        return

    def get(self, key: str, timestamp: int) -> str:
        leftmost_ts_to_timestamp = -1
        arr = self.db[key]
        n = len(arr)
        l,r = 0,n-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid][1] > timestamp:
                r = mid-1
            elif arr[mid][1] < timestamp:
                leftmost_ts_to_timestamp = max(leftmost_ts_to_timestamp, mid)
                l = mid+1
            else:
                return arr[mid][0]
        
        return arr[leftmost_ts_to_timestamp][0] if leftmost_ts_to_timestamp != -1 else ""
