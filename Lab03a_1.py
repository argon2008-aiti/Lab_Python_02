Tel_Number = raw_input("Enter: ")  #ask user to input telephone number as save to Tel_Number

encrypted_Tel = ''                 #result of encryption

for digit in Tel_Number:
  
    Tel_Number = int(Tel_Number)    #convert Tel_Number to type 'int' so that it can accept arithmetic operations
    
    last_Digit = Tel_Number%10      #get the last_Digit of Tel_Number
    
    encrypted_Tel = encrypted_Tel + str(last_Digit) #add the last digit to the encrypted_Tel buffer
    
    Tel_Number = str((Tel_Number-last_Digit)/10) #remove the last digit in Tel_Number; Tel_Number shortened by 1 digit

print

print 'encrypted number is: '

print encrypted_Tel                             # print the encrypted number  