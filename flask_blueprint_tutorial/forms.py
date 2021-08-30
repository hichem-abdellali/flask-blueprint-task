from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    """Class for the main form.

    Attributes:
        Address (str): This field contained the typed address
            that will be processed in the backed.
        submit (button): the submission button
        to calculate the distance to the MKAD.
    """
    address_form = StringField(
        'Address',
        [DataRequired()]
    )
    submit = SubmitField('Calculate')
