import requests # import library "requests"
domain = 'http://qualityassurance.pro' #Let's set the domain in variable "domain"
request = requests.get(domain) #set requests.get to open the existing domain https://nedko.info
if request.status_code == 200: #If the resource return status code 200 (success)
    print('Woohoo - the web site ',domain,' exists') #Print success message
else: #or
    print('Not cool - the web site ',domain,' seems that does not exist') #Print unsuccessful message
print ("") #Print empty line
print('Status code: ',request.status_code) #Print returned status code here


# Expected result:

# >python example.py
# Woohoo - the web site  http://qualityassurance.pro  exists
#
# Status code:  200