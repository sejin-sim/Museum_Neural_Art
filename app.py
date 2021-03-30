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
      # 구름ide에서 실행 불가. cpu 터짐
      # a = str(np.random.randint(1,100))
      # content = request.files['file']
      # style = request.form.get('style')
      # content.save(os.path.join(UPLOAD_FOLDER+ '/'+a+'content.jpg'))

      # #load in content and style image
      # content = style_transfer.load_image(UPLOAD_FOLDER+'/'+a+'content.jpg')
      
      # vgg = style_transfer.model()

      # style, target, x = [0 for i in range(5)],[0 for i in range(5)],[0 for i in range(5)]

      # for i in range(0,5):
      #   # #Resize style to match content, makes code easier
      #   style[i] = style_transfer.load_image('/content/Museum_Neural_Art/static/image/s'+ str(i+1)+'.jpg', shape=content.shape[-2:])
      #   target[i] = style_transfer.stylize(content,style[i],vgg)
      #   x[i] = style_transfer.im_convert(target[i])
      #   plt.imsave(UPLOAD_FOLDER+'/'+a+'target_'+str(i)+'.png',x[i])

      # return render_template('success.html', content_file= 'image/upload/'+a+'content.jpg', t_0= 'image/upload/'+a+'target_0.png',
      #                        t_1= 'image/upload/'+a+'target_1.png', t_2= 'image/upload/'+a+'target_2.png', 
      #                        t_3= 'image/upload/'+a+'target_3.png', t_4= 'image/upload/'+a+'target_4.png')
    return render_template('success.html',
                              content_file= 'image/upload/sample/content.jpg', t_0= 'image/upload/sample/target_0.png',
                              t_1= 'image/upload/sample/target_1.png', t_2= 'image/upload/sample/target_2.png', 
                              t_3= 'image/upload/sample/target_3.png', t_4= 'image/upload/sample/target_4.png')
							
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]), debug = True)
    
    
    # 참고 1) 파일 저장 위치 (FLASK 문법)
    #      ㄴ templates -html / static : image, css, js
    #     2) 홈페이지는 상단에 동그라미 아이콘 클릭시 시작 : 여러명이 실행 시키면 구동 발생 참고
    #     3) input size = 400 x 400 이하, 풍경 사진 추천(차이가 확명하게 보임)   