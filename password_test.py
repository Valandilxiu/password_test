# 密碼重試程式

i = 3
while True:
    password = input('請輸入密碼: ')
    if password == 'a123456':
        print('登入成功')
    else:
        i = i - 1
        if i == 0:
            break
        print('密碼錯誤! 還有', i, '次機會')