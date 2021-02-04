class ListNode:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        result = [self.data]
        p = self
        while p.next_node is not None:
            p = p.next_node
            result.append(p.data)
        return result.__str__()

    def __len__(self):
        count = 1
        node = self
        while node.next_node is not None:
            node = node.next_node
            count += 1
        return count
