# ==========================================
# Zoom In
# ==========================================
def zoom_in(self):

        if self.current_image:

            self.zoom_factor *= 1.2

            self.display_image()

           
def zoom_out(self):

        if self.current_image:

            self.zoom_factor /= 1.2

            if self.zoom_factor < 0.2:
                self.zoom_factor = 0.2

            self.display_image()