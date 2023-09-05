from base64 import b64encode
from flask import Flask, request, render_template, redirect, url_for, flash
from forms import ImageUploadForm
from img_color_extractor import color_extractor
import random
import os



app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('secret_key')
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024


@app.route("/", methods=["GET", "POST"])
def homePage():
    form = ImageUploadForm()
    if request.method == "POST" and form.validate_on_submit():
        if form.image.data:
            img_file = form.image.data
            byte_img = img_file.read()
            color_count = form.quantity.data

            img_b64 = b64encode(byte_img).decode("utf-8")

            ten_colors = color_extractor(img_file,  color_count)

            if ten_colors == "error":
                flash("Invalid Image")
                return redirect(url_for("homePage"))

            random_border_color = random.choice(["light", "warning",  "danger", "success", "info", "primary", "secondary"])


            return render_template("index2.html", colors=ten_colors[0], form=form, image= img_b64, randomb_color=random_border_color, dominant_color=ten_colors[1])
        else:
            flash("No image selected")
            return redirect(url_for("homePage"))


    return render_template("index2.html", form=form)


if __name__ == "__main__":
    app.run(debug=False, threaded=True)

