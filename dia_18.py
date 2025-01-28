from PIL import Image, ImageDraw
import random
ancho, alto = 500, 500
imagen = Image.new("RGB", (ancho, alto), "white")
dibujo = ImageDraw.Draw(imagen)
for _ in range(150):
    forma = random.choice(["ellipse", "rectangle", "line"])
    x1, y1 = random.randint(0, ancho), random.randint(0, alto)
    x2, y2 = random.randint(0, ancho), random.randint(0, alto)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if forma == "ellipse":
        dibujo.ellipse([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)], fill=color, outline=color)
    elif forma == "rectangle":
        dibujo.rectangle([min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)], fill=color, outline=color)
    else:
        dibujo.line([x1, y1, x2, y2], fill=color, width=3)
imagen.save("arte_abstracto.png")
imagen.show()