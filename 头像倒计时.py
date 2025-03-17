from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def add_days_to_image(image_path, output_path):
    # Calculate days to 2026 New Year
    today = datetime.now()
    new_year = datetime(2026, 1, 1)
    days_remaining = (new_year - today).days

    # Text to display
    text = f"{days_remaining} days to 2026"

    # Load the image
    image = Image.open(image_path)

    # Ensure image is in RGB mode
    if image.mode != "RGB":
        image = image.convert("RGB")

    draw = ImageDraw.Draw(image)

    # Use specific font
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Chalkduster.ttf", 40)

    # Calculate text position
    text_bbox = font.getbbox(text)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    image_width, image_height = image.size
    x_position = (image_width - text_width) // 2
    y_position = max(10, (image_height - text_height) // 12)

    # Add text to image
    draw.text((x_position, y_position), text, font=font, fill="black")  # Changed to black

    # Save the modified image
    image.save(output_path)


# Example usage
add_days_to_image("/Users/chrisoops/Downloads/头像倒计时原版.jpg", "/Users/chrisoops/Downloads/头像倒计时修改.jpg")
