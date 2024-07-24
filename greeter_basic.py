from string import Template
#intro
print("Hey there, please input your details to receive a customized greeting from Greeter\n")
#User details form
first_name = input("First Name: ")
#Print greet statement
#method 1
# print("Hello "+ first_name + ", have a nice day")
# #method 2
# print(f'Hello {first_name}, have a nice day')
# #method 3
# print('Hello %s, have a nice day'%(first_name))
#method 4
new = Template('Hello $first_name, have a nice day')
print(new.substitute(first_name = first_name))
