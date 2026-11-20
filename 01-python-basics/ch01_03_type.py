count = 100                      
price = 9.99                    
title = "Python basics"             
is_ok = True                      
nothing = None

print(count, type(count))       
print(price, type(price))         
print(title, type(title))       
print(is_ok, type(is_ok))      
print(nothing, type(nothing))    
print(isinstance(count, int))     
print(isinstance(price, int))    
print(isinstance(True, int))     


big = 2 ** 100                   
print(big)                       
ln = 1_000_000                
print(ln)                         

sci = 1.5e3                       
print(sci)                      


print(10 / 3)                    
print(10 // 3)                    
print(10 % 3)                    
print(2 ** 0.5)                   

s1 = 'Single quotes can also be used.'                
s2 = "Double quotes can also be used."                
s3 = "He said: 'Hello'"                
print(s1, s2, s3)               


print(bool(0))                    
print(bool(1))
print(bool(""))                  
print(bool("0"))                


print(0.1 + 0.2)                  
print(0.1 + 0.2 == 0.3)          
print(abs((0.1 + 0.2) - 0.3) < 1e-9)  


print(True + True)                
print(False + 5)                  
print(sum([True, False, True]))   

print(None == 0)                  
print(None == "")                
    
print(nothing is None)         


num = 10                          
num = num + 1                    
print(id(num))                   

text = "abc"                     
text2 = text.upper()            
print(text, text2)                

