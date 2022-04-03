import os
from PIL import Image
from flask import url_for, current_app

def add_pic(pic_upload, username):

    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    storage_filename = str(username)+'.'+ext_type

    filepath = os.path.join(current_app.root_path, 'static\category', storage_filename)

    # output_size = (200, 200)   # to make size of image as width : 200px and height : 200px

    pic = Image.open(pic_upload)
    # pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename


