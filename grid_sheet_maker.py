import pathlib
from PIL import Image

PATH = pathlib.Path("path here")
SAVE_PATH = pathlib.Path("save path here")
STEP_X = 4
STEP_Y = 3

max_w = 0
max_h = 0
images = []
for f in PATH.glob("*.png"):
    image = Image.open(f)
    if max_w < image.width:
        max_w = image.width
    if max_h < image.height:
        max_h = image.height
    images.append(image)
while max_w % STEP_X != 0:
    max_w += 1
while max_h % STEP_Y != 0:
    max_h += 1
    
sprite_sheet = Image.new("RGBA", (max_w * STEP_X, max_h * STEP_Y))
for x_i in range(0, STEP_X):
    for y_i in range(0, STEP_Y):
        img = images[-1]
        sprite_sheet.paste(img, (
            int((x_i * max_w + (x_i + 1) * max_w - img.width) / 2),
            int((y_i * max_h + (y_i + 1) * max_h - img.height) / 2)
        ), mask=img)
        images.pop()
sprite_sheet.save(SAVE_PATH)