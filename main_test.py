from main import randomnumber

def testRandomnumber():
    assert randomnumber()<=100
    print ("Fuction works as expected")

if __name__ == '__main__':
    testRandomnumber()
