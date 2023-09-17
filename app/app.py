import flask
from flask import render_template
import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)

# загружаем модель и определяем параметры функции  -  будущие входы для модели (всего 12 параметров)

def set_params(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12):

    model = keras.models.load_model("/Users/kusita_1/Desktop/final_project/saved_model/composites_model_16/")
    prediction = model.predict([param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12])

    return prediction[0][0]

@app.route('/', methods=['post', 'get'])

def app_calculation():
    param_list = []
    message = ''
    if flask.request.method == 'POST':
        
       # получим данные из форм и добавим их в список, который затем передадим функции set_params
        for i in range(1,13,1):
            param = flask.request.form.get(f'param{i}')
            param_list.append(float(param))
            
        message = set_params(*param_list)
        
    # указываем шаблон и прототип сайта для вывода    
    return render_template("/Users/kusita_1/Desktop/final_project/templates/main.html", message=message) 

# запускаем приложение  
    app.run()