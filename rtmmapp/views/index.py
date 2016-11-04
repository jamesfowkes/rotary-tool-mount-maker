from io import BytesIO

from flask import render_template, flash, send_file

from rtmmapp.blueprints import index_blueprint
import rtmmapp.util.util
import rtmmapp.util.svg

from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    outer_diameter = DecimalField('Diameter of lip (outside)', validators=[DataRequired()])
    inner_diameter = DecimalField('Diameter of lip (inside)', validators=[DataRequired()])
    base_diameter = DecimalField('Diameter of base', validators=[DataRequired()])
    material_thickness = DecimalField('Thickness of your material', validators=[DataRequired()])
    
    submit = SubmitField("Get my SVG")

def package_svg_for_send(svg_content):
    strIO = BytesIO(bytes(svg_content, "utf-8"))
    return send_file(strIO, attachment_filename="rotary_tool_mount.svg", as_attachment=True)

@index_blueprint.route("/", methods=["GET", "POST"])
def show_index_page():

    input_form = InputForm()

    if input_form.validate_on_submit():
        error = rtmmapp.util.util.validate_diameters(input_form.outer_diameter.data, input_form.inner_diameter.data, input_form.base_diameter.data)
        if error is None:
            svg_content = rtmmapp.util.svg.create_rotary_tool_holder(
                float(input_form.outer_diameter.data), float(input_form.inner_diameter.data),
                float(input_form.base_diameter.data), float(input_form.material_thickness.data),
                rtmmapp.util.util.get_help_text())
            return package_svg_for_send(svg_content)

        else:
            flash("Error! " + error)

    return render_template("index.template.html", form=input_form)
