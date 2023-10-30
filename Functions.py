#def my_Function():
#    print("Hello from a function")
#my_Function()
    
#def my_function(fname):
#    print(fname + "Refsnes")
#my_function("Emil")    
#my_function("Tobias")    
#my_function("Linux")    

#def my_function(fname , lname):
#    print(fname +" " +lname)
#my_function("pranita" , "k")    

#def my_function(*kids):
#    print("Yogest child is" + " " +kids[2])
#my_function("pari" , "aks" , "soni" , "akki")    

#def my_function(child1 , child2, child3):
#    print("The Yongest child is" +" "+child3)
#my_function(child1 ="pari", child2 = "aks", child3 = "akki")

#def my_function(**kid):
#    print("his last name is :" + kid["fname"], kid["lname"] , kid["address"] ,)
#my_function(fname = "Pari" , lname = "K" , address = "pune")

#def my_function(country = "Norway"):
#    print("i am from " +country)
#my_function("India")
#my_function()
#my_function("Sweden")

#def my_fun(food):
#    for x in food:
#        print(x)
#fruits = ["apple" , "banana" , "cherry"]
#city = ["pune" ,"nashik","delhi"]
#my_fun(fruits) 
#my_fun(city)   

#def return_fun(x):
#    return 5*x
#print(return_fun(3))
#print(return_fun(2))
#print(return_fun(5))
    
#def empty_fun(fname):
#    pass

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)