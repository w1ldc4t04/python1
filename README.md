# 期中報告第1題
南華大學-python期末報告
11124128 蘇佑庭 11124144 管心慈
#推导式与生成器
1. 輸出元素為0-9的3次方的列表
2. 輸出元素為0-9中偶數的三次方的列表
3. 輸出元素為元組的列表,元組中元素依次是0-9中的奇數和該數的三次方
4. 將列表ls中每個元素首字母轉為大寫,輸出新列表
5. #程式碼
第一題
1. 輸出元素為0-9的3次方的列表
```
def func1():
    print([x**3 for x in range(10)])
```
