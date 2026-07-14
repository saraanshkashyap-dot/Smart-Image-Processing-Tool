import customtkinter as ctk
import tkinter as tk
import filters

# ==========================================
# CENTER IMAGE AREA
# ==========================================
def create_canvas(self):

    # ==========================
    # Center Panel
    # ==========================

    self.center = ctk.CTkFrame(
        self,
        fg_color="#0F172A",
        corner_radius=15
    )

    self.center.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # ==========================
    # Title
    # ==========================

    ctk.CTkLabel(
        self.center,
        text="Image Preview",
        font=("Segoe UI", 18, "bold")
    ).pack(pady=(15, 5))

    # ==========================
    # Canvas Frame
    # ==========================

    self.canvas_frame = ctk.CTkFrame(
        self.center,
        fg_color="#111827",
        corner_radius=15
    )

    self.canvas_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(5, 20)
    )

    # ==========================
    # Tkinter Canvas
    # ==========================

    self.canvas = tk.Canvas(
        self.canvas_frame,
        bg="#111827",
        highlightthickness=0,
        cursor="cross"
    )

    self.canvas.pack(
        fill="both",
        expand=True
    )
    
   
    # ==========================
    # Placeholder
    # ==========================

    self.canvas.create_text(
        500,
        300,
        text="🖼\n\nDrag & Drop\nor\nClick Open",
        fill="#7F8EA3",
        font=("Segoe UI", 24, "bold"),
        justify="center",
        tags="placeholder"
    )


# ==========================================
# RIGHT PANEL
# ==========================================

def create_histogram(self):

    self.right_panel = ctk.CTkFrame(
        self,
        width=280,
        fg_color="#111827",
        corner_radius=15
    )

    self.right_panel.pack(
        side="right",
        fill="y",
        padx=(0,10),
        pady=10
    )

    self.right_panel.pack_propagate(False)

    ctk.CTkLabel(
        self.right_panel,
        text="🎨 Filters",
        font=("Segoe UI",18,"bold")
    ).pack(pady=(20,10))

    self.filter_box = ctk.CTkOptionMenu(
        self.right_panel,
        values=filters.get_filter_names(),
        width=220
    )

    self.filter_box.pack()

    ctk.CTkButton(
        self.right_panel,
        text="Apply Filter",
        command=self.apply_filter,
        width=220,
        height=40
    ).pack(pady=(10,20))

    card = ctk.CTkFrame(
        self.right_panel,
        width=240,
        height=320,
        fg_color="#1E293B",
        corner_radius=15
    )

    card.pack()

    card.pack_propagate(False)

    ctk.CTkLabel(
        card,
        text="📊 Histogram",
        font=("Segoe UI",18,"bold")
    ).pack(pady=10)

    self.histogram = tk.Canvas(
        card,
        width=220,
        height=200,
        bg="#0F172A",
        highlightthickness=0
    )

    self.histogram.pack()

    self.histogram.create_text(
        110,
        100,
        text="No Image",
        fill="white",
        font=("Segoe UI",13,"bold")
    )

    self.info_label = ctk.CTkLabel(
        card,
        text="Size : -- x --\nMode : --",
        font=("Segoe UI",12)
    )

    self.info_label.pack(pady=10)


# ==========================================
# STATUS BAR
# ==========================================

def create_statusbar(self):

    self.status = ctk.CTkLabel(
        self,
        text="Ready",
        anchor="w",
        height=30,
        fg_color="#1E293B"
    )

    self.status.pack(
        side="bottom",
        fill="x"
    )