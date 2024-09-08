# Neural Style Transfer with Flask

![image](https://github.com/user-attachments/assets/4354c3ac-6360-48de-a740-e21fc9067eb3)

![image](https://github.com/user-attachments/assets/c3628826-016c-4dfe-b44c-ad01096c8b99)

This project demonstrates a neural style transfer application using TensorFlow and Flask. The application allows users to upload content and style images and produces a stylized image that combines the content of the content image with the style of the style image.

## Prerequisites

- Python 3.6 or higher
- TensorFlow
- TensorFlow Hub
- Flask
- Flask-WTF
- Matplotlib
- Numpy

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/koushik2k3/Neural-Style-Transfer.git
   cd Neural-Style-Transfer
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Packages**

   ```bash
   pip install tensorflow tensorflow-hub flask flask-wtf matplotlib numpy
   ```

## Usage

1. **Start the Flask Application**

   ```bash
   python app.py
   ```

   The Flask app will start on `http://127.0.0.1:3000/`.

2. **Upload Images**

   - Navigate to the root URL of the Flask app.
   - Use the form to upload a content image and a style image.
   - Submit the form to process the images.

3. **View the Result**

   - The processed stylized image will be displayed on the page.
   - The stylized image will also be saved to the `static/output` directory.

## Project Structure

- `app.py`: Main Flask application script.
- `templates/`: Contains the HTML templates.
- `static/`: Contains static files including uploaded images and output images.

