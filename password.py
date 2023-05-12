password = 'a123456'
x = 0
while True :
    passwordin = input('請輸入密碼：')
    if passwordin != password and x == 0: 
        print('您還剩下2次機會')
        x = x + 1
    elif passwordin != password and x == 1:
    	print('您還剩下1次機會')
    	x= x + 1
    elif passwordin != password and x == 2:
    	print('密碼錯誤')
    	break
    if passwordin == password:
        print('登入成功')
        break