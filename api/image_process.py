import requests
from PIL import Image, ImageTk
from io import BytesIO

def process_image(image_url):
    pokemon_picture = get_picture_from_url(image_url)
    cropped_pokemon_picture = ImageTk.PhotoImage(crop_image(pokemon_picture))

    return cropped_pokemon_picture

def get_picture_from_url(url):
    picture_response = requests.get(url)
    img_data = picture_response.content

    img = Image.open(BytesIO(img_data))

    return img

def crop_image(image, size=(150, 150)):
    gray = image.convert('L')
    bbox = gray.getbbox()

    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    max_dimension = max(width, height)

    x_center = (bbox[0] + bbox[2])//2 
    y_center = (bbox[1] + bbox[3])//2
    half_size = max_dimension//2 + 5

    crop_box = (
        int(x_center - half_size),
        int(y_center - half_size),
        int(x_center + half_size),
        int(y_center + half_size)
    )

    cropped_image = image.crop(crop_box)

    cropped_image = cropped_image.resize(size)
    
    return cropped_image