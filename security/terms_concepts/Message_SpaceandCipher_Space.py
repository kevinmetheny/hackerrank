Enter file contents here
num = raw_input()
code = ""
for dig in num:
  new = (int(dig)+1)%10
  code = code + str(new)
print code
