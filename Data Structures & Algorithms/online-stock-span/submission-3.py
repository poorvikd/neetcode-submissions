class StockSpanner:

    def __init__(self):
        self.prices = [] #[price, curr_span, blockedByIdx, curr_idx]

    def next(self, price: int) -> int:
        span = 1
        if len(self.prices) == 0:
            self.prices.append([price,span,-1,0])
        else:
            top = self.prices[-1]
            span = 1
            while price >= top[0]:
                span += top[1]
                if top[2] < 0:
                    top[3] = -1
                    break
                top = self.prices[top[2]]

            self.prices.append([price,span,top[3],len(self.prices)])
        return span
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)