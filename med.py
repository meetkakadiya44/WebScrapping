# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:41:51 2019

@author: kakad
"""

from bs4 import BeautifulSoup as bs
import urllib
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

'''
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
'''
list with name 'reallist' is prepared, which can be used to iterate all the websites
'''''''
#--------------------------------------------------------------------------------------------------------------------------------------
  #lowercasing all the characters so that it can load the list faster
     
for i in range(len(reallist)):
    reallist[i]=reallist[i].lower()
'''    
#print(reallist)    
#---------------------------------------------------------------------------------------------------------   
#this list contains all the diseases which are to be traveresed to get all The medicines



'''
 below code is used to traverse every website using the list 'reallist' 
     and then we'll just open every 'href' there is and open it
     and would open the webpage through that link obtained and extract the data of name and price
     which is yet easy said then done.
     
'''
'''
#-------------------BELOW CODE IS USED TO TRAVERSE EVERY DISEASES AND MEDICINES CONTAINED IN EACH DIESEASE-----------------------------
medlist=[]
medname=[]
s=[]
count1=1
medcount=1

z=0
for i in range(len(reallist)):
    s=make_soup("https://www.netmeds.com/prescriptions/"+ reallist[i] )
    
    try:
        p=0
        while(p<26):
            ac= s.find('div', {'id' : 'prescriptions_products'}).findAll("ul", {"class" : "alpha-drug-list"})[p]
            
            for j in ac.findAll('a',href=True):
                #print(j['href'])
                medlist.append(j['href'])
                
                #f= open('result1.txt', 'a')
                #f.write(j['href'] )
                #f.close()
                medcount=medcount+1
            
            p=p+1
            
        
        
    #------------------------- IF I GOT AN ERROR RELATED T0 WHILE LOOP WWE WOULD JUST PASS THE ERROR.--------------------------------
    except:
        print(" \n ------------------------------------------------------------- \n ")
    
    
    print(count1)
    count1 = count1 +1
    
    #print(" -------")
    #print(" ")
    
print(medcount)  #------------PRINTING THE COUNT OF ALL MEDICINES----------------------------

print(medlist) #---------------PRINTING ALL MEDICINES' URL---------------------

'''
'''
#------------------------------------------------------------------------------
f1=open('medlist.txt', 'w')
for i in medlist:
    
    f1.write(i + '\n')
f1.close
#------------------------------------------------------------------------------



f= open('mednames.text', 'w')
for i in medlist:
    ss=make_soup(i)
    
    medname1=ss.find('div', class_='product-top-essentials').h1.text
    print(medname1)
    medname.append(medname1)
    
    f.write(i + '\n')
    
    
f.close()
'''




#--------------ABOVE CODE WAS USED TO EXTRACT ALL THE WEBPAGES OF ALL THE MEDICINES AVAILABLE-------------------------------------
#--------------WHICH WE EXTRACTED INTO A FILE NAMED MEDLIST. NOW WE'LL JUST TO USE TO EXTRACT THE DATA IN EACH PAGE ACCESSING THE URLS IN MEDLIST----------------
x=0
#------ 'X' HERE IS THE LINE NUMBER OF URL, IF URLERROR OCCURS, SAY IN X=5 THE DATA STARING FROM URL'0' AND URL'4' IS SAVED AND  YOU NEED TO SET X=5 TO RESTART BUT FROM X=5--------------- 
counter=x
tab1name="THERAPEUTIC USES:-"
tab2name="WARNING & PRECAUTIONS:-"
tab3name="INTERACTIONS:-"
tab4name="DIRECTIONS FOR USE:-"
tab5name="SIDE EFFECTS:-"
tab6name="MORE INFORMATION:-"

f2=open('medlist.txt', 'r')
lines= f2.readlines()
for i in lines[x:]:
     
    s=make_soup(i)
    names=s.find('div', class_='product-top-essentials').h1.text
    price=s.find('div', class_='essential-container').find('span', class_='pull-left').find('span', class_='price').text
    print(names.lstrip())
    print(price)
    
    p=s.find('div', id_='prod_desc')
    try:
        drug=s.find('div',class_='prescript-txt')
        print(drug.h1.text)
        
        
        for j in drug.ul.find_all("li", recursive=True): 
            print (j.text)
            
        print()
        print("DESCRIPTION TABLE-------------------------------")
      
        '''/////////////////////////////////////////--TAB1--////////////////////////////////////////////////////'''
        print(tab1name)
        
        tab1 = s.find('div', class_='col-md-12').find('div', class_="inner-content")
        print(tab1.h2.text)
        
        
        try:
            print(tab1.p.text + ":")
        
        except:
            nnn=0
            
            
            
        try:
            for li1 in tab1.find_all('li', recursive=True):
                print('-' +li1.text)
        except:
            nnn=1
        '''/////////////////////////////////////////////////////////////////////////////////////////////'''
        
        
        
        
        
        
        '''/////////////////////////////////////////--TAB2--////////////////////////////////////////////////////'''
        print(tab2name)
        tab2 = s.find('div', class_='col-sm-9')

        try:
            print(tab2.p.text)
        except:
            nnn=0
        
        try:
            for li2 in tab2.find_all('li', recursive=True):
                print('-' +li2.text)
        except:
            nnn=0
           
        '''/////////////////////////////////////////////////////////////////////////////////////////////'''   
        
        
        '''/////////////////////////////////////////--TAB3--////////////////////////////////////////////////////'''
        
        print(tab3name)
        
        tab3 = s.find_all('div', class_='col-md-12')[1]
        
        
        try:
            print(tab3.p.text)
        except:
            nnn=12
            
        try:
            for li3 in tab3.find_all('li', recursive=True):
                print('-' +li3.text)
        except:
            nnn=55
        
        '''/////////////////////////////////////////////////////////////////////////////////////////////'''   
        
        
        
        '''/////////////////////////////////////////--TAB4--////////////////////////////////////////////////////'''
        
        print(tab4name)
        
        tab4 = s.find_all('div', class_='col-md-12')[2]
        
        
            
        try:
            for li4 in tab4.find_all('li', recursive=True):
                print('-' +li4.text)
                
        except:
            nnn=0
        '''/////////////////////////////////////////////////////////////////////////////////////////////'''   
       
        
        
        
        '''/////////////////////////////////////////--TAB5--////////////////////////////////////////////////////        
        print(tab5name)
        tab5 =s.find_all('div', class_='col-md-12')[2]
        
        
        print("COMMON:")
        tab5_2=tab5.find_all('div', class_="inner-content")
        
        try:
            for li5_2 in tab5_2.find_all('li', recursive=True):
                print('-' +li5_2.text)
                
        except:
            nnn=0
        
        
        
        
        print("SERIOUS:")
        tab5_1=tab5.find('div', id_="serious-side-effects").find('div', class_="inner-content")
        try:
            print(tab5_1.p.text)
        except:
            nnn=0
        
        try:
            for li5_1 in tab5_1.find_all('li', recursive=True):
                print('-' +li5_1.text)
                
        except:
            nnn=0
        
       
        
        
        
        '''
        
        
        
       
        
    except:
        nnn=0  #do nothing, just skip the non descriptive types, for the time being
    
    print(str(counter) + "---------/////////////////////////////////////")
    print()
    counter=counter+1
    

f2.close()
