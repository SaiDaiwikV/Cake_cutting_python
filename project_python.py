Angle = 360 # This is the total angle of the cicle.

N = int(input("N: ")) # This is input form the user to divide the cake.

if (N==0) or (N==1): # This is the condition were the N is equal to 1 or 0.
    print(N,"cannot be divide the cake") # This is the output when N is Equal to 0 or 1.

else: # This is the condition were the N is more than 1.
    # This is an Nested loop.
    if (Angle%N == 0): # This is the condition when the Angle get divided N remainder equal to 0.
        print("The cake will cut into",N,"Equal parts") # This is the output for if condition.

    else: # This is the condition when reamainder not equals to 0.
        print("The cake will not cut into",N,"Equal Parts") # This is the output for else condition.

    if Angle/N != 0: # This is the condition were the angle divide by N is not equals to 0 because the cake should be cut into N parts.
        print("The cake will cut into",N,"parts") # This is the output if is True.

    else: # This condition will done if if False.
        print("The cake will not cut into",N,"parts") # This is the output if is False

    if Angle%N == 0 and Angle/N != 0: # This is the Condition weather to check after cutting cake into N parts and Checking no two pieces are not equal
        print("The cake is cutted into",N,"But all pieces are equal") # Output if is True

    else: # Condition if is False.
        print("The cake is cutted into",N,"But two pieces are not equal") # Output when else is True.