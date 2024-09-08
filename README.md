# Neural Style Transfer with Flask

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
   git clone <repository-url>
   cd <repository-directory>
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

## Code Overview

- **`crop_center(image)`**: Crops an image to a square shape from the center.
- **`load_image(image_path, image_size=(256, 256), preserve_aspect_ratio=True)`**: Loads and preprocesses images from a file path.
- **`hub_module`**: TensorFlow Hub module for arbitrary image stylization.
- **`project()`**: Flask route that handles image upload and style transfer.

## Project Structure

- `app.py`: Main Flask application script.
- `templates/`: Contains the HTML templates.
- `static/`: Contains static files including uploaded images and output images.

## Contributing

Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License.

---

Replace `<repository-url>` and `<repository-directory>` with the actual URL and directory name of your repository. Let me know if there are any specific details you'd like to include!
