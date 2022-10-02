# Pseudocode: 
# #Create a function freed_prisoners taking list of prison cells as an argument
# def freed_prisoners(list_of_prison_cells):
# #Create a variable free_prisoners storing number of freed prisoners
# 	#Loop through the list_of_prison_cells
# 	for cell in list_of_prison_cells:
# 		#Use if statement to check whether cell is locked: if locked (0) move on to the next cell; 
# 		if cell == 0:
# 			continue

# 		#if unlocked(1) free the prisoner and increase variable storing number of freed prisoners by one and enter another 
# 		else:
# 			free_prisoners += 1

# 		#Enter the loop through the list_of_prison_cells and change every 0 to 1, and every 1 to 0 using if else conditional statement.
# 		#Create counter variable outside of the loop and increment by one on each iteration.
# 			counter = 0
# 			for cell in list_of_prison_cells:
# 				if cell == 1:
# 					list_of_prison_cells[counter] == 0
# 					counter += 1
# 				else:
# 					list_of_prison_cells[counter] == 1
# 					counter += 1

# 		#Print free_prisoners variable
# 		print(free_prisoners)

# # Call the freed_prisoners(list_of_prison_cells) function
# freed_prisoners(list_of_prison_cells)

# Python code: 
def freed_prisoners(list_of_prison_cells):
  free_prisoners = 0
  for cell in list_of_prison_cells:
    if cell == 0:
      continue
    else:
     free_prisoners += 1
     counter = 0
     for cell in list_of_prison_cells:
      if cell == 1:
        list_of_prison_cells[counter] = 0
        counter += 1
      else:
        list_of_prison_cells[counter] = 1
        counter += 1
  print(free_prisoners)  
  
freed_prisoners([1, 1, 0, 0, 0, 1, 0])
