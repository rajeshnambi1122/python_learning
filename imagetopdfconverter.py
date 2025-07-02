from fpdf import FPDF
import os
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.image('SRMIST.png', 10, 8, 25)
        self.set_xy(40, 20)
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, "Sofware Engineering Week 9 Internal Practical Assignment", 0, 1, 'C')
        self.ln(5)
        self.set_line_width(0.5)
        current_y = self.get_y()
        self.line(10, current_y, 200, current_y)
        self.ln(5)

    def footer(self):
        self.set_y(-50)
        self.set_font('Arial', 'B', 12)
        if self.page_no() == self.pages or self.pages == 1:
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(5)
            self.cell(0, 8, "Rajesh Nambi", 0, 1, 'C')
            self.cell(0, 8, "EC2532251010337", 0, 1, 'C')
            self.cell(0, 8, "MCA", 0, 1, 'C')
            self.cell(0, 8, "rn6525@srmist.edu.in", 0, 1, 'C')
        else:
            self.cell(0, 10, f"Page {self.page_no()}", 0, 0, 'C')

def convert_images_to_pdf(image_folder, output_pdf):
    pdf = PDF()
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    if not image_files:
        print("No image files found in the specified folder!")
        return
    image_files.sort()
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = Image.open(image_path)
        img_width, img_height = img.size
        a4_width = 190  # A4 width in mm
        a4_height = 277  # A4 height in mm (full page)
        header_space = 40  # Space below header in mm
        reserved_footer = 50  # Reserve 50mm at the bottom for the footer
        max_img_height = a4_height - header_space - reserved_footer
        width_ratio = a4_width / img_width
        height_ratio = max_img_height / img_height
        scale_factor = min(width_ratio, height_ratio)
        new_width = img_width * scale_factor
        new_height = img_height * scale_factor
        pdf.add_page()
        x = (210 - new_width) / 2  # Center horizontally
        y = header_space  # Start just below the header
        pdf.image(image_path, x, y, new_width, new_height)
    pdf.output(output_pdf)
    print(f"PDF generated successfully: {output_pdf}")

if __name__ == "__main__":
    # Specify the folder containing images and output PDF name
    image_folder = "images"  # Create this folder and put your images in it
    output_pdf = "Week9-SE-IPA.pdf"
    
    # Create images folder if it doesn't exist
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
        print(f"Created folder: {image_folder}")
        print(f"Please add your images to the '{image_folder}' folder and run the program again.")
    else:
        convert_images_to_pdf(image_folder, output_pdf)
