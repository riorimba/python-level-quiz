score = 0
score = int(score)

#user
name = input("Hello, Enter user name to start Level Quiz? \n")
name = name.title()
print("""Hello {}, Enter the number for the correct answer
Good luck!""".format(name))

#EasyQuestion1
print("""What continent is Germany on?
1. Africa 
2. Asia 
3. Europe 
4. Australia""")

#the correct answer
easyQuestion1 = 3

#to check if user input numbers other than 1-4 
easyResponse1 = 0
easyResponse1 = input("Your answer: ")
easyResponse1 = int(easyResponse1)
while easyResponse1 >4 or easyResponse1<=0:
    print("Sorry, Input number must be 1 to 4")
    easyResponse1 = input("Your answer: ")
    easyResponse1 = int(easyResponse1)

#to assess the answer is right or wrong and add a score value
if (easyResponse1 != easyQuestion1):
    score = score
else:
    score = score + 50

#EasyQuestion2
print("""which continent is Indonesia located on?
1. South America 
2. North America 
3. Asia 
4. Europe""")

#the correct answer
easyQuestion2 = 3

#to check if user input numbers other than 1-4
easyResponse2 = 0
easyResponse2 = input("Your answer: ")
easyResponse2 = int(easyResponse2)
while easyResponse2 >4 or easyResponse2<=0:
    print("Sorry, Input number must be 1 to 4")
    easyResponse2 = input("Your answer: ")
    easyResponse2 = int(easyResponse2)

#to assess the answer is right or wrong and add a score value
if (easyResponse2 != easyQuestion2):
    score = score
else:
    score = score + 50

#display score
print("Your score is " + str(score))

#mediumQuiz must be have score more than 50
if(score>50):

    #to check if user want to continue
    medium = "yes"
    responseMedium = input("do you want to continue to medium quiz?(yes/no)\n")
    if(responseMedium == medium):

        #reset score
        score = 0
        score = int(score)
        print("Medium Quiz, Score back to 0")

        #mediumQuestion1
        print("""what ocean is west of the continent of australia?\n"""
        """1. Indian Ocean\n"""
        """2. Pacific Ocean\n"""
        """3. Atlantic Ocean\n"""
        """4. Artic Ocean""")

        #the correct answer
        mediumQuestion1 = 1

        #to check if user input numbers other than 1-4
        mediumResponse1 = 0
        mediumResponse1 = input("Your answer: ")
        mediumResponse1 = int(mediumResponse1)
        while mediumResponse1 >4 or mediumResponse1<=0:
            print("Sorry, Input number must be 1 to 4")
            mediumResponse1 = input("Your answer: ")
            mediumResponse1 = int(mediumResponse1)

        #to assess the answer is right or wrong and add a score value
        if (mediumResponse1 != mediumQuestion1):
            score = score
        else:
            score = score + 50

        #mediumQuestion2
        print("""what ocean is west & east of indonesia?\n"""
        """1. Pacific Ocean & Atlantic Ocean\n"""
        """2. Indian Ocean & Pacific Ocean\n"""
        """3. Atlantic Ocean & Artic Ocean\n"""
        """4. Artic Ocean & Indian Ocean""")

        #the correct answer
        mediumQuestion2 = 2

        #to check if user input numbers other than 1-4
        mediumResponse2 = 0
        mediumResponse2 = input("Your answer: ")
        mediumResponse2 = int(mediumResponse2)
        while mediumResponse2 >4 or mediumResponse2<=0:
            print("Sorry, Input number must be 1 to 4")
            mediumResponse2 = input("Your answer: ")
            mediumResponse2 = int(mediumResponse2)

        #to assess the answer is right or wrong and add a score value
        if (mediumResponse2 != mediumQuestion2):
            score = score
        else:
            score = score + 50

        #display score
        print("Your medium quiz score is " + str(score))
        print("Thank you for answering all quiz")
    #if user not going to medium score
    else:
        print("goodbye {}!".format(name))

#if user fail pass minim score easyquiz
else:
    print("Thank you for answering {}, sorry you haven't been able to enter the medium question.\n"""
    """Please try again""".format(name))
