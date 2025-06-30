from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os
import textwrap


class PDFReport:
    def __init__(self, level: str, results: dict):
        self.level = level
        self.results = results

        # Fix: Create output path inside Assignment
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.output_dir = os.path.join(base_dir, "output")
        os.makedirs(self.output_dir, exist_ok=True)

        self.filename = os.path.join(self.output_dir, f"{level}_analysis_report.pdf")

    def generate_pdf(self):
        c = canvas.Canvas(self.filename, pagesize=A4)
        width, height = A4
        y = height - 40

        # Title
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(width / 2, y, f"{self.level} ANALYSIS")
        y -= 50

        # Dataset Description
        c.setFont("Helvetica-Bold", 14)
        c.drawString(40, y, "Dataset Description:")
        y -= 20
        for line in self.wrap_text(self.results.get("description", ""), 90):
            c.setFont("Helvetica", 12)
            c.drawString(50, y, line)
            y -= 15

        # Facts
        y -= 10
        c.setFont("Helvetica-Bold", 14)
        c.drawString(40, y, "Facts:")
        y -= 20
        for fact in self.results.get("Facts", []):
            c.setFont("Helvetica", 12)
            c.drawString(50, y, f"- {fact}")
            y -= 15

        # Column Info
        y -= 10
        c.setFont("Helvetica-Bold", 14)
        c.drawString(40, y, "Columns and Types:")
        y -= 20
        for col, dtype in self.results.get("Column_info", {}).items():
            c.setFont("Helvetica", 12)
            c.drawString(50, y, f"{col}: {dtype}")
            y -= 15
            if y < 100:
                c.showPage()
                y = height - 50

        # Plot Insertion: from Plot_1 to Plot_6
        for i in range(1, 7):
            plot_key = f"Plot_{i}"
            img_path = self.results.get(plot_key)

            if img_path and os.path.exists(img_path):
                c.showPage()
                c.setFont("Helvetica-Bold", 14)
                c.drawString(40, height - 50, f"Analysis Plot {i}")
                try:
                    c.drawImage(img_path, 40, height / 2 - 100, width=5.5 * inch, preserveAspectRatio=True)
                except Exception as e:
                    c.setFont("Helvetica", 12)
                    c.drawString(40, height / 2, f" Error loading {img_path}: {e}")
            else:
                # Add placeholder for missing plots
                c.showPage()
                c.setFont("Helvetica-Bold", 14)
                c.drawString(40, height - 50, f"Plot {i} Missing")
                c.setFont("Helvetica", 12)
                c.drawString(40, height - 70, f"{plot_key} not found in results or image path doesn't exist.")

        c.save()
        print(f"PDF saved at: {self.filename}")

    def wrap_text(self, text, width):
        return textwrap.wrap(text, width)
