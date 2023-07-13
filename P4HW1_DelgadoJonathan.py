#CTI-110
#P4HW1 - Score List
#Jonathan Delgado

listOfScores = []

numberOfScores = int(input("How many scores you want to enter? "))

currentNumOfScores = 0
while(True):
    
    while(currentNumOfScores<numberOfScores):
        scores = float(input('Enter score #{}: '.format(currentNumOfScores+1)))
        
        while(True):
            if(scores<0 or scores>100):
                print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
                scores = float(input('Enter score #{} again: '.format(currentNumOfScores+1)))
            
            else:
                
                listOfScores.append(scores)
                
                break
        
        currentNumOfScores+=1 
        
        
    if(currentNumOfScores==numberOfScores):
        break

minElement = min(listOfScores)

listOfScores.remove(min(listOfScores))

average = sum(listOfScores)/len(listOfScores)

if(average>=90 and average<=100):
    grade = 'A'
   
elif(average>=80 and average<=89.9):
    grade = 'B'
    
elif(average>=70 and average<=79.9):
    grade = 'C'
    
elif(average>=60 and average<=69.9):
    grade = 'D'
    
elif(average<59.9):
    grade = 'F'

print("--------------------Results----------------------")
print("Lowest Score  :",minElement)
print("Modified List :",listOfScores)
print("Scores Average:",average)
print("Grade         :",grade)
print("-------------------------------------------------")