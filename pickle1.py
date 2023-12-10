import pickle
countrydict={"India":2,"America":7,"Canada":4,"Russia":9,"Dubai":11,"Pakistan":8,"bangladesh":15}
fin=open("countrydict.dat",'wb')
pickle.dump(countrydict,fin)
fout=open("countrydict.dat",'rb')
print(pickle.load(fin))
print("Bye")
fout.close()
fin.close()