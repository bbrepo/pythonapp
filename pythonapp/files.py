#OPEN A FILE
fo=open('test.txt','w')
#Get some info
print('Name:' , fo.name)
print('Is closed: ', fo.closed)
print('Opening mode: ', fo.mode)

#Write to file
fo.write('I love Python')
fo.write(' and Javascript.')

#Close file
fo.close()

#Open to append
fo=open('test.txt','a')
fo.write('I also like PHP.')
fo.close()

#Read from file
fo=open('test.txt','r+')
text=fo.read(10)
print(text)
fo.close()

#Create file
fo=open('test2.txt','w+')
fo.write('This is my new file')
fo.close()