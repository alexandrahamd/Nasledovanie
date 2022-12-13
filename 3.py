class MyList(list):
    names = []

    def __init__(self, lst):
        self._add(lst)

    def _add(self, data):
        for i in data:
            print('Работает магический метод 1')
            self.names.append(i)

    def __len__(self):
        print("Работает магический метод 2")
        return len(self.names)

    def __str__(self):
        print("Работает магический метод 3")
        return f"{self.names}"


lst = MyList(['Jone', 'Snow', 'Java'])

if not lst.names[2] == 'Python':
    lst.names[2] = 'Python'

print(lst)
print(len(lst))
