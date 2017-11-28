
x=[4,6,1,3,5,7,25]
def stars(x):
	star="*"
	for i in range(len(x)):	
		print star*i 
		'''
		python allows us to multiply an integer and 
		a string, it assumes that you want that value 
		in duplicity
		'''
stars(x)

#part II

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def newstar(x):
	star="*"
	for i in x:
		if type(i) is int:
			print star*i
		elif type(i) is str:
			print i[0].lower()*len(i)

newstar(x)