from abstract_analysis import AbstractAnalysis
from data_loader import DataLoader
from analyzer import DataAnalyzer
from pdf_generator import PDFReport

class Analysis(AbstractAnalysis):
    def run_analysis(self, level: str):
        try:
            # Load data
            data = DataLoader().load_data()

            # Analyze data
            analyzer = DataAnalyzer(data, level.upper())
            analysis_results = analyzer.perform_analysis()

            # Generate PDF
            pdf = PDFReport(level.upper(), analysis_results)
            pdf.generate_pdf()

            print(f"{level.upper()} analysis PDF successfully created.")
        except Exception as e:
            print(f"Something went wrong during analysis: {e}")


if __name__ == "__main__":
    level = input("Enter Analysis Level (Level-1 / Level-2 / Level-3): ").strip().upper()

    if level not in ["LEVEL-1", "LEVEL-2", "LEVEL-3"]:
        print("Invalid level. Please enter Level-1, Level-2, or Level-3.")
    else:
        Analysis().run_analysis(level)

