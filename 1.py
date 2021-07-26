class A(object):
    def __init__(self, a):
        self.a = a

    def test(self, b):
        print(self.a.get(b))


abc = A({'name':'Tom', 'age':'25', 'city':'newyork', 'sex':'man'})
abc.test('city')