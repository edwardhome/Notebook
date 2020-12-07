class Desktop:
    pass
class Notebook:
    pass

Macbook = Notebook()

print(isinstance(Macbook,Desktop))
print(isinstance(Macbook,Notebook))