from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextField
from wtforms.validators import Required, Email

class AddCandidateForm(FlaskForm):
    name = TextField(
        'Name',
        validators=[Required()])

    address = TextField(
        'Address',
        validators=[Required()])

    qualification = TextField(
        'Qualification',
        validators=[Required()])

    jobskill = TextField(
        'JobSkill',
        validators=[Required()])
		
    yearsofexperience = TextField(
        'YearsOfExperience',
        validators=[Required()])


class AddJobForm(FlaskForm):
    clientname = TextField(
        'ClientName',
        validators=[Required()])

    jobprofile = TextField(
        'JobProfile',
        validators=[Required()])

    jobrequirements = TextField(
        'JobRequirements',
        validators=[Required()])


class AddCustomerForm(FlaskForm):
    name = TextField(
        'Name',
        validators=[Required()])

    address = TextField(
        'Address',
        validators=[Required()])