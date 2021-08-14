import logging as lg

def evennos():
    lg.basicConfig(filename = "C:\\Users\\ADMIN\\log21\\jaga.log" , level=lg.INFO, format = '%(asctime)s %(message)s')
    lg.info("This is my addition function")
    try:
        n=int(input("enter a number based on your choice:"))
        for i in range(0,n):
              if (i%2==0):
                    print(i)
    except Exception as e:
          lg.error("this is my error",e)
          
          
          
            
        