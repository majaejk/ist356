PASSWORD = "secret" # constant, storing what is tested against

# Version 1: Single attempt
# input_password = input("Enter the password: ")

# if PASSWORD == input_password:
#     print("access granted")
#     exit(0)
# else:
#     print("invalid password")
#     exit(1)

# Version 2: 5 attempts with else on for loop
# for attempt in range(5):
#     input_password = input("Enter the password: ")
#     print(f"Attempt {attempt+1} of 5")
#     if PASSWORD == input_password:
#         print("access granted")
#         break # break only if input matches master
#     else:
#         print("invalid password")
# else: # if the loop completes without breaking do x
#     print("you are locked out")

# Version 3: has set max attempts with success variable
MAX_ATTEMPTS = 5 # versus having while loops the for needs to break
success = False
for attempt in range(MAX_ATTEMPTS):
    input_password = input("Enter the password: ")
    print(f"Attempt {attempt+1} of {MAX_ATTEMPTS}")
    if PASSWORD == input_password:
        print("access granted")
        success = True
        break # break only if input matches master
    else:
        print("invalid password")

if not success:
    print("you are locked out") # error condition is to be kind to you and the data source