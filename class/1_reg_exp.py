import re

text='hey i am asteek 1-1 my number is 9015099260 call any time if you need any help from me and my assistant  number is (999)-333-4444 , - asteek  ai abc j a aii'
# pat='\(\d{3}\)-\d{3}-\d{4} | \d{10}'
# match=re.findall(pat,text)
# print(match)
# pat2='hey \d-\d ([^\n]*)'
# print(re.findall(pat2,text))

# gives all the charcters address that end with eek
# pat3=re.compile(r'.eek')

# match=pat3.finditer(text)
# for i in match:
#     print(i)

# return if string start with hey
# pat4=re.compile(r'^hey')
# match=pat4.findall(text)
# print(match)

# return if string end with eek
# pat5=re.compile(r'eek$')
# match=pat5.findall(text)
# print(match)

# # return all the list with  a or ai aii aiii
# pat6=re.compile(r'ai*')
# match=pat6.findall(text)
# print(match)

# return all the list with  ai aii aiii
# pat6=re.compile(r'ai+')
# match=pat6.findall(text)
# print(match)

# return all the list with  a or specific number of i
# pat6=re.compile(r'ai{2}')
# match=pat6.findall(text)
# print(match)

# special sequences

# return is string start with hey
# pat=re.compile(r'\Ahey')
# match=pat.findall(text)
# print(match)

# return is string end with eek
# pat=re.compile(r'ek\Z')
# match=pat.findall(text)
# print(match)

pat=re.compile(r'\d{10}')
match=pat.findall(text)
print(match)
