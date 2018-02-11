# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        CNl1 = l1
        CNl2 = l2
        l3 = ListNode(0)
        CNl3 = l3
        PNl3 = l3
        Pnum = 0
        while CNl1 != None or CNl2 != None:
            if CNl1 == None:
                num = CNl2.val + Pnum
                CNl3.val = num%10
                Pnum = num//10
                CNl2 = CNl2.next
            elif CNl2 == None:
                num = CNl1.val + Pnum
                CNl3.val = num%10
                Pnum = num//10
                CNl1 = CNl1.next
            else:
                CNl3.val = (CNl1.val + CNl2.val + Pnum)%10
                Pnum = (CNl1.val + CNl2.val + Pnum)//10
                CNl1 = CNl1.next
                CNl2 = CNl2.next
            CNl3 = ListNode(0)
            if CNl1 == None and CNl2 == None:
                if Pnum == 0:
                    pass
                else:
                    CNl3.val = 1
                    PNl3.next = CNl3
            else:
                PNl3.next = CNl3
                PNl3 = CNl3
        return l3
