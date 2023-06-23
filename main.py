# Imports
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

image_path = ""


def select_image():
    """Changes the image path variable with the path selected by the user"""
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])


def add_watermark():
    """Create a new image with the watermark added"""
    global image_path
    # Open the image file
    if image_path:
        image = Image.open(image_path)
    else:
        messagebox.showwarning(title="No Image", message="Please Select an image by clicking on the Select File "
                                                         "button above.")
        return

    # Create a transparent layer for the watermark
    watermark = Image.new('RGBA', image.size, (255, 255, 255, 0))

    # Set the watermark text
    if watermark_entry.get():
        watermark_text = watermark_entry.get()
    else:
        messagebox.showwarning(title="No Watermark", message="You didn't enter any watermark!")
        return

    # Define the font and size for the watermark text
    font = ImageFont.truetype("./fonts/Poppins-Medium.ttf", 36)  # Replace with your desired font and size

    # Calculate the position to place the watermark (e.g., bottom right corner)
    watermark_position = (image.width - font.getsize(watermark_text)[0], image.height - font.getsize(watermark_text)[1])

    # Draw the watermark text on the transparent layer
    draw = ImageDraw.Draw(watermark)
    draw.text(watermark_position, watermark_text, fill=(255, 255, 255, 128), font=font)

    # Merge the original image with the watermark
    watermarked_image = Image.alpha_composite(image.convert('RGBA'), watermark)

    # Save the watermarked image to a file
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    watermarked_image.save(save_path)

    messagebox.showinfo(title="Success", message=f"New watermarked image was added in {save_path}")
    image_path = ""


def show_info():
    messagebox.showinfo(title="About The Program", message="_The 'watermark' input should contain the watermark that "
                                                           "you want to put on the image\n"
                                                           "_The 'Select file' button selects the image that you want "
                                                           "to put on it the watermark\n"
                                                           "_The 'Add watermark' button creates an image identical "
                                                           "to the one selected but with the watermark that you wrote."
                                                           "\n"
                                                           "Note: When you click on the 'add watermark' button you "
                                                           "will specify the directory and the name of the new image "
                                                           "that is created")


# Create the Tkinter window
window = tk.Tk()
window.title("Image Watermark Program")
window.config(padx=50, pady=50)


# Add a button to open the image
watermark_label = tk.Label(text="Watermark: ")
watermark_label.grid(row=0, column=0)

watermark_entry = tk.Entry(width=20)
watermark_entry.grid(row=0, column=1)

select_button = tk.Button(window, text="Select File", command=select_image, width=28)
select_button.grid(row=1, column=0, columnspan=2)

add_watermark_button = tk.Button(window, text="Add Watermark", command=add_watermark, width=28)
add_watermark_button.grid(row=2, column=0, columnspan=2)

info_button = tk.Button(window, text="Info", command=show_info, width=28)
info_button.grid(row=3, column=0, columnspan=2)


# Run the Tkinter event loop
window.mainloop()
