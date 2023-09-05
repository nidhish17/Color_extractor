from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileSize, FileRequired, FileAllowed
from wtforms import SubmitField, IntegerField
from wtforms.validators import NumberRange


class ImageUploadForm(FlaskForm):
    image = FileField("Image", validators=[FileSize(max_size=16 * 1024 * 1024), FileRequired(),
                                           FileAllowed(["jpg", "png", "jpeg"],
                                                       'Images only!  JPG PNG JPEG')])
    quantity = IntegerField("Color Quantity", validators=[NumberRange(min=1, max=50)], default=10)
    submit = SubmitField("Upload")
