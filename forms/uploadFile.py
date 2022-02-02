from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired


class UploadForm(FlaskForm):
    xml = FileField('selecciona el xml:',validators=[FileRequired()])
    submit = SubmitField('Submit')