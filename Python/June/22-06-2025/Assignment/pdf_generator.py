from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from pathlib import Path
import textwrap

# Setup output path
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

class PDFReport:
    def __init__(self, level: str, results: dict):
        self.level = level
        self.results = results
        self.filename = OUTPUT_DIR / f"{level}_analysis_report.pdf"

    def generate_pdf(self):
        c = canvas.Canvas(str(self.filename), pagesize=A4)
        width, height = A4
        y = height - 40

        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(width / 2, y, f"{self.level} ANALYSIS")
        y -= 50

        c.setFont("Helvetica", 12)
        if "description" in self.results:
            c.drawString(40, y, "Dataset Description:")
            y -= 20
            for line in self.wrap_text(self.results["description"], 90):
                c.drawString(50, y, line)
                y -= 15

        if "Facts" in self.results:
            y -= 20
            c.drawString(40, y, "Facts:")
            for fact in self.results["Facts"]:
                y -= 15
                c.drawString(50, y, f"- {fact}")

        if "Column_info" in self.results:
            y -= 30
            c.drawString(40, y, "Columns and Types:")
            for col, dtype in self.results["Column_info"].items():
                y -= 15
                c.drawString(50, y, f"{col}: {dtype}")
                if y < 100:
                    c.showPage()
                    y = height - 40

        # Add plots for Level-2 and Level-3
        for i in range(1, 7):
            plot_key = f"Plot_{i}"
            if plot_key in self.results:
                c.showPage()
                c.setFont("Helvetica-Bold", 14)
                c.drawString(40, height - 50, f"Analysis Plot {i}")
                img_path = self.results[plot_key]
                c.drawImage(str(img_path), 40, height / 2 - 100, width=5.5 * inch, preserveAspectRatio=True)

        c.save()
        print(f" PDF saved at: {self.filename}")

    def wrap_text(self, text, width):
        return textwrap.wrap(text, width)

