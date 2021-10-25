import json
import matplotlib.pyplot as plt
import os

# load the tweets from json files into a list
chinagdp = []
with open('chinagdp.json') as f:
        china = f.read()
        chinagdp += json.loads(china)
xs = []
chigdpy = []
for line in chinagdp:
        xs.append(line['date'])
        chigdpy.append(line['value'])
xs.reverse()
chigdpy.reverse()

indiagdp = []
with open('indiagdp.json') as f:
        india = f.read()
        indiagdp += json.loads(india)
indgdpy = []
for line in indiagdp:
        indgdpy.append(line['value'])
xs.reverse()
indgdpy.reverse()


import numpy
fig, ax = plt.subplots()
ax.bar(xs, chigdpy, label= 'China')
ax.bar(xs, indgdpy, label = 'India')
plt.title('China vs India GDP (USD)')    #to add a title
plt.xlabel('Year') #x axis label
plt.xticks(rotation=25) #to rotate the bar labxwels
plt.xticks(numpy.arange(0, len(xs)+1, 5)) #to change the frequency of the bar labels
plt.ylabel('GDP (USD)') #y axis label
plt.legend()
plt.show()


chinapop = []
with open('chinapop.json') as f:
        chinap = f.read()
        chinapop += json.loads(chinap)
x = []
chipopy = []
for line in chinapop:
        x.append(line['date'])
        chipopy.append(line['value'])
x.reverse()
chipopy.reverse()

indiapop = []
with open('indiapop.json') as f:
        indiap = f.read()
        indiapop += json.loads(indiap)

indpopy = []
for line in indiapop:
        indpopy.append(line['value'])
indpopy.reverse()

plt.plot(x,chipopy, label ='China')
plt.plot(x,indpopy, label ='India')
plt.title('China vs India Population')    #to add a title
plt.xlabel('Year') #x axis label
plt.xticks(rotation=25) #to rotate the bar labxwels
plt.xticks(numpy.arange(0, len(xs)+1, 5)) #to change the frequency of the bar labels
plt.ylabel('Population') #y axis label
plt.legend() #this is to add a legend (labels are assigned when data was plotted)
plt.show()



