class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:

	def reverseLLUsingStack(self, head):
		stack, temp = [], head
		
		while temp:
			stack.append(temp)
			temp = temp.next
		head = temp = stack.pop()
	
		while len(stack) > 0:
			temp.next = stack.pop()
			temp = temp.next

		temp.next = None
		return head

if __name__ == "__main__":
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
	obj = Solution()
	head = obj.reverseLLUsingStack(head)
	while head:
		print(head.val, end=' ')
		head = head.next