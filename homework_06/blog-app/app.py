from os import getenv

from flask import Flask, request, render_template

from views.products import products_app
from models.database import db


app = Flask(__name__)
config_name = "config.%s" % getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(config_name)

app.register_blueprint(products_app, url_prefix="/products")

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.route("/")
def index_page():
    print(request.path)
    print(vars(request.url_rule))
    print(vars(request))
    return render_template("index.html")


@app.get("/hello/")
def hello_name():
    name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    return {"message": f"Hello, {name}!"}


@app.get("/items/<int:item_id>/")
def get_item(item_id: int):
    return {
        "item": {"id": item_id},
    }


@app.get("/items/<item_id>/")
def get_item_str(item_id: str):
    return {
        "item_id": item_id.upper(),
    }


def create_db():
    pass


if __name__ == "__main__":
    create_db()
    app.run(port=5000)
