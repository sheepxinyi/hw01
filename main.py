for i in range(1,10):
    for j in range(1,10):
        if i>=j:
            print('%s*%s=%s' %(j,i,i*j),end='  ')
    print()
