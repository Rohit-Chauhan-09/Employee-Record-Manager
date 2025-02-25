import ast

print("Press 0 for Employee Data Entry or press 1 for find Data of Employee.")

class Employee:
    def __init__(self,i_d):
        self.i_d = i_d # Storing the user entered Id

    def write_s(self,Id,Name,Salary):
        with open("Employee Data.txt","a") as f:
            Dic_Employee = {"Employee Id":Id,"Employee Name":Name,"Employee Salary":Salary}
            # Storing the Employee data in the dictionary
            f.write(str(Dic_Employee)+"\n") # Writting the data in file, formate (Dictionary)
            print("Record Submitted...")
            print("")

    def read_s(self,i_d):
        found = False
        with open("Employee Data.txt", "r") as f:
            for line in f: # Loop for reading the each line of the file.
                dict_data = ast.literal_eval(line.strip()) # it removes leading and trailing whitespace from each line
                Employee_Id = (dict_data["Employee Id"]) # Assign the value 

                if (Employee_Id == i_d):
                    print(f"Records of Id: {i_d} is found.")
                    for key, value in dict_data.items(): # For printing the data
                        print(f"{key}: {value}")
                    found = True
                    break
            print("")
        if found == False: # For Error
            print(f"No employee found of ID {i_d}.")

try:
    user = int(input("Enter the number: "))
except ValueError:
    print("Please, Enter the correct value (0 or 1)!") # For string Error
else:
    details = Employee(user)
    if (user == 0 or user == 1): # Condition For Error
        if (user == 0):
            user_Input_1 = int(input("How many Employee Data you want Entry? "))
            print("")

            for i in range(1,user_Input_1+1): # Loop of Employee data Entry
                # Entry of data
                i_d = int(input('Enter the Employee Id: '))
                name = input('Enter the Employee Name: ')
                name2 = name.capitalize()
                salary = int(input('Enter the Employee Salary: '))
                details.write_s(i_d,name2,salary) # calling the function

        elif (user == 1):
            user_Input_2 = int(input("How many Employee Data you want? "))
            print("")

            for i in range(1,user_Input_2+1): # Loop for checking the Employee data
                i_d = int(input("Enter the employee Id: "))
                details.read_s(i_d) # calling the function
    else: # Error
        print("Please, Enter the correct value!")