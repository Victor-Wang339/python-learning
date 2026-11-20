print("Hello, Python!")
print("我是一名python初学者")                     
print(1+2)

print("--- 分隔线 ---")         

print("年龄:", 18, "岁")           

print()

print(3.14 * 2)                    
print("3.14 * 2")                 

print(True)                        
print(None)                       



import sys    

print("当前 Python 版本:", sys.version.split()[0]) 
print("当前脚本路径:", __file__)                   
print("是否被直接运行:", __name__ == "__main__")    

print("a", "b", sep="-")                    
print("a", "b", end="")                      
print("A", "B", "C", sep="|", end="\n")      

if __name__ == "__main__":                   
    print("主程序入口被执行了")                       
                 



from datetime import date   

WIDTH = 40        
name = "张三"        
major = "人工智能"            
goal = "精通python"
today = date.today()        

print("=" * WIDTH)          
print("|" + "个 人 名 片".center(WIDTH - 2) + "|")
print("=" * WIDTH)            
print("|" + f"姓名：{name}".ljust(WIDTH - 2) + "|")  
print("|" + f"专业：{major}".ljust(WIDTH - 2) + "|") 
print("|" + f"目标：{goal}".ljust(WIDTH - 2) + "|")  
print("|" + f"日期：{today}".ljust(WIDTH - 2) + "|")  
print("=" * WIDTH)            
