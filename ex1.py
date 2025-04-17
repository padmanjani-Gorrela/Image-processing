from PIL import Image
import matplotlib.pyplot as plt

def load_and_resize(image_path, target_height):
    image = Image.open(image_path)
    aspect_ratio = image.width / image.height
    new_width = int(target_height * aspect_ratio)
    return image.resize((new_width, target_height))

def show_image(image, title="Image"):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

def main():
    # Paths to the images
    image_path1 = "Desktop/build/bean.webp"
    image_path2 = "Desktop/build/professor.jpg"

    try:
        # Load the two images
        image1 = Image.open(image_path1)
        image2 = Image.open(image_path2)
        print("Images loaded successfully.")
        show_image(image1, "Image 1")
        show_image(image2, "Image 2")

        # Resize both images to the same height
        target_height = min(image1.height, image2.height)
        image1_resized = load_and_resize(image_path1, target_height)
        image2_resized = load_and_resize(image_path2, target_height)
        print("Images resized successfully.")
        show_image(image1_resized, "Image 1 Resized")
        show_image(image2_resized, "Image 2 Resized")

        # Create a new image by arranging them side-by-side
        total_width = image1_resized.width + image2_resized.width
        side_by_side_image = Image.new('RGB', (total_width, target_height))
        side_by_side_image.paste(image1_resized, (0, 0))
        side_by_side_image.paste(image2_resized, (image1_resized.width, 0))
        print("Side-by-side image created successfully.")
        show_image(side_by_side_image, "Side-by-Side Image")

        # Convert the side-by-side image to grayscale
        gray_image = side_by_side_image.convert('L')
        print("Grayscale image created successfully.")
        show_image(gray_image, "Grayscale Image")

        # Convert grayscale image back to RGB to match color format
        gray_image_rgb = gray_image.convert('RGB')
        print("Grayscale image converted to RGB successfully.")
        show_image(gray_image_rgb, "Grayscale Image in RGB")

        # Create the final image by stacking the colored and gray images
        final_height = target_height * 2
        final_image = Image.new('RGB', (total_width, final_height))
        final_image.paste(side_by_side_image, (0, 0))
        final_image.paste(gray_image_rgb, (0, target_height))
        print("Final image created successfully.")
        show_image(final_image, "Final Image")

        # Save the final image
       # final_image.save("A1_solution.jpg")
        #print("A1_solution.jpg saved successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
