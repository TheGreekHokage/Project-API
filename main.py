# import subprocess

# Run the pip install command
# subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Your main script code goes here
# Import Dependencies
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# define application and database variables
app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
app_version = "v1/"


# create the data definition
# I took what we had from class with likes and dislikes and changed them to hp and attack
class MonsterModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)

    # outputs to log/screen to verify data visually
    def __repr__(self):
        return f"Monster(name = {name}, attack = {attack}, hp = {hp})"


# run this statement the first thme to create the database structure
db.create_all()
# handle the incoming data request with a parser
# arguments for a put request
monster_put_args = reqparse.RequestParser()
monster_put_args.add_argument(
    "name", type=str, help="Name of the monster is required", required=True
)
monster_put_args.add_argument(
    "attack", type=int, help="attacks of the monster", required=False
)
monster_put_args.add_argument("hp", type=int, help="hp of the monster", required=False)

# arguments for an update request
monster_update_args = reqparse.RequestParser()
monster_update_args.add_argument(
    "name", type=str, help="Name of the monster is required"
)
monster_update_args.add_argument("attack", type=int, help="attacks of the monster")
monster_update_args.add_argument("hp", type=int, help="hp of the monster")

# Map the types to columns extracted from the database object
resource_fields = {
    "id": fields.String,
    "name": fields.String,
    "attack": fields.Integer,
    "hp": fields.Integer,
}


# Set up the Resource Functions for CRUD
class Monster(Resource):

    # GET (READ in CRUD)
    # @marshal_with serializes output from the DB as a dictionary (json object) so we can work with it in python
    @marshal_with(resource_fields)
    def get(self, monster_id):
        result = MonsterModel.query.filter_by(id=monster_id).first()
        if not result:
            abort(404, message="Could not find monster with that id")
        return result

    # POST (CREATE in CRUD)
    @marshal_with(resource_fields)
    def put(self, monster_id):
        args = monster_put_args.parse_args()
        result = MonsterModel.query.filter_by(id=monster_id).first()
        if result:
            abort(409, message="Monster ID taken...")

        monster = MonsterModel(
            id=monster_id, name=args["name"], attack=args["attack"], hp=args["hp"]
        )
        db.session.add(monster)
        db.session.commit()
        return Monster, 201

    # PUT (UPDATE in CRUD)
    @marshal_with(resource_fields)
    def patch(self, monster_id):
        args = monster_update_args.parse_args()
        result = MonsterModel.query.filter_by(id=monster_id).first()
        if not result:
            abort(404, message="Monster doesn't exist, cannot update")

        if args["name"]:
            result.name = args["name"]
        if args["attack"]:
            result.attack = args["attack"]
        if args["hp"]:
            result.hp = args["hp"]

        db.session.commit()

        return result, 200

    # DELETE (DELETE in CRUD)
    def delete(self, monster_id):
        abort_if_monster_id_doesnt_exist(monster_id)
        del monsters[monster_id]
        return "", 204


# Register the Resource called monster to the API (remember to change versions when making changes for submission)
api.add_resource(Monster, "/" + app_version + "monster/<int:monster_id>")

# Run the API body
if __name__ == "__main__":
    app.run(debug=True)

# now I have to do the same for the Get and push ones
