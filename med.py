# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:41:51 2019

@author: kakad
"""

from bs4 import BeautifulSoup as bs
import urllib.request

import string 


      





#-------------------------------------------GETTING THE URL AND SOUPIFYING THE LINK SENT--------------------------------------------------------------------------------

def make_soup(url):

    #rejecting forbidden error

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    
    request=urllib.request.Request(url,None,headers) #The assembled request
    thepage = urllib.request.urlopen(request)
    #passing to s
    soup=bs(thepage,"html.parser")
    return soup
#---------------------------------------------------------------------------------------------------------------------------


#getting website here////////////////////////-----------------
url1= "https://www.netmeds.com/prescriptions"
#/////////////////////////////////////////---------------------
soup1=make_soup(url1)





       
   #name of all dieases
j=0
names=[]
while(j<20):
    ss= soup1.find('div',{'id': 'prescriptions_products'}).findAll("ul", {"class" : "alpha-drug-list"})[j]
            
    for i in ss.findAll('a'):
        #print(i.text)
        names.append(i.text)
        
    j=j+1
  
list1=[]          
for i in names:
    result = ''.join([j for j in i if not j.isdigit()])
    list1.append(result)   
   
  # removes all numbers from above list  
    
    
    
    
    #------------------------------------------------------------------------------------------------------------

#this code below removes all the '()' from the list and replaces '/' with '-'


for i in range(len(list1)):
    for j in list1[i]:
        if j in "()":   
            f=list1[i].replace(j,'')
            list1[i]=f
    
        if j in "/":
            r=list1[i].replace(j,'-')
            list1[i]=r
        

# this code removes the last space from all the elements of list1 and append it in 'reallist' list
#  i did this because i was unable to use 'rstrip' function, "smh!"      
    
reallist=[]
    
for i in list1:
    s=len(i)
    i=i[0:s-1]
    reallist.append(i)

    
    
#let's solve the error situation of anaesthesia-local

reallist[7]="Anaesthesia-Local"
    
    
    # remove all the spaces and replace it with '-' 
    
    
for i in range(len(reallist)):
    for j in reallist[i]:
        if j in " ":   
            f=reallist[i].replace(j,'-')
            reallist[i]=f
    



'''
list with name 'reallist' is prepared, which can be used to iterate all the websites
'''
#--------------------------------------------------------------------------------------------------------------------------------------
  #lowercasing all the characters so that it can load the list faster
     
for i in range(len(reallist)):
    reallist[i]=reallist[i].lower()
        
#print(reallist)    
#---------------------------------------------------------------------------------------------------------   
#this list contains all the diseases which are to be traveresed to get all The medicines



'''
 below code is used to traverse every website using the list 'reallist' 
     and then we'll just open every 'href' there is and open it
     and would open the webpage through that link obtained and extract the data of name and price
     which is yet easy said then done.
     
'''

#-------------------BELOW CODE IS USED TO TRAVERSE EVERY DISEASES AND MEDICINES CONTAINED IN EACH DIESEASE-----------------------------
s=[]

p=0
for i in range(len(reallist)):
    s=make_soup("https://www.netmeds.com/prescriptions/"+reallist[i] )
    try:
        while(p<26):
            ac= s.find('div', {'id' : 'prescriptions_products'}).findAll("ul", {"class" : "alpha-drug-list"})[p]
           
            for j in ac.findAll('a',href=True):
                print(j['href'])
            
            p=p+1
    except:
        pass
















        
        
        
