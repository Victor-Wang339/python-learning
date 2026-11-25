name = "Wang"                      
age = 18                          
score = 100            

msg1 = "I am " + name + " and I am " + str(age) + " years old."  
print(msg1)                       

msg2 = "我是%s，今年%d岁，得分%.1f" % (name, age, score)  
print(msg2)                       

msg3 = "我是{}，今年{}岁，得分{:.2f}".format(name, age, score)  
print(msg3)                      
msg4 = "我是{0}，今年{1}岁，{0}很开心".format(name, age)  
print(msg4)                      
msg5 = "我是{n}，今年{a}岁".format(n=name, a=age)  
print(msg5)                   

msg6 = f"我是{name}，今年{age}岁，得分{score:.2f}"  
print(msg6)                      
msg7 = f"明年我就 {age + 1} 岁了"      
print(msg7)                       
msg8 = f"姓名大写：{name.upper()}"    
print(msg8)                      


print(f"{score:.2f}")             
print(f"{score:.0f}")           
print(f"{1234567:,}")            
print(f"{0.856:.1%}")           
print(f"{255:b}")               
print(f"{255:o}")                 
print(f"{255:x}")                
print(f"{42:08.2f}")             

print(f"|{'left':<10}|")            
print(f"|{'right':>10}|")           
print(f"|{'middle':^10}|")            
print(f"|{'fill in ':*^10}|")  
