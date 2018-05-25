from flask import Flask, request, redirect, url_for
import base64

# Reference: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/

UPLOAD_FOLDER = '/static/photos'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def first_page():
    return redirect("/static/WEBPhoto.html", code=302)

@app.route('/uploadphoto', methods=['GET', 'POST'])
def upload_photo():
    
    if request.method == 'POST':
        print('Uploading...')
        print(request.method)
        print(request.mimetype)
        #print(request.get_json())

        #imgData = request.form.get('pic')
        #imgData = request.form
        #imgData = request.get_json(force=True, silent=False)
        imgData = request.get_data()

        #imgData = request.content

        print(imgData)
        
        print('Gravando...')
        
        arquivo = open('fotinho.png','wb') #write binary
        #arquivo.write(base64.decodestring(imgData)) 
        #arquivo.write(base64.b64decode(imgData)) 
        arquivo.write(imgData) 


        arquivo.close()
    
    return 'OK' #Usar Return

