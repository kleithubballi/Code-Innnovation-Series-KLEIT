#personal medical assistant
Disease_type = input('Enter the type of Disease: ')
#Enter the type of Disease any one:- Heart, Diabetes, High BP

Heart_medicine1 = "Morning time:- Heart Medicine1"
Heart_medicine2 = "Afternoon time:- Heart Medicine2"
Heart_medicine3 = "Night time:- Heart Medicine3"

Diabetes_medicine1 = "Morning time:- Diabetes Medicine1"
Diabetes_medicine2 = "Afternoon time:- Diabetes Medicine2"
Diabetes_medicine3 = "Night time:- Diabetes Medicine3"

High_BP_medicine = "Morning time:- High BP Medicine1"
High_BP_medicine = "Afternoon time:- High BP Medicine2"
High_BP_medicine = "Night time:- High BP Medicine3"

if Disease_type == 'Heart':
   print("You need to take, \n")
   print(Heart_medicine1)
   print(Heart_medicine2)
   print(Heart_medicine3)
elif Disease_type == 'Diabetes':
    print("You need to take, \n")
    print(Diabetes_medicine1)
    print(Diabetes_medicine2)
    print(Diabetes_medicine3)
elif Disease_type == 'High BP':
    print("You need to take, \n")
    print(Heart_medicine1)
    print(Heart_medicine2)
    print(Heart_medicine3)
else:
    print("Not found!")
    print("Please, enter the type of Disease any one:- Heart, Diabetes, High BP")