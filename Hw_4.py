# Homework 04
"""
求質數：只可以被 1 及 自己 整除的數稱為質數
請輸入１～１００之間的質數有那些

 4 是質數????   不是；因為他被 1  、2  、4  整除
 5 是質數???    是：因為他只被 1  及 5 整除
"""

for a in range(2,101):   #從2迴圈到100
    for b in range(2,a): #從2迴圈到當前的a,  <n
        if (a % b == 0): #判斷a能被b整除（不是質數）
            break        #不是質數，中斷迴圈
    else:                
          print(a,"是質數")  #2 到 n-1 都不能被 n 整除，是質數

      
        



