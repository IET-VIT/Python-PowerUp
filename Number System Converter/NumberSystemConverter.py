from flask import Flask, render_template, request
 
# instance of flask application
app = Flask(__name__)
 
# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return render_template('index.html', conversions={})

@app.route("/convert", methods=['POST'])
def converter():
    if request.method=='POST':
        result = request.form
        conversions = {}
        conversions["Decimal"] = int(result["decimal"])
        conversions["Binary"] = bin(int(result["decimal"]))
        conversions["Hexadecimal"] = hex(int(result["decimal"]))
        conversions["Octal"] = oct(int(result["decimal"]))
        return render_template("index.html", conversions=conversions)
    

if __name__ == '__main__':  
   app.run(debug=True)