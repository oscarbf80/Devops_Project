import random
def randomnumber():
    return random.randrange(1, 100)+100  


def main():   
    print("Your random number is", randomnumber())
    
if __name__ == '__main__':
    main()
