print('''
 _     _____     _______                                     
| |   / _ \ \   / / ____|                                    
| |  | | | \ \ / /|  _|                                      
| |__| |_| |\ V / | |___                                     
|_____\___/  \_/  |_____| _   _ _        _  _____ ___  ____  
 / ___|  / \  | |   / ___| | | | |      / \|_   _/ _ \|  _ \ 
| |     / _ \ | |  | |   | | | | |     / _ \ | || | | | |_) |
| |___ / ___ \| |__| |___| |_| | |___ / ___ \| || |_| |  _ < 
 \____/_/   \_\_____\____|\___/|_____/_/   \_\_| \___/|_| \_|

''')
def calculate_love_score(name1 , name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(f'''Your Love Score is : {score}  
          ,-.-.
          `. ,'
            `''')
name1 = input("Enter your name: ")
name2 = input("Enter their name: ")
calculate_love_score(name1 , name2)
