import json
import base64

with open("test.jpg", 'rb') as fo:
    img_bytes = fo.read()
    img_b64 = base64.b64encode(img_bytes).decode('utf-8')

pred_dict = {"instances" : [{"img1": img_b64}] } #, {"img4" : img_b64}]}

