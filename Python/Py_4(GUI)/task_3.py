import tkinter as tk
from math import pi, cos, sin


class HumidityGauge(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Humidity Gauge")
        self.resizable(True, True)

        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()

        self.draw_gauge(36)  # Example with 36% humidity

    def draw_gauge(self, humidity):
        # Draw arcs for the gauge background
        self.canvas.create_arc(
            50, 150, 350, 450, start=0, extent=100, fill="green", width=2
        )

        self.canvas.create_arc(
            50, 150, 350, 450, start=100, extent=80, fill="yellow", width=2
        )

        self.canvas.create_arc(
            50, 150, 350, 450, start=140, extent=40, fill="red", width=2
        )

        # Center coordinates of the large arc
        center_x = (50 + 350) // 2
        center_y = (150 + 450) // 2

        # Dimensions of the smaller arc
        smaller_width = 200
        smaller_height = 200

        # Coordinates of the bounding box for the smaller arc
        smaller_left = center_x - smaller_width // 2
        smaller_top = center_y - smaller_height // 2
        smaller_right = center_x + smaller_width // 2
        smaller_bottom = center_y + smaller_height // 2

        self.canvas.create_arc(
            smaller_left,
            smaller_top,
            smaller_right,
            smaller_bottom,
            start=0,
            extent=180,
            fill="white",
            width=2,
        )

        # Draw the needle
        angle = pi * (180 * humidity / 100 - 90) / 180
        x = 200 + 120 * cos(angle)
        y = 300 + 120 * sin(angle)
        self.canvas.create_line(200, 300, x, y, width=4)

        # Draw the labels
        self.canvas.create_text(
            200, 100, text="Humidity", font=("Helvetica", 24, "italic")
        )
        self.canvas.create_text(50, 320, text="100", font=("Helvetica", 12))
        self.canvas.create_text(350, 320, text="0", font=("Helvetica", 12))
        self.canvas.create_text(200, 350, text=f"{humidity} %", font=("Helvetica", 16))


if __name__ == "__main__":
    app = HumidityGauge()
    app.mainloop()
