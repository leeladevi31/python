import re
x = "asdfklsd*"
new = re.sub('[\w]+' ,'', x)
print (len(new))
