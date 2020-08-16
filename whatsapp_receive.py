from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse



app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
            print(quote)
        else:
            quote = '.'
        msg.body(quote)
        responded = True
    if 'math' in incoming_msg:
        pass
        
        responded = False
    if not responded:
        msg.body(incoming_msg )
        
        
        mess=incoming_msg
        file1 = open("myfile.txt","a+") 
        
  
 

        file1.writelines(mess) 
        file1.write("\n")
        file1.close()
      
    return str(resp)




if __name__ == '__main__':
    app.run(port=5000)