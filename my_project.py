num = int(input())
def hello_word():
    print('Hello, World!!!')

hello_word()

# Необходимо реализовать рекурсивное выполнение функции hello_word, пока num > 0

def rec_h_w(num):
    if num == 0:
        return None
    else:
        hello_word()
        rec_h_w(num - 1)

