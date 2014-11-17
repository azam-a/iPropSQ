from flask import Flask, render_template
import requests
app = Flask(__name__)


myparams = {'client_id': 'MT3VHUDOIPPIF00TPOEMOUOV550MISJG21TM0U2RUZZP42XD',
            'client_secret': 'FZI4HLHMZ1U0IKFSHESG2BLAFMOPSU1T2XUMDIAKCWV0FO3C',
            'v': '20141101',
            }
venue_id = '4b058805f964a520fbac22e3'


@app.route('/')
def hello_world():
    text_to_render = 'Hello World!'
    return render_template('hello.html', text_tag=text_to_render)


@app.route('/request001')
def request001():
    fetched = requests.get('https://api.foursquare.com/v2/venues/' + venue_id, params=myparams)
    return str(fetched.json())

if __name__ == '__main__':
    app.run(debug=True)
