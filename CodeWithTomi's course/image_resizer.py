from PIL import Image

def resize_image(w, h):
    img = Image.open("malta.jpg")

    print(f"current image size= {img.size}")

    resized = img.resize((w,h))
    resized.save("malta_resized.jpeg")

    print(f"new image size= {resized.size}")


w = int(input("enter w"))
h = int(input("enter h"))
resize_image(w,h)
