#-------------------------------------------------#
# Title: Python Exception Handling and Python Pickling
# Dev:   Surafel Abeel
# Date:  Dec 3, 2018
# ChangeLog: (Surafel, 12/3/2018, Commented)
#   RRoot, 12/3/2018, Created Script

#-------------------------------------------------#


#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# lstTable = A row of text data that stores the output
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can use Input1 and Input2 to input their choice of integers
# User can see a Menu (Step 2)
# User can choose to operate the addition command (Step 3)
# User can choose to operate the Substraction command (Step 4)
# User can choose to operate the Multiplicaiton command (Step 5)
# User can choose to operate the Division command (Step 6)
# User can choose to save and close program (Step 7)

#-- Processing --#
# Step 1
# Program starts by asking the user for two integers (numbers of their choice)

# Step 2
# Display a menu of choices to the user

# Step 3
# Operate addition command and add to a lstTable

# Step 4
# Operate substraction command and add to a lstTable

# Step 5
# Operate multiplicaiton command and add to lstTable

# Step 6
# Operate division command and add to lstTable

# Step 7
# Save and Exit program
#-------------------------------

lstTable = []
#step 1
Input1 = input("Input the first number: ")
Input2 = input("Input the second number: ")

try:
    def main(): # the main function that captures all the rest of functions
        while (True): #option for the user (Step 2)

            print("""
            Menu of Options
            1) Addition
            2) Subtraction 
            3) Multiplicaiton
            4) Division
            5) Save and Exit Program
            """)
            #Step 2
            strChoice = str(input("Which option would you like to perform? [1 to 5] - ")) #user can pick from list
            print()  # adding a new line

            # Step 3
            # Compute Addition of given values
            if (strChoice.strip() == '1'):
                func1() #function 1 refers to the function that excutes addition
            # Step 4
            # Subtraction
            elif (strChoice.strip() == '2'):
                func2() #function 2 refers to the subtraction command
            #step 5
            #Multiply inputs
            elif (strChoice == '3'):
                func3() #function for multiplying inputs

            # Step 6
            # Divide inputs
            elif (strChoice == '4'):
                func4() #function for dividing first input to second input

            #Step 7
            # Save and exits
            elif (strChoice =='5'):
                func5() #Saves and exit
            else: break


    def func1(): #calling out funciton 1
        print("******* Addition of input1 and 2 is: *******")
        try: #Exception Handling
            Addition=(int(Input1) + int(Input2)) #Addition command
            print (Addition) #print data
            lstTable.append(Addition) #add data to lstTable
        except:
            print("Input has to be integer!") #if input is not integer, the following message displays
        print("*******************************************")

    def func2(): #calling out funciton 2
        print("******* Subtraction of input1 and 2 is: *******")
        try: #Exception Handling
            Subtraction = (int(Input1) - int(Input2))
            print (Subtraction)
            lstTable.append(Subtraction)
        except:
            print("Input has to be integer!") #if input is not integer, the following message displays
        print("*******************************************")

    def func3(): #calling out funciton 3
        print("******* Multiplication of input1 and 2 is: *******")
        try: #Exception Handling
            Multiplication = (int(Input1) * int(Input2)) #Multiplicaiton output
            print (Multiplication) #print data
            lstTable.append (Multiplication) #Add data to lstTable
        except:
            print("Input has to be integer!") #if input is not integer, the following message displays
        print("*******************************************")

    def func4(): #calling out function 4
        print("******* Division of input1 and 2 is: *******")
        try: #Exception Handling
            Division = (int(Input1) / int(Input2)) #Division command
            print (Division) #prints data
            lstTable.append (Division) #adds data to lstTable
        except:
            if Input2 == "0": #If input2 is zero, use exception handling to output the following message:
                print("Undefined, cannot divide by zero!") #Input2 cannot be 0!
            else:
                print("Input has to be integer!") #if input is not integer, the following message displays
        print("*******************************************")
    def func5(): #funciton 5 saves data (python pickling)
        #try:
        import pickle #Import pickle since it's not in pycharm
        Integer1 = Input1 #declaring inputs
        Integer2 = Input2 #declaring inputs
        List = [Integer1, Integer2, lstTable] #List of inputs and result
        print("Two of the inputs and the result from each command used is displayed in a list:" + " " + str(List))
        # store the data with the pickle.dump method
        objFile = open("C:\\PythonClass\\Assignment7\\BasicArithmetic.dat", "ab") #open .dat file
        pickle.dump(lstTable, objFile) #dump/load file
        objFile.close() #close file

        #read the data back with the same pickle.load method
        objFile = open("C:\\PythonClass\\Assignment7\\BasicArithmetic.dat", "rb") #read file
        objFileData = pickle.load(objFile)  # Loads row of data.
        objFile.close() #close file



except Exception as e: #exeption for the entire code
    print("Python reported the following error: " + str(e)) #print following message for errors
finally:
    print("No error detected; program works as expected!") #prints if no error detected

if __name__ == '__main__': #Calling out the main function which causes the code to run
    main() #referring to the main function

