from PIL import ImageTk, Image
import numpy as np

def display_image(self):

    if self.current_image is None:
        return

    img = self.current_image.copy()

    canvas_w = self.canvas.winfo_width()
    canvas_h = self.canvas.winfo_height()

    if canvas_w <= 1 or canvas_h <= 1:
        self.after(100, self.display_image)
        return

    img_w, img_h = img.size

    # Auto Fit
    scale = min(canvas_w / img_w, canvas_h / img_h)

    # Zoom
    scale *= self.zoom_factor

    new_w = max(1, int(img_w * scale))
    new_h = max(1, int(img_h * scale))

    img = img.resize(
        (new_w, new_h),
        Image.Resampling.LANCZOS
    )

    self.photo = ImageTk.PhotoImage(img)

    self.canvas.delete("all")

    self.canvas.create_image(
        canvas_w//2,
        canvas_h//2,
        image=self.photo,
        anchor="center"
)

    self.canvas.image = self.photo

    update_histogram(self)
# ==========================================
# HISTOGRAM
# ==========================================

def update_histogram(self):

    if self.current_image is None:
        return

    self.histogram.delete("all")

    gray = self.current_image.convert("L")

    data = np.array(gray)

    hist,_ = np.histogram(
        data.flatten(),
        256,
        [0,256]
    )

    max_value = hist.max()

    width = 220
    height = 180

    for i,value in enumerate(hist):

        x = i*(width/256)

        y = height-(value/max_value)*height

        self.histogram.create_line(
            x,
            height,
            x,
            y,
            fill="#3B82F6"
        )

    self.info_label.configure(
        text=f"Size : {self.current_image.width} x {self.current_image.height}\nMode : {self.current_image.mode}"
    )