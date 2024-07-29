with open("DATA.txt","a+") as cv:
    cv.writelines(['hi','hello','python'])
    cv.writelines(["\nWelcome","Progrmming"])
    print(cv.readlines())
    cv.close()
