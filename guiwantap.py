# hello_psg.py
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "XAskX1IiTe2AebXN5AATdetNfKTx2ABG"
# Very basic window.
# Return values using
# automatic-numbered keys

def main(values):
    info = "Submitted"
    space1 = "\n"
    info += space1
    url = main_api + urllib.parse.urlencode({"key":key, "from":values['orig'], "to":values['dest']})
    info += url
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        APISTATUS=" \n API Status: " + str(json_status) + " = A successful route call.\n"
        info += APISTATUS
        border= "================================================="
        info += border
        direk= " \n Directions from " + (values['orig']) + " to " + (values['dest'])
        info += direk
        duration = "\n Trip Duration: " + (json_data["route"]["formattedTime"])
        info += duration
        kilo="\n Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)) 
        info += kilo
        space2 = "\n" 
        info += space2 
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            narrative=(each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")
            info += narrative
        border2= "\n =================================================" 
        info += border2
        
    elif json_status == 402:
        asterisk1= "\n ********************************************** \n"
        info += asterisk1
        ErrorSC="\n Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations."
        info += ErrorSC        
        asterisk2= "\n ********************************************** \n"
        info += asterisk2
    
    elif json_status == 611:
        asterisk3= "\n ********************************************** \n"
        info += asterisk3
        ErrorSC1="\n Status Code: " + str(json_status) + "; Missing an entry for one or both locations."
        info += ErrorSC1
        asterisk5= "\n ********************************************** \n"
        info += asterisk5


    
    else:
        asterisk4= "\n ********************************************** \n"
        info += asterisk4
        ErrorSC3="\n For Staus Code: " + str(json_status) + "; Refer to:"
        info += ErrorSC3
        prnturl= "https://developer.mapquest.com/documentation/directions-api/status-codes"
        info += prnturl

       
    return info

    


while True:
    event, values = window.read()
    if event == 'Submit':
        sg.popup('RESULTS',main(values))
    elif event == 'Cancel':
        exit()
window.close()



