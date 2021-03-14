# Import Dependencies
from flask import Flask
import pandas as pd 

### FLASK INSTANCE ##
app = Flask(__name__)

# Home Page
@app.route('/machine_learning')
def machine_learning(): 
    return 'ML page'



    




if __name__ == "__main__":
    app.run(debug=True)