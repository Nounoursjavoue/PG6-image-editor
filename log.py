

def log (msg)  :
    f = open("logger.log" , "a")
    f.write(msg + "\n") 
    f.close()
    
    
def read_log () :
    f = open("logger.log" , "r") 
    log = f.readlines()
    for ligne in log :
        print(ligne)
    
    
read_log()