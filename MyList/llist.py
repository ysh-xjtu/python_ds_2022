from List import List

# 创建链表所需要的结点类类型
class Link():
    def __init__(self, it=None, nextVal=None):
        self._element = it
        self._next = nextVal
    def next(self):
        return self._next
    def setNext(self, nextVal):
        self._next = nextVal
    def element(self):
        return self._element
    def setElement(self, it):
        self._element = it

# 按照List抽象数据类型的规范，定义链表存储方式实现的线性表LList

class LList(List):
    def __init__(self):
        self._head = Link()
        self._curr = self._head
        self._tail = self._head
        self._length = 0

    def clear(self):
        '''清空整个线性表'''
        self._head.setNext(None)
        self._curr = self._head
        self._tail = self._head
        self._length = 0

    def insert(self,item):
        '''在线性表的当前位置（curr）处插入元素item'''
        if self._curr == None:
            raise Exception("No current element")
        tempNode = Link(item, self._curr.next())
        self._curr.setNext(tempNode)
        if self._curr == self._tail:
            self._tail = self._curr.next()
        self._length += 1

    def append(self,item):
        '''在线性表的表尾追加元素item'''
        self._tail.setNext(Link(item, None))
        self._tail = self._tail.next()
        self._length += 1

    def remove(self):
        '''将线性表当前位置的元素从线性表中删除，并返回该元素给调用者'''
        if self.isEmpty():
            raise Exception("Can't delete from empty list.")
        if not self.isInList():
            raise Exception("No current element.")
        item = self._curr.next().element()
        if self._tail == self._curr.next():
            self._tail = self._curr
        self._curr.setNext(self._curr.next().next())
        self._length -= 1
        return item

    def setFirst(self):
        '''将当前位置（curr）设置为线性表的表首处'''
        self._curr = self._head

    def next(self):
        '''将当前位置（curr）向后移动一个位置'''
        if self._curr != None:
            self._curr = self._curr.next()

    def prev(self):
        '''将当前位置（curr）向前移动一个位置'''
        if self._curr == None or self._curr == self._head:
            self._curr = None
            return
        temp = self._head
        while temp != None and temp.next() != self._curr:
            temp = temp.next()
        self._curr = temp

    def length(self):
        '''获取线性表中实际存放的元素个数'''
        return self._length

    def setPos(self, pos):
        '''将当前位置（curr）设置为pos参数所对应的值'''
        self._curr = self._head
        index = 0
        while self._curr != None and index < pos:
            self._curr = self._curr.next()
            index += 1

    def setValue(self, item):
        '''将item的值设置为线性表中位置为curr的内容'''
        if not self.isInList():
            raise Exception("No current element")
        self._curr.next().setElement(item)

    def currValue(self):
        '''获得线性表中位置为curr的元素内容，并将该内容返回'''
        if not self.isInList():
            return None
        return self._curr.next().element()

    def isEmpty(self):
        '''判断当前线性表是否为空，空则返回True，否则返回False'''
        return self._head.next() == None

    def isInList(self):
        '''
        判断当前curr值是否为合理位置；
        合理即curr的值为head指针的内容一直到tail之前
        '''
        return self._curr != None and self._curr.next() != None

    def print(self):
        if self.isEmpty():
            print("The list is empty.")
        else:
            print("[", end="  ")
            temp = self._head.next()
            while temp != None:
                print(temp.element(), end="  ")
                temp = temp.next()
            print("]")




