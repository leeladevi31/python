a=input("enter: ")
def snake_to_camel(word):
  import re
  return ''.join(x.capitalize() or '_' for x in word.split('_'))
print(snake_to_camel(x))
