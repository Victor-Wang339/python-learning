print("Hello, Python!")
print("I am a beginner in Python.")                     
print(1+2)

print("--- line between ---")         

print("age:", 18, "years old")           

print()

print(3.14 * 2)                    
print("3.14 * 2")                 

print(True)                        
print(None)                       



import sys    

print("The current version of Python:", sys.version.split()[0]) 
print("Current script path:", __file__)                   
print("Was it directly executed:", __name__ == "__main__")    

print("a", "b", sep="-")                    
print("a", "b", end="")                      
print("A", "B", "C", sep="|", end="\n")      

if __name__ == "__main__":                   
    print("The main program entry has been executed.")                       
                 



from datetime import date   

WIDTH = 40        
name = "Victor-Wang339"        
major = "artificial intelligence"            
goal = "Proficient in Python"
today = date.today()        

print("=" * WIDTH)          
print("|" + "Personal Profile".center(WIDTH - 2) + "|")
print("=" * WIDTH)            
print("|" + f"name：{name}".ljust(WIDTH - 2) + "|")  
print("|" + f"major：{major}".ljust(WIDTH - 2) + "|") 
print("|" + f"goal：{goal}".ljust(WIDTH - 2) + "|")  
print("|" + f"date：{today}".ljust(WIDTH - 2) + "|")  
print("=" * WIDTH)            
