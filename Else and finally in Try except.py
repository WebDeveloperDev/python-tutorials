try:
    f=open("doex.txt")
except EOFError as e:
    print(e)
except IOError as e:
    print("io error",e )
else:
    print("This will run only if except is not running")
finally:
    print("This should be print")

print("Important stuff")