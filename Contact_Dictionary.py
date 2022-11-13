print("******** Programmed By ********")
print("******** Raymart Latap ********")
print("********** BSCOE 2-2 **********\n")


#Empty Dictionary
contacts = {}

#Display a menu of options
print("\n------Menu------")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit")
print("----------------\n")

while True:
#Allow user to select item in the menu (check if valid)
	menu_opt = (int(input("\nWhat do you want to do?:")))
	
#Option 1: Ask personal data for contact tracing
	if menu_opt == 1:
		fullname = input("Fullname: ")
		age = input("Age: ")
		address = input("Address: ")
		phone_num = input("Phone Number: ")
		contacts[fullname] = {"Age" : age, "Address" : address, "Phone Number" : phone_num}
		print("Saved")
	
	
		
#Option 2: Search, ask full name then display the record
	elif menu_opt == 2:
		fullname_search = input("Fullname: ")
		if fullname_search in contacts.keys():
		              	for key, value in contacts[fullname_search].items():
		              		print(key,":",value)
		              		
		else:
			print("Contact not found")


#Option 3: Ask the user if want to exit or retry.			
	elif menu_opt ==3:
		exit = input("Exit? (Y/N): ")
		if exit == "Y":
			break
			
		else:
			print(menu_opt)