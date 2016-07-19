import requests # import library "requests"
domainName = 'http://qualityassurance.pro' #Let's set the domain in variable "domainName"
request = requests.get(domainName) #set requests.get to open the existing domain https://nedko.info
if request.status_code == 200: #If the resource return status code 200 (success)
    print('Woohoo - the web site ',domainName,' exists') #Print success message
else: #or
    print('Not cool - the web site ',domainName,' seems that does not exist') #Print unsuccessful message
print ("") #Print empty line
print('Status code: ',request.status_code) #Print returned status code here 


# Expected result:

# >python example.py
# Woohoo - the web site  http://qualityassurance.pro  exists
#
# Status code:  200