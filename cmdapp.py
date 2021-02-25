#Written by Braedon Kimball (bmk228) for Software Quality Assurance
def BMI():
	print("BMI goes here.")


def retirement():
	print("Retirement goes here.")






def main():

	print("Welcome to the application! Options below: \n")
	x = 0
	while(x==0):
		
		print("1: Calculate BMI \n2: Calculate Retirement\n3: Exit the program\n")
		var = input()
		
		if var == '1':
			BMI()
			
		
		elif var == '2':
			retirement()
		
		elif(var == '3'):
			break
		
		else:
			print("Please input a valid option, either 1 or 2.\n")

	return


main()

