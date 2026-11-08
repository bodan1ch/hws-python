from flask import Flask, abort, render_template

from models import ProductModel

app = Flask(__name__)
product_model = ProductModel()


@app.get("/")
def index():
    return render_template(
        "index.html",
        products=product_model.get_all_products(),
    )


@app.get("/product/<int:product_id>")
def product_detail(product_id):
    product = product_model.get_product_by_id(product_id)
    if product is None:
        abort(404)
    return render_template("product_detail.html", product=product)


if __name__ == "__main__":
    app.run(debug=True)
