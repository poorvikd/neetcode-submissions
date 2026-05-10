# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        db = []
        heapq.heapify(db)
        count = 0
        for i,ll in enumerate(lists):
            heapq.heappush(db, (ll.val,count,ll))
            count += 1
        
        head = None
        ptr = None
        while len(db) != 0:
            val,i,node = heapq.heappop(db)
            if head == None:
                head = node
                ptr = head
            else:
                ptr.next = node
                ptr = ptr.next
            if node.next != None:
                node = node.next
                heapq.heappush(db,(node.val,count,node))
                count+=1
        return head
        
        