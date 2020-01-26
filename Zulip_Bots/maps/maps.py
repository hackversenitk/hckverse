import urllib.request, json 
from flask import Flask
import sys
import zulip

def mapme(msg):
    xy = msg.split("-")
    try:
        with urllib.request.urlopen("http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0="+str(xy[0])+"&wp.1="+str(xy[1])+"&optmz=distance&key=<BING_API_KEY>") as url:
            
            data = json.loads(url.read().decode())
            
            ret = ""
            for i in range(0,len(data['resourceSets'][0]['resources'][0]['routeLegs'][0]['itineraryItems'])-1):
                ret += "After " + str(data['resourceSets'][0]['resources'][0]['routeLegs'][0]['itineraryItems'][i]['travelDistance']*1000)+"m " + data['resourceSets'][0]['resources'][0]['routeLegs'][0]['itineraryItems'][i+1]['instruction']['text']+" (Time " + str(data['resourceSets'][0]['resources'][0]['routeLegs'][0]['itineraryItems'][i]['travelDuration'])+"s)"
    except:
        return "Path Not found"
    return ret

class MapsBotHandler(object):
    '''
    A docstring documenting this bot.
    '''

    def usage(self):
        pass

        

    def handle_message(self, message, bot_handler):
        original_content = message['content']
        result = mapme(original_content)
        bot_handler.send_reply(message, result)
        

handler_class = MapsBotHandler
