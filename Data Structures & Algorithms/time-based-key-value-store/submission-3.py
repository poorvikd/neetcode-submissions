class TimeMap:

    def __init__(self):
        self.timesvaluedb = {}
        self.timesdb = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timesvaluedb[f"{key}-{timestamp}"] = value
        self.timesdb[key].append(timestamp)        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timesdb or len(self.timesdb[key]) == 0:
            return ""
        timeset = self.timesdb[key]
        l,r = 0,len(timeset)-1
        final_timestamp = timeset[0]
        while l<=r:
            print(timeset[l],timeset[r])
            mid = (l+r) // 2
            if timeset[mid] > timestamp:
                r = mid-1
            elif timeset[mid] < timestamp:
                final_timestamp = timeset[mid]
                l = mid+1
            else:
                final_timestamp = timeset[mid]
                break
        if final_timestamp > timestamp:
            return ""
        return self.timesvaluedb[f"{key}-{final_timestamp}"]
