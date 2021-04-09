from flask import Flask , render_template ,request
import os, sys
import matplotlib.pyplot as plt
import style_transfer
from flask import Flask, url_for, redirect, render_template, request
from flask_ngrok import run_with_ngrok
import os
import time
import numpy as np

TEMPLATE_FOLDER = '/content/Museum_Neural_Art/templates' 
STATIC_FOLDER = '/content/Museum_Neural_Art/static'
app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder = STATIC_FOLDER)
run_with_ngrok(app)   #starts ngrok when the app is run

UPLOAD_FOLDER = '/content/Museum_Neural_Art/static/image/upload'
style =""
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/success", methods=['POST'])
def upload_file():
      a = str(np.random.randint(1,100))
      content = request.files['file']
      style = request.form.get('style')
      content.save(os.path.join(UPLOAD_FOLDER+ '/'+a+'content.jpg'))

      #load in content and style image
      content = style_transfer.load_image(UPLOAD_FOLDER+'/'+a+'content.jpg')
      
      vgg = style_transfer.model()

      style, target, x = [0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)]

      for i in range(0,5):
        # #Resize style to match content, makes code easier
        style[i] = style_transfer.load_image('/content/Museum_Neural_Art/static/image/s'+ str(i+1)+'.jpg', shape=content.shape[-2:])
        target[i] = style_transfer.stylize(content,style[i],vgg)
        x[i] = style_transfer.im_convert(target[i])
        plt.imsave(UPLOAD_FOLDER+'/'+a+'target_'+str(i)+'.png',x[i])

      return render_template('success.html', content_file= 'image/upload/'+a+'content.jpg', t_0= 'image/upload/'+a+'target_0.png',
                             t_1= 'image/upload/'+a+'target_1.png', t_2= 'image/upload/'+a+'target_2.png', 
                             t_3= 'image/upload/'+a+'target_3.png', t_4= 'image/upload/'+a+'target_4.png')

# 다시하기 버튼 만들기
@app.route("/restart")
def restart():
  os.remove(UPLOAD_FOLDER+ '/'+a+'content.jpg')
  os.remove(UPLOAD_FOLDER+ '/'+a+'target.png')
  return render_template("index.html") 

if __name__ == '__main__':
    app.run()
