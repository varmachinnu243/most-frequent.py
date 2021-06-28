def most_frequent(str):
    d=dict()
    for i in str:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print('String letters in decreasing order of frequency:')
    for r in sorted(d,key=d.get,reverse=True):
        print(r,'=',d[r])
        
most_frequent(input('Please enter a string:'))
