from flask import Flask, request, jsonify

app = Flask(__name__)

# lets use dict as in-memory storage
users = {}


@app.route("/")
def home():
    return "User Management API is live"


# Create new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user_id = str(data["id"])
    users[user_id] = data
    return jsonify({"message": "User created"}), 201


# Read user
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


# Read all user
@app.route("/users", methods=["GET"])
def get_all_users():
    users_list = list(users.values())
    if users_list:
        return jsonify(users_list)
    return jsonify({"error": "No users found"}), 404


# Update user
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id in users:
        users[user_id] = request.json
        return jsonify({"message": "User updated"})
    return jsonify({"error": "User not found"}), 404


# Delete user
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
