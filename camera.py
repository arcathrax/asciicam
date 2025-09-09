import cv2

class Camera:
    ASCII_CHARS = "@%#*+=-:. "  # Characters from dark to light

    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        if not self.camera.isOpened():
            raise Exception("Cannot open camera")

    def get_image(self):
        ret, frame = self.camera.read()
        if not ret:
            raise Exception("Can't receive frame.")
        return frame

    def resize_image(self, image, new_width=100):
        height, width = image.shape
        ratio = height / width
        new_height = int(new_width * ratio * 0.55)  # Adjust height ratio for ASCII
        resized_image = cv2.resize(image, (new_width, new_height))
        return resized_image

    def grayify(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def pixels_to_ascii(self, image):
        ascii_str = ""
        for pixel_row in image:
            for pixel in pixel_row:
                pixel_val = int(pixel)
                ascii_str += self.ASCII_CHARS[pixel_val * len(self.ASCII_CHARS) // 256]
            ascii_str += "\n"
        return ascii_str

    def get_ascii_camera(self, width=100):
        image = self.get_image()
        gray_image = self.grayify(image)
        resized_image = self.resize_image(gray_image, new_width=width)
        ascii_art = self.pixels_to_ascii(resized_image)
        return ascii_art

# Example usage:
if __name__ == "__main__":
    cam = Camera()
    try:
        while True:
            ascii_frame = cam.get_ascii_camera(width=80)
            print(ascii_frame)
    finally:
        cam.camera.release()
        cv2.destroyAllWindows()
