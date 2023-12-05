from PIL import Image
import os


def pixel_img(image_path, pixel_size):
    image = Image.open(image_path)

    w, h = image.size

    new_w = w // pixel_size
    new_h = h // pixel_size

    small_image = image.resize((new_w, new_h), resample=Image.NEAREST)

    pixeled_image = small_image.resize((new_w, new_h), resample=Image.NEAREST)

    return pixeled_image


def image_path_name(image_name, pixel_size):
    current = os.path.dirname(os.path.abspath(__file__))

    image_path = os.path.join(current, image_name)

    if os.path.exists(image_path):
        pixel = pixel_img(image_path, pixel_size)
        output_path = os.path.join(current, f"pixelated_{image_name}")
        pixel.save(output_path)
        print("以處理完\n")

    else:
        print("找不到圖像,請再重新run一次\n")


if __name__ == "__main__":
    input_image_name = input("請輸入檔案名稱: ")
    pixel_size = 10

    # 進行像素化處理
    image_path_name(input_image_name, pixel_size)
