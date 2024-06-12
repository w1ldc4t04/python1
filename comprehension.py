ls = ['the lord of the rings','anaconda','legally blonde','gone with the wind']

def func1():
    print([x**3 for x in range(10)])
def func2():
    print([x**3 for x in range(10) if x%2==0])
def func3():
    print([(x,x**3) for x in range(10) if x%2])
def func4():
    print([s.capitalize() for s in ls])
options={
    '1':func1,
    '2':func2,
    '3':func3,
    '4':func4
}
ll=['1','2','3','4']
c='1'
while c in ll :
    c=input('1. 輸出元素為0-9的3次方的列表\n'+
        '2. 輸出元素為0-9中偶數的三次方的列表\n'+
        '3. 輸出元素為元組的列表,元組中元素依次是0-9中的奇數和該數的三次方\n'+
        '4. 將列表ls中每個元素首字母轉為大寫,輸出新列表\n')
    if c in options:
        options[c]()
print("結束程序")