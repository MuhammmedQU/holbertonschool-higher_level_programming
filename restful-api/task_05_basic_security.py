bele sey demek isdrsen ya nece from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "secret-key"

jwt = JWTManager(app)


# users with roles
users = {
    "user1": {"password": "123", "role": "user"},
    "admin": {"password": "456", "role": "admin"}
}
  

#basic auth ucun kod  
@app.route("/basic-protected")
@auth.login_required
def basic():

    return "Basic Auth Access Granted"


@auth.verify_password
def verify(username,password):
    if username in users and users[username]["password"]==password:
        return username

# JWT ucun kod
@app.route("/login",methods=["POST"])
def login():
    data=request.json
    username = data["username"]
    password = data["password"]
    
    if username in users and users[username]["password"]==password:
        token=create_access_token(identity=username)
        return jsonify(access_token=token)
    return  jsonify({"error": "wrong credentials"}), 401





@app.route("/admin-only")
@jwt_required()
def admin_only():

    username = get_jwt_identity()

    if users[username]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify(message="Admin Access: Granted")

if __name__=="__main__":
    app.run(debug=True)
