"""This is the entry point of the program."""


def create_box(height, width, character):
    for i in range(height): #loop from 0 to height 
        print (character * width ) #prints character "width" many times
       
        
        


if __name__ == '__main__':
    create_box(3, 3, '$')
