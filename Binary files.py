import pickle

#	Writing
f= open('binary.txt','wb')
l= [1,'abgf','3456','#_-(']

pickle.dump(l,f)
f.close()

#	Reading
f= open('binary.txt','rb')
print(pickle.load(f))