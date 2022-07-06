#iterators
class Numberss:
  def __iter__(self):
    self.a = 10
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = Numberss()
iter1 = iter(myclass)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))