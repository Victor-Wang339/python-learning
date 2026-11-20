s = 'python'
print(len(s))
print(s[0])
print(s[2])
print(s[-1])
print(s[-6])

print(s[0:3])   
print(s[:3])                    
print(s[3:])                    
print(s[:])
print(s[::2])                  
print(s[::-1])                                
print(s[100:200])                 
print(repr(s[100:200]))           

print('Py' in s)
print('py' in s)
print(s.find('t'))
print(s.find('d'))
print(s.count('p'))


print('Hello'.lower())
print('hello'.upper())
print('hello world'.title())
print('hello'.capitalize())


msg = ' Hello   '
print(msg.strip())
print(msg.lstrip())
print(msg.rstrip())

print('xxxxabcxxxxxxx'.strip('x'))

print('a-b-c'.replace('-','+'))
print('a-b-c'.split('-'))
print('a  b c       d'.split())
print('-'.join(['a','b','c']))

print(s.startswith('py'))
print(s.endswith('on'))

name = "python"                   
name2 = name.upper()             
print(id(name), id(name2))        


s2 = "cat"                         
s3 = s2[:1] + "o" + s2[2:]       
print(s3)                         



url = "https://example.com/data/report.csv"  
print(url.split("/")[-1])
print(url.rsplit("/", 1)[-1])      
file_name = url.split("/")[-1]    
print(file_name.split(".")[-1])    


print("123".isdigit())             
print("abc".isalpha())            
print("abc123".isalnum())         
print("   ".isspace())             
print("123".isdigit(), "-123".isdigit())  


print(ord("a"))                  
print(chr(97))                   
print(ord("中"))                  
    
  
text = "  Hello  "                
text.strip()                      
print(repr(text))                  
text = text.strip()               
print(repr(text))             


print("apple" < "banana")         
print("A" < "a")                   
print("10" < "9") 
