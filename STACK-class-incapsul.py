class Stack:
    def __init__(self, max_len=100, *args):
        self.stack = list(args)
        self.max_len = max_len

    def push(self):
        if len(self.stack) < self.max_len:
            n = input('Bведите число, которое хотите добавить')
            self.stack = self.stack + [n]
            return self.stack

    def pop(self):
        try:
            print(self.stack[-1])
        except IndexError:
            print('Стек пустой. Добавьте элементы для выполнения команды.')
        else:
            self.stack = self.stack[:-1]
        return self.stack

    def back(self):
        try:
            print(self.stack[-1])
        except IndexError:
            print('Стек пустой. Добавьте элементы для выполнения команды.')

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []
        return self.stack


def exit():
    print("Bye")


if __name__ == '__main__':
    stack = Stack()
    while True:
        command = input("Введите вашу команду:")
        if command == 'push':
            stack.push()
            print('ok')
        elif command == 'pop':
            stack.pop()
        elif command == 'back':
            # back(lis)
            stack.back()
        elif command == 'size':
            print(stack.size())
        elif command == 'clear':
            print('ok')
        elif command == 'exit':
            print('bye')
            break
        else:
            print('Error')
