# Create a function called draw_stars() that takes a list of numbers and prints out * corresponding to the number value in the list

def stars(list):
	star="*"
	for i in range(0,len(list)):	
		a=list[i]*star
		print a 
	return list
stars([4,6,1,3,5,7,25])

#part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def newstar(x):
	star="*"
	for i in x:
		if type(i) is int:
			print star*i
		elif type(i) is str:
			print i[0].lower()*len(i)
newstar(x)