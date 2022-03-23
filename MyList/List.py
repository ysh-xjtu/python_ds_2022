import abc

'''
请同学们按照如下的代码形式构建Python语言下的抽象类型（ADT）
下面的ADT即为教材中Java语言版本的List定义
'''

class List(metaclass=abc.ABCMeta):
    @abc.abstractmethod #定义抽象方法，无需实现功能
    def clear(self):
        '''清空整个线性表'''
        raise NotImplementedError

    @abc.abstractmethod
    def insert(self,item):
        '''在线性表的当前位置（curr）处插入元素item'''
        raise NotImplementedError

    @abc.abstractmethod
    def append(self,item):
        '''在线性表的表尾追加元素item'''
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self):
        '''将线性表当前位置的元素从线性表中删除，并返回该元素给调用者'''
        raise NotImplementedError

    @abc.abstractmethod
    def setFirst(self):
        '''将当前位置（curr）设置为线性表的表首处'''
        raise NotImplementedError

    @abc.abstractmethod
    def next(self):
        '''将当前位置（curr）向后移动一个位置'''
        raise NotImplementedError

    @abc.abstractmethod
    def prev(self):
        '''将当前位置（curr）向前移动一个位置'''
        raise NotImplementedError

    @abc.abstractmethod
    def length(self):
        '''获取线性表中实际存放的元素个数'''
        raise NotImplementedError

    @abc.abstractmethod
    def setPos(self, pos):
        '''将当前位置（curr）设置为pos参数所对应的值'''
        raise NotImplementedError

    @abc.abstractmethod
    def setValue(self, item):
        '''将item的值设置为线性表中位置为curr的内容'''
        raise NotImplementedError

    @abc.abstractmethod
    def currValue(self):
        '''获得线性表中位置为curr的元素内容，并将该内容返回'''
        raise NotImplementedError

    @abc.abstractmethod
    def isEmpty(self):
        '''判断当前线性表是否为空，空则返回True，否则返回False'''
        raise NotImplementedError

    @abc.abstractmethod
    def isInList(self):
        '''
        判断当前curr值是否为合理位置；
        合理即curr的值在[0, numInList)
        numInList为线性表中存储的实际元素个数
        '''
        raise NotImplementedError

