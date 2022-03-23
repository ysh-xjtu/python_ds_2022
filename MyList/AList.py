from List import List
'''
这个Python文件定义已数组存储方式实现的线性表，其行为的限制来源于抽象类型List
同学们后续可以将已链表存储方式实现的线性表再重新创建一个Python文件，也可以
继续在这个文件中添加新的类类型

'''
class AList(List):
    def __init__(self, size=10):
        '''
        所有数据成员的命名都请大家在名字前加下划线（_）
        python的类型的定义里对私有数据这类访问型能力没有支持，故通过这种下划线起始的方式方便解释器做一些特殊的动作检查
        '''
        self._msize = size
        self._numInList = 0
        self._curr = 0
        '''
        创建一个大小为size的‘数组’（其实在python语言中就是线性表），数组中的元素内容为空值
        我们要掌握数组形式下的线性表的实现原理，所以放弃python自带的线性表list
        创建一个自定义的线性表List，以后就不会因为语言能力所限而不知所措
        '''
        self._listArray = [None]*size
    # 实现了clear方法，方法的逻辑和教材所示的java版本一致
    def clear(self):
        self._curr, self._numInList = 0, 0
    # 实现了insert方法，方法的逻辑和教材所示的java版本一致
    def insert(self, item):
        if self._numInList == self._msize:
            raise Exception("List is full") #借助于python的异常机制，当检测到条件不满足时抛出例外，终止程序的继续执行
        if self._curr not in range(0, self._numInList + 1):
            raise Exception("Bad value for curr")
        for i in range(self._numInList, self._curr, -1):
            self._listArray[i] = self._listArray[i-1]
        self._listArray[self._curr] = item
        self._numInList += 1
    '''
    请同学们根据线上视频的学习，以上面代码为样本补充实现List中定义的其他所有抽象方法
    这是一个非常好的实践过程，能够强化理解抽象数据类型和数据结构之间的关系，也能强化逻辑的严密性
    '''

    def append(self, item):
        '''在线性表的表尾追加元素item'''
        if self._numInList == self._msize:
            raise Exception("List is full.")
        self._listArray[self._numInList] = item
        self._numInList += 1

    def remove(self):
        '''将线性表当前位置的元素从线性表中删除，并返回该元素给调用者'''
        if self.isEmpty():
            raise Exception("Can't delete from empty list.")
        if not self.isInList():
            raise Exception("No current element.")
        it = self._listArray[self._curr]
        for i in range(self._curr, self._numInList-1):
            self._listArray[i] = self._listArray[i+1]
        self._numInList -= 1
        return it

    def setFirst(self):
        '''将当前位置（curr）设置为线性表的表首处'''
        self._curr = 0

    def next(self):
        '''将当前位置（curr）向后移动一个位置'''
        self._curr += 1

    def prev(self):
        '''将当前位置（curr）向前移动一个位置'''
        self._curr -= 1

    def length(self):
        '''获取线性表中实际存放的元素个数'''
        return self._numInList

    def setPos(self, pos):
        '''将当前位置（curr）设置为pos参数所对应的值'''
        self._curr = pos

    def setValue(self, item):
        '''将item的值设置为线性表中位置为curr的内容'''
        if not self.isInList():
            raise Exception("No current element.")
        self._listArray[self._curr] = item

    def currValue(self):
        '''获得线性表中位置为curr的元素内容，并将该内容返回'''
        if not self.isInList():
            raise Exception("No current element.")
        return self._listArray[self._curr]

    def isEmpty(self):
        '''判断当前线性表是否为空，空则返回True，否则返回False'''
        return self._numInList == 0

    def isInList(self):
        '''
        判断当前curr值是否为合理位置；
        合理即curr的值在[0, numInList)
        numInList为线性表中存储的实际元素个数
        '''
        return self._curr >= 0 and self._curr < self._numInList

    def print(self):
        if self.isEmpty():
            print("The list is empty.")
        else:
            print("[", end="  ")
            for i in range(0, self._numInList):
                print(self._listArray[i], end="  ")
            print("]")


