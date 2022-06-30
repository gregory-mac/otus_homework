from flask import Flask, request, render_template
from flask_migrate import Migrate

from views.posts import posts_app

from models import Post
from models.database import db


app = Flask(__name__)
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

app.register_blueprint(posts_app, url_prefix="/posts")


@app.route("/")
def view_blog():
    posts = Post.query.all()
    return render_template("view_blog.html", posts=posts)


@app.get("/add/")
def add_post():
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
    # create_db()
    app.run(port=5000, debug=True)
