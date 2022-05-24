import sys
sys.path.insert(2, 'OFA')

from flask import Flask, jsonify, request
from get_caption import predict_caption as model

from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)


def image_from_base64(b64image):
    img = Image.open(BytesIO(base64.b64decode(b64image)))
    return img

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    #img_names = ['img', 'img1', 'img2', 'img3', 'img4']
    print("received image(s)")
    outputs = []
    req_list = request.json.get('instances')
    
    for ob in req_list:
        
        key = list(ob.keys())[0]; val = list(ob.values())[0]
        print(key)
        print("preprocessing")
        
        img = image_from_base64(val)
        print("infering")
        output = model(image=img)
        print("postprocessing")
        outputs.append({key : [output]})
    
    to_return = {'predictions' : outputs}
    print(to_return)
    return jsonify(to_return)

@app.route('/healthz')
def healthz():
    return "OK"
    
@app.route('/health', methods=['GET'])
def health_check():
   return jsonify({"status": 'healthy'})

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=False) # use_reloader=False)
