from AList import AList
from llist import LList

'''
该python文件主要用来写测试程序，以验证自定义的线性表的功能是否正确
'''
if __name__ == '__main__':
    numbers = LList()
    numbers.insert(20)
    numbers.append(21)
    numbers.setPos(1)
    numbers.insert(30)
    numbers.setFirst()
    numbers.next()
    numbers.insert(11)
    numbers.print()
    print(numbers.length())