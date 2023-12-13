from flask import Flask, render_template

app = Flask(__name__)
# flask cria nosso site

 # Adicione mais URLs de imagens conforme necessário
@app.route('/')
def index():
    imagens = [
        'static/solar.jpg',
        ]  
       
 # Adicione mais links conforme necessário
    links = [
        {'url': 'https://www.youtube.com/watch?v=yJE1OsT2Cdc','texto': 'Link1 do vídeo do you tube' },
        {'url': 'https://www.youtube.com/watch?v=Rvc_8CeESkg', 'texto': 'Link2 do vídeo do you tube'},

    ]
       
    # Caminho da imagem
    caminho_imagem = 'static/solar2.jpg',
    
    # Caminho da imagem
    caminho_imagem = 'static/solar3.jpg',
    

    return render_template('index.html', imagens=imagens, links=links)

    

if __name__ == '__main__':
    app.run(debug=True)