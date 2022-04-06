num1 = float(input('Primeiro numero: '))
num2 = float(input('Segundo numero: '))
if num1 > num2:
    print('O \033[1:34mPRIMEIRO\033[0m é maior')
elif num2 > num1:
    print('O \033[1:34mSEGUNDO\033[0m é maior')
else:
    print('Os dois valores sao \033[1:34mIGUAIS\033[0m')