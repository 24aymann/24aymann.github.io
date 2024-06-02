class Node:
    def __init__(self, value, color='RED'):
        """
        Initializes a new node with a specific value and color, defaulting to RED.
        Also initializes the left, right, and parent node links as None.
        """
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        """
        Initializes a new red-black tree by setting the root to None and the size to 0.
        """
        self.root = None
        self.size = 0

    def add(self, value):
        """
        Adds a value to the red-black tree. If the value already exists, the function exits without making changes.
        If the tree is empty, inserts a new black node as the root. Otherwise, inserts a red node
        and then adjusts the tree to correct red-black properties violations.
        """
        if self.contains(value):
            return False

        if self.root is None:
            self.root = Node(value, 'BLACK')
            self.size += 1
            return
        current = self.root
        parent = None
        while current is not None:
            parent = current
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return  # Value already exists, no need to add
        new_node = Node(value)
        new_node.parent = parent
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        self.fix_red_red_violation(new_node)
        self.size += 1

    def fix_red_red_violation(self, node):
        """
        Fixes violations of the red-black properties caused after insertion.
        Colors are adjusted and necessary rotations are performed to maintain the tree's balance.
        """
        while node != self.root and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'BLACK'

    def left_rotate(self, node):
        """
        Performs a left rotation on a given node, reassigning the node's links, its right child,
        and the parent to maintain the order of the binary search tree.
        """
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        """
        Performs a right rotation on a given node, reassigning the node's links, its left child,
        and the parent to maintain the order of the binary search tree.
        """
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def contains(self, value):
        """
        Checks if a specific value exists in the red-black tree.
        Utilizes a recursive helper method to search through the sub-trees.
        """
        return self._contains_helper(self.root, value)

    def _contains_helper(self, node, value):
        if node is None:
            return False
        if value < node.value:
            return self._contains_helper(node.left, value)
        elif value > node.value:
            return self._contains_helper(node.right, value)
        else:
            return True

    def atIndex(self, index):
        """
        Returns the value of the node at the given index, using an in-order traversal of the tree.
        This method considers the size of the left subtree to determine the relative position of the index.
        """
        return self._at_index_helper(self.root, index)

    def _at_index_helper(self, node, index):
        """
        Recursive helper method to find the value of the node at a specific index.
        Utilizes the size of the left subtree to navigate through the tree.
        """
        if node is None:
            return None
        left_size = self._size(node.left)
        if index == left_size:
            return node.value
        elif index < left_size:
            return self._at_index_helper(node.left, index)
        else:
            return self._at_index_helper(node.right, index - left_size - 1)

    def _size(self, node):
        """
        Calculates the total number of nodes in a subtree, including the current node.
        """
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def length(self):
        """
        Returns the size of the tree, i.e., the total number of nodes.
        """
        return self.size

    def remove(self, value):
        """
        Removes a node with a specific value from the tree. If the node has two children,
        it finds the successor to replace it and then removes the successor node.
        """
        node = self._find_node(value)
        if node is None:
            return
        self._remove_node(node)
        self.size -= 1

    def _find_node(self, value):
        """
        Finds and returns the node containing the given value.
        If the value does not exist in the tree, returns None.
        """
        current = self.root
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current
        return None

    def _remove_node(self, node):
        """
        Removes the node from the tree. If the node to be removed has two children,
        this method uses the successor to replace the node's value and then removes the successor.
        It also handles fixing red-black properties violations after removal.
        """
        if node.left is not None and node.right is not None:
            successor = self._min_value_node(node.right)
            node.value = successor.value
            node = successor
        child = node.left if node.left is not None else node.right
        if node.color == 'BLACK':
            if child is None:
                self.fix_double_black(node)
            else:
                node.value = child.value
                node.left = None
                node.right = None
        else:
            if child is not None:
                node.value = child.value
                node.left = None
                node.right = None
            else:
                if node.parent is None:
                    self.root = None
                else:
                    if node == node.parent.left:
                        node.parent.left = None
                    else:
                        node.parent.right = None
        if node.color == 'BLACK':
            self.fix_double_black(node)

    def fix_double_black(self, node):
        """
        Fixes double black violations that may occur after the removal of a black node.
        This method uses rotations and recolors nodes to restore red-black properties.
        """
        if node == self.root:
            return
        sibling = self._get_sibling(node)
        parent = node.parent
        if sibling is None:
            self.fix_double_black(parent)
        else:
            if sibling.color == 'RED':
                parent.color, sibling.color = sibling.color, parent.color
                if sibling == parent.left:
                    self.right_rotate(parent)
                else:
                    self.left_rotate(parent)
                self.fix_double_black(node)
            else:
                if (sibling.left is None or sibling.left.color == 'BLACK') and \
                   (sibling.right is None or sibling.right.color == 'BLACK'):
                    sibling.color = 'RED'
                    if parent.color == 'BLACK':
                        self.fix_double_black(parent)
                    else:
                        parent.color = 'BLACK'
                else:
                    if sibling == parent.left:
                        if sibling.left is None or sibling.left.color == 'BLACK':
                            self.left_rotate(sibling)
                            sibling = sibling.parent
                        sibling.color = parent.color
                        parent.color = 'BLACK'
                        sibling.left.color = 'BLACK'
                        self.right_rotate(parent)
                    else:
                        if sibling.right is None or sibling.right.color == 'BLACK':
                            self.right_rotate(sibling)
                            sibling = sibling.parent
                        sibling.color = parent.color
                        parent.color = 'BLACK'
                        sibling.right.color = 'BLACK'
                        self.left_rotate(parent)

    def _get_sibling(self, node):
        """
        Returns the sibling of the given node, i.e., the other child of the node's parent.
        """
        if node.parent is None:
            return None
        if node == node.parent.left:
            return node.parent.right
        else:
            return node.parent.left

    def _min_value_node(self, node):
        """
        Finds and returns the node with the minimum value in the specified subtree.
        This is always the leftmost node.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def clear(self):
        """
        Clears the tree by removing all references to the nodes,
        setting the root to None, and the size to 0.
        """
        self.root = None
        self.size = 0

    def ceiling(self, value):
        """
        Finds the smallest value in the tree that is greater than or equal to the given value.
        """
        current = self.root
        ceiling_value = None
        while current:
            if current.value >= value:
                ceiling_value = current.value
                current = current.left
            else:
                current = current.right
        return ceiling_value

    def first(self):
        """
        Returns the value of the first node in the tree, which is the smallest.
        """
        current = self.root
        if current is None:
            return None
        while current.left is not None:
            current = current.left
        return current.value

    def higher(self, e):
        """
        Finds and returns the lowest value in the tree that is greater than the given value.
        If there is no such value, returns None.
        """
        return self._higher_helper(self.root, e)

    def _higher_helper(self, node, e):
        """
        Auxiliary method to find the lowest value greater than the given one.
        Recursively navigates through the tree to find the right value.
        """
        if node is None:
            return None
        if e < node.value:
            if node.left is not None and e < node.left.value:
                return self._higher_helper(node.left, e)
            return node.value
        else:
            return self._higher_helper(node.right, e)

    def pollFirst(self):
        """
        Removes and returns the value of the node with the minimum value in the tree.
        Uses _min_value_node to find this node and then removes it.
        """
        if self.root is None:
            return None
        min_node = self._min_value_node(self.root)
        self.remove(min_node.value)
        return min_node.value

    def pollLast(self):
        """
        Removes and returns the value of the node with the maximum value in the tree.
        Uses the last method to find this node and then removes it.
        """
        if self.tree.length == 0:
            return None
        last_value = self.last()
        self.remove(last_value)
        return last_value

    def _max_value_node(self, node):
        """
        Finds and returns the node with the maximum value in the specified subtree.
        This is always the rightmost node.
        """
        current = node
        while current.right is not None:
            current = current.right
        return current

    def __iter__(self):
        """
        Returns an iterator that traverses the tree in ascending order.
        """
        return self._inorder_iterator(self.root)

    def _inorder_iterator(self, node):
        """
        Generator that traverses the nodes of the tree in order (left, root, right).
        """
        if node is not None:
            yield from self._inorder_iterator(node.left)
            yield node.value
            yield from self._inorder_iterator(node.right)

    def __reversed__(self):
        """
        Returns an iterator that traverses the tree in descending order.
        """
        return self._reverse_inorder_iterator(self.root)

    def _reverse_inorder_iterator(self, node):
        """
        Generator that traverses the nodes of the tree in reverse order (right, root, left).
        """
        if node is not None:
            yield from self._reverse_inorder_iterator(node.right)
            yield node.value
            yield from self._reverse_inorder_iterator(node.left)
