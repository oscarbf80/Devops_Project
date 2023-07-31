from main import randomnumber

def testRandomnumber():
    try:
        assert(randomnumber()<=100)
        print ("Fuction works as expected")
    except AssertionError as msg:
        print("There is an issue with the fucntion")
    
if __name__ == '__main__':
    testRandomnumber()
