run=[] #Creating a empty list 
no_players=int(input("enter the number of the players in the team :")) 
for i in range (no_players):
    run_score=int(input("Enter the runs scored by the player "+str(i+1)+":"))
    run.append(run_score)
#code for the average score of the team
def average(run):
    print("____________________________________")
    sum=0
    for i in range (0,len(run)):
        sum+=run[i]
        avg=sum/len(run)
    print("Average score of the team is :",avg)
#code for the maximun runs scored by the players in the team
def high(run):
    print("______________________________________")
    max=run[0]
    for i in range(len(run)):
        if max<run[i]:
            max=run[i]
    print("Highest run score by the player is :",max)
#code for the minimum runs scored by the players in the team
def low(run):
    print("____________________________________")
    mim=run[0]
    for i in range(len(run)):
        if mim>run[i]:
            mim=run[i]
    print("Lowest runs scored by the player is :",mim)
#code for the runs scored more than 50 runs in the the team
def check(run): 
    print("_______________________________________")     
    count=0
    for i in range(0,len(run)):
        if run[i]>=50:
            count+=1
        else:
            pass
    print("Count of the player score more than '50' are :",count)
#code for the runs scored for higher number of the frequency
def feq(run):
    print("___________________________________")
    max=0
    result=run[0]
    for i in run:
        freq=run.count(i)
        if freq>max:
            max=freq
            result=i
            
    print(f"run scored with the highest frequncy {result} is",max)
    print("-------------'THANKYOU---------------")

average(run)
high(run)
low(run)
check(run)
feq(run)


