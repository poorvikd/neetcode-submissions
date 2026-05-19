class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_heapq = []
        heapq.heapify(trip_heapq)
        for c,x,y in trips:
            heapq.heappush(trip_heapq,(x,y,c))
        qu = deque()
        dist = 0
        current_cap = 0
        while qu or trip_heapq:
            while len(qu)>0 and dist == qu[0][1]:
                x,y,c = qu.pop()
                current_cap -= c
                print(f"At dist {x}, current cap {current_cap}")

            while len(trip_heapq) > 0 and dist == trip_heapq[0][0]:
                print(f"Considering pooling {trip_heapq[0]}, current_cap : {current_cap}")
                x,y,c = heapq.heappop(trip_heapq)
                if current_cap + c <= capacity:
                    current_cap += c
                    qu.append((x,y,c))
                    print(f"At dist {x}, current cap {current_cap}")
                else:
                    return False

            dist += 1

        return True