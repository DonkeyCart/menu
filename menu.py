
order=[]
prices =[['Classic',17.50],['American',19],['milanesa',15.5],['veggie',16.50],['coripan', 16],['loaded fries',11.5],['fries',8]]
total = 0

def Menu():
  print()
  print('***** menu ******')
  for i in range(0, 7):
    print(i+1,'',prices[i][0],' $',prices[i][1] )
  print()

  print ("welcome to el cordobes here is our menu: ")
  print()

  


def getOrder():
  orderLine=int(input("what would you like to order: "))
  order.append(orderLine) #this is to make the order have somewhere to be stored

  while True: 
    try:
      orderLine=int(input("Is there anything else you would like to order? enter 0 to finish "))

      if orderLine == 0:
        break

      if orderLine <= -1 or orderLine >= 7:      
        print("not a vaild input try agan.")
        
      else:
        order.append(orderLine) #this is to make the order have somewhere to be stored
      
    except ValueError:
      print ("Not a valid input try again")


def checkOrder():
  print("your oreder is")
  for i in order:
    print("   ",prices[i][0])
  
  check = input("would you like anything else? enter Yes to add an item")
  if check == "Yes":
    b = int(input("What would you like to add: "))
    order.append(b) 
    print('item added')
  elif check == "yes":
    b = int(input("What would you like to add: "))
    order.append(b)    
    print('item added')
  else:
    print()
   

def payment():
  total = 0
  for item in order:
      total = total + prices[int(item)-1][1]

  print("Your total comes to", total)
  
  while True:
    try:
      x = input("Do you want to pickup or get it delieverd: ")
      if x == "pickup": 
        name = input("Please enter a name for your order: ")
        phoneNumber = input("Please enter your phone number: ") 
        print("see you shortly ")
        break
      
      elif x == "delieverd":
        adress = input("Where would you like it delieverd: ")
        print("your order is on its way")
        break

    except ValueError:
      print("not a valid option try again")

Menu()
getOrder()
checkOrder()
payment()





  
  


