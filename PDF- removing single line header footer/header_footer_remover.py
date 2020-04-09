"""
!pip install bs4
!pip install fuzzywuzzy
!pip install tika 
"""

#Check if two strings match 
def matcher(Str1,Str2):
  from fuzzywuzzy import fuzz  #Fuzzywuzzy is modified version of 'levenshtein distance' to check similarity of strings
  Partial_Ratio = fuzz.partial_ratio(Str1.lower(),Str2.lower())
  Token_Sort_Ratio = fuzz.token_sort_ratio(Str1,Str2)
  if (Token_Sort_Ratio>80) : 
    return 1
  else :
    if Partial_Ratio>85 :  
      return 1
    else :
      return 0

import tika
tika.initVM()
from tika import parser
parsed = parser.from_file('/content/brain.pdf', xmlContent=True)   #Input your PDF file here
content= parsed["content"]
#print(content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(content)
divs = soup.findAll("div", { "class" : "page" })

texts= {}             #stores header and footers
noOfPages=0
for div in divs:
    noOfPages=noOfPages+1
    inner_text = div.text
    strings = inner_text.split("\n")
    for i in range(0,8):  #Considering 1st four non-empty texts of each page (Spaces exists after each text)
      if(len(strings[i])>1):  #it's a non-empty string
        #print(strings[i])     #print that non-empty string
        if(len(texts)==0):    #initial hashmap is empty
           texts[strings[i]]=1
           continue
        f=0                   #flag to check if string found in hashmap
        for x in texts:
          if(matcher(x,strings[i])==1): #texts already exist in hashmap
            texts[x]=texts[x]+1
            f=1                #setting the flag
            break
        if f==0:
          texts[strings[i]]=1

header_footer=[]
temp=0
if noOfPages==1:
  for x in texts:
     header_footer.append(x)
     temp=temp+1
     if(temp==2):
       break

elif noOfPages==2:                 #If we have 2 page pdf and 1st page doesn't have header/footer. It'll not work. So we'll paas only 2nd page to algo
  for x in texts :
      if(texts[x]==2):             #havent' taken '==1' since do want to take any risk loosing my actual content of pdf
        header_footer.append(x)
elif noOfPages==3:
  for x in texts :
      if(texts[x]>=2):            
        header_footer.append(x)
elif noOfPages>=4:
 for x in texts :
    if(texts[x]>=3):
     #print(x,texts[x])      #print header/footer and their count
     header_footer.append(x)

#print(header_footer)
     
#Delete headers and footers from entire content extracted
final_text=''
for div in divs:
    inner_text = div.text
    strings = inner_text.split("\n")
    for i in range(0,8):  #Considering 1st four non-empty texts of each page (Spaces exists after each text)
      if(len(strings[i])>1):  #it's a non-empty string
        for hf in header_footer:
          if(matcher(hf,strings[i])==1): #string extracted is a header or footer
             strings.remove(strings[i])
    
    for x in strings:
      final_text= final_text+"\n"+x

print(final_text)

