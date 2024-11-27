
# countdown function
def toTheMoon(countdown):
    # count down to zero
    for i in range(countdown, -1, -1):
        print("{}...".format(i))
    
    print("BLAST OFF!!!!")


toTheMoon(10)