class encoder:
  def __init__(self, code, res):
    self.code = code
    self.res = res
  
  def encode(self):
    return self.code

code = encoder('print("Hello world!")', 'any')
print(code.encode())