"""This is the entry point of the program."""


def create_box(height, width, character):
    box = ''
    for i in range(height): #loop from 0 to height 
        box += (character * width) + '\n'
        print (character * width ) #prints character "width" many times
    return box
        
        


if __name__ == '__main__':
    create_box(3, 4, '*')
