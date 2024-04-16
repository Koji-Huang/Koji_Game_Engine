from typing import TypeVar

_KT = TypeVar('_KT')
_VT = TypeVar('_VT')
_T = TypeVar('_T')


class LinkedListNode:
    def __init__(self, value: _T, last: any = None):
        self.value = value
        self.last = last
        self.next = None

    def __next__(self):
        return self.next

    def __reversed__(self):
        tmp = self.next
        self.next = self.last
        self.last = tmp

    def __len__(self):
        return 1 + self.next.__len__()

    def append(self, value: _VT):
        if isinstance(value, LinkedListNode):
            if self.next is None:
                self.next = value
                value.last = self
            else:
                self.next.append(value)
        else:
            self.next = LinkedListNode(value, self)

    def insert(self, value: any):
        old = self.next
        if isinstance(value, LinkedListNode):
            replace = value
            replace.last = self
        else:
            replace = LinkedListNode(value, self)
        self.next = replace
        if old.last is not None:
            replace.insert(old)

    def remove(self):
        if self.last is not None:
            self.last.next = self.next
        if self.next is not None:
            self.next.last = self.last


class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.size = 0
        self.extract_from_head = False

    def append(self, value: _VT):
        if self.head is None:
            if isinstance(value, LinkedList):
                copy = value.__copy__()
                self.head = copy.head
                self.tail = copy.tail
                self.size = copy.size
            elif isinstance(value, LinkedListNode):
                self.head = value
                self.tail = value
                self.size = 1
            else:
                self.head = LinkedListNode(value)
                self.tail = self.head
                self.size = 1
        else:
            if isinstance(value, LinkedList):
                self.tail.append(value.__copy__().head)
                self.size += value.size
            elif isinstance(value, LinkedListNode):
                self.tail.append(value)
                self.size += value.__len__()
            else:
                self.tail.append(value)
                self.size += 1
                self.tail = self.tail.next
            while self.tail.next is not None:
                self.tail = self.tail.next

    def insert(self, index, value: _VT):
        node = self.__get_node__(index)
        node.insert(value)
        if node == self.tail:
            self.tail = node.next
        self.size += 1

    def remove(self, value: _T):
        node = self.__search_node__(value)
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.last
        node.remove()
        self.size -= 1

    def size(self):
        return self.size

    def clear(self):
        self.size = None
        self.head = None
        self.tail = None

    def reverse(self):
        head = self.head
        tail = self.tail
        node = self.head
        while node is not None:
            node.__reversed__()
            node = node.last
        self.head = tail
        self.tail = head

    def show(self):
        print("LinkedList: ", self.__iter__())

    def pop(self, index: int = None):
        if index is None:
            if self.extract_from_head:
                get = self.head
                index = 0
            else:
                get = self.tail
                index = self.size - 1
        else:
            get = self[index]
        if get is None:
            return None
        else:
            self.__delitem__(index)
            return get

    def extend(self, value):
        self.append(value)

    def __copy__(self):
        ret = LinkedList()
        node = self.head
        while node is not None:
            ret.append(node.value)
            node = node.next
        return ret

    def __get_node__(self, index: int):
        if index >= self.size:
            raise "Index out of range"
        if index < self.size / 2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.size - index):
                node = node.last
        return node

    def __search_node__(self, value: _T):
        node = self.head
        while node is not None:
            if node.value == value:
                return node
        return None

    def __len__(self):
        return self.size

    def __iter__(self):
        ret = list()
        node = self.head
        while node is not None:
            ret.append(node.value)
            node = node.next
        return ret.__iter__()

    def __item__(self):
        return tuple(self.__iter__())

    def __setitem__(self, key, value):
        if key <= self.size:
            node = self.__get_node__(key)
            if node is None:
                node = LinkedListNode(value)
            node.value = value
        else:
            raise IndexError("Index out of range")

    def __delitem__(self, key):
        node = self.__get_node__(key)
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.last
        node.remove()
        self.size -= 1

    def __getitem__(self, item):
        return self.__get_node__(item).value

    def __contains__(self, *args, **kwargs):
        for i in self.__iter__():
            if i == args[0]:
                return True
        return False

    def __iadd__(self, *args, **kwargs):
        new_list = self.__copy__()
        new_list.append(args[0])
        return new_list
