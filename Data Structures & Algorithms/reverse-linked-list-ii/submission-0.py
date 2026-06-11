# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
    
        count = 1
        ptr = head
        prev = None
        while ptr:
            print(count)
            if count >= left and count < right:
                print("rotating")
                nxt = ptr.next
                ptr.next = nxt.next
                if prev == None:
                    nxt.next = head
                    head = nxt
                else:
                    nxt.next = prev.next
                    prev.next = nxt
            else:
                prev = ptr
                ptr = ptr.next
            count += 1
        
        
        
        return head