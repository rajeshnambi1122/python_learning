from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.image('SRMIST.png', 10, 8, 25)
        self.set_xy(40, 20)
        self.set_font('helvetica', 'B', 14)
        self.cell(0, 10, "Week 9 Career Advancement LAQ", 0, 1, 'C')
        self.ln(5)
        self.set_line_width(0.5)
        current_y = self.get_y()
        self.line(10, current_y, 200, current_y)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, 'C')

    def add_table(self, headers, data, col_widths):
        self.set_font('helvetica', 'B', 9)
        line_height = 6
        # Draw table header
        self.set_fill_color(200, 200, 200)
        for i, header in enumerate(headers):
            self.cell(col_widths[i], line_height * 2, header, border=1, align='C', fill=True)
        self.ln(line_height * 2)

        self.set_font('helvetica', '', 9)

        for row in data:
            # Calculate the max height for the row
            max_lines = 1
            cell_lines = []
            for i, cell in enumerate(row):
                # Use split_only to count lines
                n_lines = len(self.multi_cell(col_widths[i], line_height, cell, border=0, align='L', split_only=True))
                cell_lines.append(n_lines)
                max_lines = max(max_lines, n_lines)
            row_height = max_lines * line_height

            x_start = self.get_x()
            y_start = self.get_y()

            for i, cell in enumerate(row):
                self.set_xy(x_start + sum(col_widths[:i]), y_start)
                # Save current font
                self.set_font('helvetica', '', 9)
                self.multi_cell(col_widths[i], line_height, cell, border=0, align='L')
                # Draw cell border
                self.set_xy(x_start + sum(col_widths[:i]), y_start)
                self.cell(col_widths[i], row_height, '', border=1)

            self.set_y(y_start + row_height)

    def add_unicode_text(self, text):
        self.set_font('helvetica', '', 12)
        in_code_block = False
        in_table = False
        table_lines = []
        unicode_replacements = {
            '\u2019': "'", '\u2014': '-', '\u2013': '-', '\u201c': '"', '\u201d': '"',
            '\u2018': "'", '\u2022': '*', '\u2012': '-', '\u2015': '-',
            '\u2192': '->',
            '\u2212': '-',  # Unicode minus sign
        }
        def calc_col_widths(table_rows, min_width=25, max_width=60):
            # Calculate max width for each column using get_string_width
            num_cols = len(table_rows[0])
            col_widths = [min_width] * num_cols
            for row in table_rows:
                for i, cell in enumerate(row):
                    cell_width = self.get_string_width(cell) + 8  # padding
                    col_widths[i] = min(max(col_widths[i], cell_width), max_width)
            return col_widths

        for line in text.split('\n'):
            if not line.strip():
                if in_table and table_lines:
                    headers = table_lines[0]
                    data = table_lines[1:]
                    col_widths = calc_col_widths(table_lines)
                    self.add_table(headers, data, col_widths)
                    self.ln(2)
                    table_lines = []
                    in_table = False
                else:
                    self.ln(2)
                continue
            for unicode_char, ascii_char in unicode_replacements.items():
                line = line.replace(unicode_char, ascii_char)
            if line.strip().startswith('+') or (line.strip().startswith('|') and line.count('-') > 5):
                self.set_font('Courier', '', 8)
                self.multi_cell(0, 4, line)
                continue
            if line.strip().startswith('|'):
                # Parse markdown table row
                row = [cell.strip() for cell in line.split('|')[1:-1]]
                if not in_table:
                    in_table = True
                    table_lines = []
                # Skip separator row (|---|---|)
                if all(set(cell) <= {'-', ':'} for cell in row):
                    continue
                table_lines.append(row)
                continue
            elif in_table and table_lines:
                headers = table_lines[0]
                data = table_lines[1:]
                col_widths = calc_col_widths(table_lines)
                self.add_table(headers, data, col_widths)
                self.ln(2)
                table_lines = []
                in_table = False
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                self.set_font('Courier', '', 10)
                self.set_fill_color(230, 230, 230)
                self.multi_cell(0, 6, line, 0, 1, fill=True)
                self.set_fill_color(255, 255, 255)
            else:
                self.set_font('helvetica', '', 12)
                if line.strip().startswith('*'):
                    self.ln(1)
                    self.multi_cell(0, 8, line)
                else:
                    self.multi_cell(0, 8, line)
        # If table at end of text
        if in_table and table_lines:
            headers = table_lines[0]
            data = table_lines[1:]
            col_widths = calc_col_widths(table_lines)
            self.add_table(headers, data, col_widths)
            self.ln(2)

content = """




There are two valid cases where you get:

1 King and 1 Spade
  But one of those cards might be King of Spades, which is both a King and a Spade.

So we break this into 2 cases:



Case 1:
King of Spades and any other non-King, non-Spade card
 Not valid for this problem, because we want exactly one King and one Spade, not both in one card

We only consider the following:



Case A:

King (but not Spade) + any Spade (not King)

* Kings in deck = 4
* One of them is King of Spades, so Kings (excluding Spade) = 3
* Spades in deck = 13
* One of them is King of Spades, so Spades (excluding King) = 12

So:

* Ways to choose 1 King (not Spade) = 3
* Ways to choose 1 Spade (not King) = 12
* Total favorable outcomes = 3 × 12 = 36



 Case B:

King of Spades + any other card (that is not King or Spade)

* King of Spades = 1 card
* Cards that are not King and not Spade =
   52 total − 4 Kings  − 13 Spades + 1 (King of Spades was subtracted twice)
   = 52 − 4 − 13 + 1 = 36

So:

* Ways to choose King of Spades = 1
* Ways to choose other card = 36
* Total favorable outcomes = 1 × 36 = 36

---

Total favorable = Case A + Case B = 36 + 36 = 72

---

Total possible ways to draw 2 cards from 52:

C(52, 2) = 1326

---
Final Answer:

Probability = 72 / 1326 = 2 / 37

---

Plain Text Answer:
Total favorable outcomes = 72
Total possible outcomes = 1326
Probability = 72 / 1326 = 2 / 37

Final Answer: 2/37

"""

pdf = PDF()
pdf.add_page()
# clean the content of unsupported unicode characters
cleaned_content = content.encode('latin-1', 'replace').decode('latin-1')
pdf.add_unicode_text(cleaned_content)

pdf_file = "Week9-CA-LAQ.pdf"
pdf.output(pdf_file)
print(f"PDF generated and saved as {pdf_file}")
