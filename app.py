from flask import Flask, render_template, jsonify

app =Flask(__name__)
product_id = [
  { 'Part_number': "LFHP12021",
    'Part_name': "Tiger",
    'Tested_at' : "ICT-05",
   'Failure_type': "Analog_test"
   },
  { 'Part_number': "LFHP12025",
    'Part_name': "Bonnville",
    'Tested_at' : "ICT-02",
   'Failure_type': "Short test"
   },
  { 'Part_number': "LFHP4134",
    'Part_name': "Scrambler",
    'Tested_at' : "ICT-01",
   'Failure_type': "Boundary scan test"
   }
]
@app.route("/")
def hello_world():
  return render_template('home.html', product= product_id)


@app.route("/api/product")
def info():
  return jsonify(product_id)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True )
