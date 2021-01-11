from public.tree import Tree

lst = ['1', '2', '3', '4', '$', '5', '6', '$', '$', '$', '$', '$', '$']
tree = Tree.deserialize_with_tail(lst)
tree.show()
print(tree.serialize_with_tail())

