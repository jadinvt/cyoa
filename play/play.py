import os
def get_adventures():
    adventures = []
    """Return a list of available adventures."""
    for file in os.listdir('saved_adventures'):
        if file.split('.')[-1] == 'adv':
            adventures.append(file)
    return adventures

    
if __name__ == '__main__':
    print ("Running from command line.")
    print ("Available adventures:")
    for adventure in get_adventures():
        print (adventure)
