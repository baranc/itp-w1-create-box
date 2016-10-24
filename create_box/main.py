def create_box(height, width, character):
    
    box = ''
    
    for i in range(height):
        box += (character * width) + '\n'
  
    return box

#extra challenge    
def create_empty_box(height, width, character):
    
    box = ''
    hollow_string_space = " " # one space unit
    
    for i in range(height):
        if (i == 0 or i == height-1):
            box += (character * width)
        else:
            box += (character + hollow_string * (width-2) + character)
    
    return box
    
if __name__ == '__main__':
    create_box(5, 10, '*')
    create_empty_box(5,5,'x')            
            

