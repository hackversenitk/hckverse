import urllib.request, json 
from flask import Flask
import sys
import zulip

def nearme(msg):
    xy = msg.split("-")
    try:
        with urllib.request.urlopen("https://dev.virtualearth.net/REST/v1/LocalSearch/?query="+str(xy[2])+"&userLocation=47.6062,-122.3321&key=<BING_API_KEY>") as url:
            ret = {}
            try:
                data = json.loads(url.read().decode())
            except:
                 pass
            try:
                ret["Name"] = data["resourceSets"][0]["resources"][0]["name"]
            except:
                ret["Name"] = "Not Found"
            try:
                ret["Address"] = data["resourceSets"][0]["resources"][0]["Address"]["formattedAddress"]
            except:
                ret["Address"] = "Not Found"
            try:
                ret["Phone Number"] = data["resourceSets"][0]["resources"][0]["PhoneNumber"]
            except:
                ret["Phone Number"] = "Not Found"
    except:
        return {"Name": "Not Found", "Address": "Not Found", "Phone Number": "Not Found"}
    return ret

class NearbyBotHandler(object):
    '''
    A docstring documenting this bot.
    '''

    def usage(self):
        pass

        

    def handle_message(self, message, bot_handler):
        original_content = message['content']
        result = nearme(original_content)
        bot_handler.send_reply(message, result)
        

handler_class = NearbyBotHandler
