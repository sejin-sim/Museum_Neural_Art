from flask import Flask , render_template ,request
import os, sys
import matplotlib.pyplot as plt
import style_transfer

app = Flask(__name__)
UPLOAD_FOLDER = './static/image/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
style =""
@app.route("/")
def home():
	return render_template("index.html")


@app.route("/success", methods=['POST'])

def upload_file():
			content = request.files['file']
			style = request.form.get('style')
			content.save(os.path.join(app.config['UPLOAD_FOLDER'], 'content.jpg'))
			#load in content and style image
			content = style_transfer.load_image('./static/image/upload/content.jpg')
		 	#Resize style to match content, makes code easier
			style = style_transfer.load_image('./static/image/s'+ style+'.jpg', shape=content.shape[-2:])
			vgg = style_transfer.model()
			target = style_transfer.stylize(content,style,vgg)
			x = style_transfer.im_convert(target)
			plt.imsave(app.config['UPLOAD_FOLDER']+'target.png',x)

			return render_template('success.html')

							
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
