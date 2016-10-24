"""This is the entry point of the program."""

"""
def create_box(height, width, character):
    box = ''
    
    if height >= 1 and width >= 1:
        box += (character * width) + '\n'
        for i in range(height-2): #loop from 0 to height 
            box += character + (width-2) * ' ' + character
            #print (character * width ) 
        box += (character * width) + '\n'
        print (box)
    else:
        print("error: height and width must be >= 1")
        
    return box
     

"""





def create_box(height, width, character):        
    box = ''
    unit_gap_of_hollow = " "
    for i in range(height):
        if (i == 0 or i == height-1):
            box += (character * width)      # + '\n'
            print (character * width) #prints character "width" many times
        else:
            box += (character + unit_gap_of_hollow * (width-2) + character)
            print (character + unit_gap_of_hollow * (width-2) + character)
    return box

#QUESTION: where is the hidden '\n' that adjusts the box perfectly 

if __name__ == '__main__':
    create_box(10, 30, '*')



#working attempt:
"""
height = 10
width = 20
unit_gap_of_hollow = " "
for i in range(height):
	if i == 0 or i == height-1:
		print ('*' * width )
	else:
		print('*' + unit_gap_of_hollow*(width-2) + '*') #print only first and last part
												   		#-2 from the width bc two stars 		  	  #taking place of gap
"""	    

""" 
0th height - full width
1st height - first and last part of width only 
2nd height - full width
"""
