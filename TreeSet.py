from RedBlack import Node
from RedBlack import RedBlackTree


class TreeSet:
    def __init__(self):
        """
        Constructor of the TreeSet class.

        Initializes a new TreeSet with an empty Red-Black Tree and undefined data type.
        """
        self.tree = RedBlackTree()
        self._datatype = None

    def add(self, obj):
        """
        Adds an element to the set.

        If the data type of the set is not defined, it defines it with the type of the first added element.

        Args:
            obj: The object to add to the set.

        Returns:
            True if the object was added successfully, False if the data type does not match the set's type.
        """
        if self._datatype is None:
            self._datatype = type(obj)
        elif type(obj) != self._datatype:
            self.raise_type_error(obj, self._datatype)
            return False

        if self.tree.contains(obj):
            return False  # Do not add duplicates
        self.tree.add(obj)
        return True

    def addAll(self, objList):
        """
        Adds a list of elements to the set.

        Args:
            objList: A list of objects to add to the set.

        Returns:
            True after adding all elements.
        """
        for obj in objList:
            self.add(obj)
        return True

    def ceiling(self, e):
        """
        Finds the smallest value in the set that is greater than or equal to the given element.

        Args:
            e: The element for which the ceiling is sought.

        Returns:
            The smallest value in the set that is greater than or equal to the given element, or None if none.
        """
        return self.tree.ceiling(e)

    def clear(self):
        """
        Removes all elements from the set.
        """
        self.tree.clear()
        self._datatype = None

    def clone(self):
        """
        Creates and returns a shallow copy of the set.

        Returns:
            A shallow copy of the set.
        """
        new_set = TreeSet()
        new_set.tree = self.tree.clone()
        new_set._datatype = self._datatype
        return new_set

    def contains(self, obj):
        """
        Checks if the set contains a given object.

        Args:
            obj: The object to check for its presence in the set.

        Returns:
            True if the object is present in the set, False otherwise.
        """
        return self.tree.contains(obj)

    def descendingIterator(self):
        """
        Returns an iterator to traverse the set in descending order.

        Returns:
            An iterator to traverse the set in descending order.
        """
        return iter(reversed(self.tree))

    def first(self):
        """
        Returns the first value in the set.

        Returns:
            The first value in the set, or None if the set is empty.
        """
        current = self.tree.root
        if self.tree.length == 0:
            raise TypeError("The tree is empty")
        else:
            while current and current.left:
                current = current.left
        return current.value if current else None

    def floor(self, value):
        """
        Finds the largest element in the set that is less than or equal to the given value.

        Args:
            value: The value for which the floor is sought.

        Returns:
            The largest element in the set that is less than or equal to the given value, or None if none.
        """
        current = self.tree.root
        floor_value = None

        while current:
            if current.value == value:
                return current.value
            elif current.value < value:
                floor_value = current.value
                current = current.right
            else:
                current = current.left
        return floor_value

    def higher(self, value):
        """
        Finds the smallest element in the set that is greater than the given value.

        Args:
            value: The value for which a greater value is sought.

        Returns:
            The smallest element in the set that is greater than the given value, or None if none.
        """
        current = self.tree.root
        higher_value = None

        while current:
            if current.value > value:
                higher_value = current.value
                current = current.left
            else:
                current = current.right
        return higher_value

    def isEmpty(self):
        """
        Checks if the set is empty.

        Returns:
            True if the set is empty, False otherwise.
        """
        return self.tree.length() == 0

    def iterator(self):
        """
        Returns an iterator to traverse the set.

        Returns:
            An iterator to traverse the set.
        """
        return iter(self.tree)

    def last(self):
        """
        Returns the last element of the set.

        Returns:
            The last element of the set, or None if the set is empty.
        """
        current = self.tree.root
        if self.tree.length == 0:
            raise TypeError("The tree is empty")
        else:
            while current and current.right:
                current = current.right
        return current.value if current else None

    def lower(self, e):
        """
        Finds the largest element in the set that is less than the given element.

        Args:
            e: The element for which a smaller value is sought.

        Returns:
            The largest element in the set that is less than the given element, or None if none.
        """
        current = self.tree.root
        result = None
        while current:
            if e > current.value:
                result = current.value
                current = current.right
            else:
                current = current.left
        return result

    def pollFirst(self):
        """
        Removes and returns the first element of the set.

        Returns:
            The first element of the set, or None if the set is empty.
        """
        if self.isEmpty():
            return None
        first = self.first()
        self.remove(first)
        return first

    def pollLast(self):
        """
        Removes and returns the value of the node with the maximum value in the tree.
        Uses the last method to find this node and then removes it.
        """
        if self.isEmpty():
            return None
        last_value = self.last()
        self.remove(last_value)
        return last_value

    def remove(self, obj):
        """
        Removes an element from the set if it is present.

        Args:
            obj: The object to remove from the set.

        Returns:
            True if the object was removed successfully, False if the object is not present.
        """
        if self.isEmpty() or type(obj) != self._datatype:
            return False
        if not self.tree.contains(obj):
            return False
        self.tree.remove(obj)
        return True

    def size(self):
        """
        Returns the number of elements in the set.

        Returns:
            The number of elements in the set.
        """
        return self.tree.length()

    def raise_type_error(self, obj, supported_datatype):
        """
        Raises a TypeError exception indicating that the datatype is not supported.

        Args:
            obj: The object with the unsupported datatype.
            supported_datatype: The datatype supported by the set.
        """
        raise TypeError("The datatype {} is not supported. Only {} are supported.".format(
            type(obj), supported_datatype))
