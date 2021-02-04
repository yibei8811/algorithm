# $为Tree尾节点
# 否则需要二叉树是有序的并且避免重复节点
# eg:[3,3],第一个3为root节点
# 第二个3无法区分是左节点或右节点
# 对于前序 [1,2,3] 存在
# [  1
#   2 3 ]
#   or
# [ 1
#    2
#     3 ]
# 对于后序 [1,2,3] 同上类似
# 对于中序  [1,2,3] 存在
# [  2
#   1 3 ]
#   or
# [ 1
#    2
#     3 ]
#   or
# [ 3
#    2
#     1 ]
# 一个序列无法确定唯一树的序列化


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # TODO 032/之字形
    def show(self):
        except_count = 1
        next_line_node_count = 0
        queue = [self]
        while len(queue) > 0:
            except_count -= 1
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left is not None:
                next_line_node_count += 1
                queue.append(node.left)
            if node.right is not None:
                next_line_node_count += 1
                queue.append(node.right)
            if except_count == 0:
                print()
                except_count = next_line_node_count
                next_line_node_count = 0

    def serialize_with_tail(self):
        queue = [self]
        result = []
        while len(queue) > 0:
            node = queue.pop(0)
            if node == '$':
                result.append('$')
                continue
            result.append(node.val)
            queue.append('$' if node.left is None else node.left)
            queue.append('$' if node.right is None else node.right)
        return result

    @staticmethod
    def deserialize_with_tail(lst):
        head = Tree(lst.pop(0))
        queue = [head]
        while len(queue) > 0:
            node = queue.pop(0)
            left_val = lst.pop(0)
            rigth_val = lst.pop(0)
            if left_val != '$':
                node.left = Tree(left_val)
                queue.append(node.left)
            if rigth_val != '$':
                node.right = Tree(rigth_val)
                queue.append(node.right)
        return head
