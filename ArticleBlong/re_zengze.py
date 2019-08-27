import re
string='Hello \n Word lll'
# .匹配，匹配任意非换行字符
result=re.findall(r'..',string)
print(result)
# \w 匹配所有数字、字母、下划线
result=re.findall(r'\w',string)
print(result)
#\W 匹配所有非数字、字母、下划线
result=re.findall(r'\W',string)
print(result)
# \d 匹配所有数字
result=re.findall(r'\d',string)
print(result)
# \D 匹配所有非数字
result=re.findall(r'\D',string)
print(result)
# [] 返回中括号中任意一个字符或任意范围的字符
result=re.findall(r'[A-Z]',string)
print(result)
# 取反
result=re.findall(r'[^A-Z]',string)
print(result)
# | 匹配两边任意一边的字符
result=re.findall(r'H|h|W|w',string)
print(result)
# ( ) 组匹配
# 匹配一个数字或字母、下划线 时前面需要H
result=re.findall(r'H(\w)',string)
print(result)
# 匹配H后面有字母数字、下划线
result=re.findall(r'H\w',string)
print(result)
# （）命名组匹配，给组起名字
result=re.findall(r'(?P<id>\w)\w(?P=id)',string)
print(result)

