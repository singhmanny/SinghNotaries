#Author: Blanche Chung
#Created Date: Spring 2023
#Description: This file is the views file for the website package. It contains the routes for the webpages.

from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
#from flask_login import login_required, current_user
from website import db #, login_manager
from .models import User, Document #, Notary, ImageTable
from werkzeug.utils import secure_filename
import os
from PIL import Image



views = Blueprint('views', __name__)

#@login_manager.user_loader
#def load_user(user_id):
#    return User.query.get(int(user_id))

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        address = request.form['address']
        address2 = request.form['address2']
        city = request.form['city']
        st = request.form['st']
        zipcode = request.form['zipcode']
        phone = request.form['phone']
        doctype = request.form['doctype']

        file = request.files['file']

        # Create User object
        user = User(
            fname=fname,
            lname=lname,
            email=email,
            address=address,
            address2=address2,
            city=city,
            st=st,
            zipcode=zipcode,
            phone=phone,
            doctype=doctype
        )

        # Add the User object to the database
        db.session.add(user)
        db.session.commit()

        # Save the document data
        document_data = file.read()

        # Create Document object
        document = Document(
            user_id=user.id,
            filename=file.filename,
            data=document_data
        )

        # Add the Document object to the database
        db.session.add(document)
        db.session.commit()

        # Read the image
        #image = Image.open(file)

        # Convert the image
        #image_data = Binary(image)

        # Create ImageTable object
        #image_record = ImageTable(
        #    user_id=user.id,
        #    image_name=file.filename,
        #    image_data=image_data
        #)

        # Add the ImageTable object to the database
        #db.session.add(image_record)
        #db.session.commit()

        return redirect(url_for('views.home'))

    return render_template('index.html')