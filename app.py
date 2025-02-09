from flask import Flask, request, send_file, jsonify
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(_name_)  # Corrected variable name

# Ensure an output directory exists
os.makedirs("output", exist_ok=True)

@app.route('/create-logo', methods=['POST'])
def create_logo():
    try:
        # Get user input from the POST request
        data = request.json
        text = data.get('text', 'Default Logo')
        font_size = int(data.get('font_size', 50))
        bg_color = data.get('bg_color', '#FFFFFF')  # Default white
        text_color = data.get('text_color', '#000000')  # Default black

        # Create an image with the specified background color
        img_width, img_height = 500, 200
        image = Image.new('RGB', (img_width, img_height), bg_color)
        draw = ImageDraw.Draw(image)

        # Load a font
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Update this path if necessary
        font = ImageFont.truetype(font_path, font_size)

        # Calculate text position to center it
        text_width, text_height = font.getsize(text)
        text_x = (img_width - text_width) // 2
        text_y = (img_height - text_height) // 2

        # Draw the text on the image
        draw.text((text_x, text_y), text, fill=text_color, font=font)

        # Save the image
        file_path = f"output/logo.png"
        image.save(file_path)

        # Send the generated logo back to the user
        return send_file(file_path, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if _name_ == '_main_':  # Corrected variable name
    app.run(debug=True)