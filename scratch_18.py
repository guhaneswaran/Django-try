# Error handling
# compile time  or syntax error , logical , run time errors


a = 5 # Normal statement . this has no chance of giving error
b = 0

try:
    print(a/b) # Critical statement
except Exception as e: # If we dono the exception
    print(" Not divisible by 0 - "  , e)
except ValueError as e:
    print("value error ", e) # if we know the exception
finally:
    print("Resource closed") # will get executed if we r getting exceptions are not
