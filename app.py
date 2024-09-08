from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from lib import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

# Set the path for image uploads
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

content_image_size = 384
style_image_size = 256

class UploadForm(FlaskForm):
    image = FileField('Image')
    submit = SubmitField('Upload')

# Define a route for the root URL and to handle image upload
@app.route('/', methods=['GET', 'POST'])
def project():
    output_path = None
    output_filename = None
    content_filename=None
    style_filename=None
    if request.method == 'POST':
        content_file = request.files['file1']
        style_file = request.files['file2']
        content_image_path = './static/images/' + content_file.filename  
        style_image_path =  './static/images/' + style_file.filename
        # Load the images from file paths.
        content_image = load_image(content_image_path, (content_image_size, content_image_size))
        style_image = load_image(style_image_path, (style_image_size, style_image_size))
        style_image = tf.nn.avg_pool(style_image, ksize=[3,3], strides=[1,1], padding='SAME')
        # Perform stylization.
        stylized_image = hub_module(content_image, style_image)[0]
        output_directory = './static/output/'

        # Define the filename for the saved stylized image.
        output_filename = 'stylized_image.jpg'  # You can choose any desired filename and extension.

        # Save the stylized image.
        output_path = output_directory + output_filename
        tf.keras.preprocessing.image.save_img(output_path, stylized_image[0])
        content_filename=content_file.filename  
        style_filename=style_file.filename
    return render_template('index.html', content=content_filename,style=style_filename,image=output_filename)

if __name__ == '__main__':
    # Run the app on http://127.0.0.1:5000/
    app.run(port=3000)
