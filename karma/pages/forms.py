from flask_wtf import FlaskForm
from wtforms.validators import  DataRequired, EqualTo
from wtforms import StringField, SubmitField, PasswordField, IntegerField, TextAreaField, SelectField, EmailField, DateTimeLocalField, HiddenField
from flask_wtf.file import FileField, FileAllowed


dr = DataRequired()

choice = [('0', 'Select State'), ('1', 'Uttar Pradesh'), ('2', 'Rajasthan'), ('3', 'Delhi'), ('4', 'Haryana'), ]

class LoginForm(FlaskForm):

    email = EmailField("Email", validators=[dr], render_kw={"placeholder":"Email"})
    password = PasswordField("Password", validators=[dr], render_kw={"placeholder":"Password"})
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[dr], render_kw={"placeholder": "Username"})
    email = EmailField("Email", validators=[dr], render_kw={"placeholder": "Email"})
    address = TextAreaField("Address", validators=[dr], render_kw={"placeholder": "Address"})
    password = PasswordField("Password", validators=[dr, EqualTo('confirmpassword', message='Password Must Match')],
                           render_kw={"placeholder": "Password"})
    confirmpassword = PasswordField("Confirm Password", validators=[dr], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField("Register")

class ProductForm(FlaskForm):

    producttype = StringField("type", validators=[dr], render_kw={"placeholder":"Product Type(hoodie/tshirt)"})
    productname = StringField("name", validators=[dr], render_kw={"placeholder":"Product Name"})
    price = IntegerField("Price", validators=[dr], render_kw={"placeholder":"Product Price"})
    originalprice = IntegerField("originalprice", validators=[dr], render_kw={"placeholder":"Product Original Price"})
    stock = IntegerField("stock", validators=[dr], render_kw={"placeholder":"Product Stock"})
    image = FileField('Product Image', validators=[dr, FileAllowed(['jpg', 'png', 'jpeg'])])
    productcategory = StringField("category", validators=[dr], render_kw={"placeholder":"Product Category"})
    submit = SubmitField("Add Product")

class HotDealsProduct(FlaskForm):
    producttype = StringField("type", validators=[dr], render_kw={"placeholder": "Product Type(hoodie/tshirt)"})
    productname = StringField("name", validators=[dr], render_kw={"placeholder": "Product Name"})
    price = IntegerField("Price", validators=[dr], render_kw={"placeholder": "Product Price"})
    originalprice = IntegerField("originalprice", validators=[dr], render_kw={"placeholder": "Product Original Price"})
    stock = IntegerField("stock", validators=[dr], render_kw={"placeholder": "Product Stock"})
    image = FileField('Product Image', validators=[dr, FileAllowed(['jpg', 'png', 'jpeg'])])
    endDate = DateTimeLocalField("End Date", render_kw={'placeholder': 'Release Date'}, format='%Y-%m-%dT%H:%M')
    submit = SubmitField("Add Product")


class AddressForm(FlaskForm):

    name = StringField("Name", validators=[dr], render_kw={"placeholder": "Name"})
    mobile = StringField("Mobile", validators=[dr], render_kw={"placeholder": "Mobile Number"})
    payment = HiddenField("payment")
    pincode = IntegerField("Pincode",validators=[dr], render_kw={"placeholder": "Pin Code"})
    address = TextAreaField("address", validators=[dr], render_kw={"placeholder": "Address"})
    city = StringField("City", validators=[dr], render_kw={"placeholder": "City/District/Town"})
    landmark = StringField("Landmark", render_kw={"placeholder": "Landmark(optional)"})
    alternatemobile = StringField("Landmark", render_kw={"placeholder": "Alternate Mobile(optional)"})
    # state = SelectField("state", validators=[dr], render_kw={"placeholder": "State"}, choices=choice)
    state = StringField("state", validators=[dr], render_kw={"placeholder": "State"})
    submit = SubmitField("ADD AND DELIVER HERE")


class TrackingForm(FlaskForm):

    orderid = StringField(validators=[dr], render_kw={"placeholder": "Order ID"})
    email = StringField(render_kw={"placeholder": "Billing Email Address"})
    submit = SubmitField("Track Order")
