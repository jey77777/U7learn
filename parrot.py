# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "


# message = ''
# while message != 'quit':
#     massage = input(prompt)
#     print(message)

# toppings = []
# message = ''
# while message != 'quit':
#     message = input("What tooppings you want to add to your pizza: ")
#     toppings.append(message)
# print(f"Your pizza ready with toppings: {toppings}")


# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
#  # Verify each user until there are no more unconfirmed users.
#  #  Move each verified user into the list of confirmed users.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# visits = {}
# go = True

# while go: 
#     name = input("Whats your name: ")
#     visit = input("Wanted country or place: ")

#     visits[name]=visit

#     again = input('do you want another visit?(y/n) ')
#     if again == 'n':
#         go = False
# for name, visit in visits.items():
#     print(f"{name} your wanted place is {visit}")


# def make_album(name, title):
#     art_name = {'Name': name, 'Album Title': title}
#     print(art_name)

# while True:
#     n = input("Enter your name: ")
#     if n == 'q':
#         break
#     t = input("Enter Album title: ")

    
#     if t == 'q':
#         break
#     make_album(n,t)
   
# messages = ['hi','how','all','good']
# list = []
# def message(messages, list):
#     while messages:
#         m = messages.pop()
#         list.append(m)


# def pri(list):
#     for lis in list:
#         print('Receieved messsages', lis)

# message(messages, list)
# pri(list)

# def make_car(name,manuf,**kwrgs):
#     kwrgs['Model name'] = name
#     kwrgs['Manufacturer'] = manuf
#     for n, m in kwrgs.items():
#         print(n,m) 

# car = make_car('subaru', 'outback', color='blue', tow_package=True)

# print(car)


class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        

    def restaurant_nama(self):
        print(f"Welcome to {self.name}")

    def name_cuisine(self):
        print(f"Main dish for today {self.cuisine}")

res1 = Restaurant('Lazzat', 'Langet')

print(res1.restaurant_nama())
print(res1.name_cuisine())
print(f"My restaurant name is {res1.name}")