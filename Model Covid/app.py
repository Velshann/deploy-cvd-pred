from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html', prediction="")

@app.route('/predict', methods=['GET', 'POST'])
def predict(): 
  cough, fever, sore, breath, head, age, gender, indication = [x for x in request.form.values()]
  data = []

  if cough == 'Ya':
    data.extend([1])
  else:
    data.extend([0])
  
  if fever == 'Ya':
    data.extend([1])
  else:
    data.extend([0])

  if sore == 'Ya':
    data.extend([1])
  else:
    data.extend([0])

  if breath == 'Ya':
    data.extend([1])
  else:
    data.extend([0])
    
  if head == 'Ya':
    data.extend([1])
  else:
    data.extend([0])

  if age == 'Ya':
    data.extend([1])
  else:
    data.extend([0])

  if gender == 'Laki-laki':
    data.extend([1])
  else:
    data.extend([0])
  
  if indication == 'Dari luar negeri':
    data.extend([0])
  elif indication == 'Kontak dengan seseorang yang terkonfirmasi positif COVID-19':
    data.extend([1])
  else:
    data.extend([2])
    
  prediction = model.predict([data])
  output = ''
  if prediction[0] == 1:
    output = 'Positif'
  else:
    output= 'Negatif'
    

  return render_template('index.html', prediction=output, cough=cough, fever=fever, sore=sore, breath=breath, head=head, gender=gender, age=age, indication=indication)



if __name__ == "__main__":
  app.run(debug=True)
