  # name: keteku yayra kofi
  #Part II of Lab_Python_02 """
# 5.
print "question 5."
print
theInput = raw_input("Enter an integer: ")

if int(theInput)%2 == 0:
    print "even"

else:
    print "odd"

print "-----------------------------------------------------------------------------------------"
# 6.
print "question 6."
print
primarySchoolAge = 6

legalVotingAge  = 18

AgeForPresident = 40

retirementAge = 60

personAge = raw_input("Enter an age: ")

if personAge < primarySchoolAge:
    print "Too young"

elif personAge >= legalVotingAge:
    print "Remember to vote"

elif 1:
    if personAge >= AgeForPresident:
        print "Vote for me"
    else:
        print " You can't be president"

elif personAge >= retirementAge:
    print "Too old"
print
print "-----------------------------------------------------------------------"   
# 7.
print "question 7."
print
for i in range(40)[::-1]:
    if i%3==0:
        print i,

print
print "--------------------------------------------------------------------------"
# 8.
print "question 8."
print
for i in range(6,30):
    if (i%2)and(i%3)and(i%5):
        print i
print
print "---------------------------------------------------------------------------"
# 9.
print "question 9."
n = 2
while 1:
    if (79*n)%97 == 1:
        print "smallest integer: ",n
        break
    n = n + 1
print


