from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{

  'id' : 1,
  'title': 'Data Analyst',
  'location': 'Bengalaru, India',
  'salary': '1,00,000',
},
  {'id' : 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': '1,50,000',
  
},
  {'id' : 3,
    'title': 'Front End Engineer',
    'location': 'Remote',
    

  }, 

    {'id' : 4,
      'title': 'Backend Engineer',
      'location': 'San Fransisco, USA',
      'salary': '120,000',

    }]

@app.route("/")
def home():
    return render_template ("home.html", jobs=JOBS, company_name = 'Jovian')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)
if  __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)