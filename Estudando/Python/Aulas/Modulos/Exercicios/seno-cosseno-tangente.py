import math
num = float(input('Digite o angulo quer voce deseja: '))
tan = math.tan(math.radians(num))
cos = math.cos(math.radians(num))
sen = math.sin(math.radians(num))
print(f'O angulo de {num} tem o SENO de {sen:.2f}\nO angulo {num} tem o COSSENO de {cos:.2f} \nO angulo de {num} tem a TANGENTE de {tan:.2f}')
