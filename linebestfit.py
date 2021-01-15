def linebestfit(x,y):
    import statistics as st
    sxy=0
    for index, i in enumerate(x):
        p=i*y[index]
        sxy+=p
        sxsyn=sum(x)*sum(y)/len(x)
        ar=sxy-sxsyn
        sx2o
        for i in x:
            sx2+=i**2
            sumx2=sum(x)**2/len(x)
            par=sx2-sumx2
            m=ar/par
            b=st.mean(y)-m*st.mean(x)
            return m,b
