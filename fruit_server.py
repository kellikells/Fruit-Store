from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# our index route
# ========================================== 
@app.route('/')
def index():
    return render_template("fruit_index.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
# ========================================== 
@app.route('/checkout', methods=['POST'])
def checkout():

    # print("Got Post Info")
    # print(request.form['username'])

    # save submitted info to a variable
    formData = request.form

    # adding up fruit quantity
    totalFruits = int(formData['strawberry']) + int(formData['lemon']) + int(formData['blueberry']) + int(formData['kiwi'])

    return render_template("checkout.html", formData = request.form, totalFruits = totalFruits)
    
if __name__=="__main__":
   # run our server
    app.run(debug=True) 


# =========== danger route
# ========================================== 
# @app.route('/danger', methods=['POST'])
# def create_user():
#     print("a user tried to visit /danger.  we have redirected the user to /")

#     # redirects back to the '/' route
#     return redirect('/')
# if __name__=="__main__":
#     # run our server
#     app.run(debug=True) 
  

