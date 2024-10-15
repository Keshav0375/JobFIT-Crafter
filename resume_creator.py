from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas


def create_resume_pdf(data, output_filename):
    pdf = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter

    airforce_blue = colors.Color(0.36, 0.54, 0.66)

    x_start = 30
    top_margin = 30
    bottom_margin = 30
    y_start = height - top_margin
    line_height = 12
    name_font_size = 24
    section_font_size = 14
    text_font_size = 10
    max_text_width = width - x_start * 1.5

    def wrap_text(text, max_width, font_name, font_size):
        """Wrap text to fit within a specified width."""
        pdf.setFont(font_name, font_size)
        words = text.split(' ')
        lines = []
        current_line = []

        for word in words:
            current_line.append(word)
            if pdf.stringWidth(' '.join(current_line)) > max_width:
                lines.append(' '.join(current_line[:-1]))
                current_line = [word]

        if current_line:
            lines.append(' '.join(current_line))

        return lines

    def draw_wrapped_text(text, x, y, font_name="Helvetica", font_size=text_font_size):
        lines = wrap_text(text, max_text_width, font_name, font_size)
        for line in lines:
            pdf.drawString(x, y, line)
            y -= line_height
        return y

    pdf.setFont("Helvetica-Bold", name_font_size)
    pdf.drawCentredString(width / 2, y_start, data.get("name", "Your Name"))

    contact_info = f'Contact Number : {data.get("phone", "Phone")} | Email: {data.get("email", "Email")}'
    contact_y = y_start - 20
    if contact_info.strip():
        pdf.setFont("Helvetica", text_font_size)
        pdf.drawCentredString(width / 2, contact_y, contact_info)

    contact_y -= line_height
    linkedin = data.get('linkedin', '')
    github = data.get('github', '')
    if linkedin or github:
        social_info = " | ".join(filter(None, [f"LinkedIn: {linkedin}", f"GitHub: {github}"]))
        pdf.drawCentredString(width / 2, contact_y, social_info)

    pdf.setStrokeColor(airforce_blue)
    pdf.setLineWidth(1)
    y_start = contact_y - 2
    pdf.line(x_start, y_start, width - 60, y_start)
    y_start -= 20

    def draw_section_title(title):
        nonlocal y_start
        pdf.setFont("Helvetica-Bold", section_font_size)
        pdf.setFillColor(airforce_blue)
        pdf.drawString(x_start, y_start, title)
        y_start -= line_height + 5
        pdf.setFillColor(colors.black)

    def add_education():
        nonlocal y_start
        draw_section_title("EDUCATION")
        pdf.setFont("Helvetica", text_font_size)
        for i in range(len(data['educations']['institutions'])):
            if all([data['educations']['institutions'][i], data['educations']['programs'][i]]):
                pdf.setFont("Helvetica-Bold", text_font_size)
                pdf.drawString(x_start, y_start, data['educations']['institutions'][i])
                duration = data['educations']['durations'][i]
                if duration:
                    duration_width = pdf.stringWidth(duration, "Helvetica", text_font_size)
                    duration_x_start = width - 60 - duration_width
                    pdf.setFont("Helvetica", text_font_size)
                    pdf.drawString(duration_x_start, y_start, duration)

                y_start -= line_height

                program = data['educations']['programs'][i]
                if program:
                    pdf.setFont("Helvetica", text_font_size)
                    pdf.drawString(x_start, y_start, program)

                    marks = data['educations']['marks'][i]
                    if marks:
                        marks_width = pdf.stringWidth(f"Marks: {marks}", "Helvetica", text_font_size)
                        marks_x_start = width - 60 - marks_width
                        pdf.drawString(marks_x_start, y_start, f"Marks: {marks}")

                    y_start -= line_height + 5

    add_education()

    def add_skills():
        nonlocal y_start
        draw_section_title("TECHNICAL SKILLS")
        for skill_type, skills in data['skills'].items():
            if skills:
                pdf.setFont("Helvetica-Bold", text_font_size)
                pdf.drawString(x_start, y_start, skill_type.replace("_", " ").title())
                y_start -= line_height

                pdf.setFont("Helvetica", text_font_size)
                y_start = draw_wrapped_text(", ".join(skills), x_start, y_start)

                y_start -= line_height / 4

    add_skills()

    def add_projects():
        nonlocal y_start
        draw_section_title("PROJECTS")

        for i, project_name in enumerate(data['projects']['names']):
            if project_name and data['projects']['technologies'][i] and data['projects']['descriptions'][i]:

                pdf.setFont("Helvetica-Bold", text_font_size)
                pdf.drawString(x_start, y_start, project_name)
                y_start -= line_height

                pdf.setFont("Helvetica", text_font_size)
                y_start = draw_wrapped_text(", ".join(data['projects']['technologies'][i]), x_start, y_start)

                for desc in data['projects']['descriptions'][i]:
                    y_start = draw_wrapped_text(f"- {desc}", x_start, y_start)

                y_start -= line_height / 2

    add_projects()

    def add_experience():
        nonlocal y_start
        draw_section_title("WORK EXPERIENCE")

        for i, company in enumerate(data['experiences']['company_names']):
            if company and data['experiences']['positions'][i] and data['experiences']['durations'][i]:

                pdf.setFont("Helvetica-Bold", text_font_size)
                pdf.drawString(x_start, y_start, f"{data['experiences']['positions'][i]} at {company}")

                duration_text = data['experiences']['durations'][i]
                duration_width = pdf.stringWidth(duration_text, "Helvetica", text_font_size)

                duration_x_start = width - 60 - duration_width

                pdf.setFont("Helvetica", text_font_size)
                pdf.drawString(duration_x_start, y_start, duration_text)

                y_start -= line_height
                if y_start < bottom_margin:
                    pdf.showPage()
                    y_start = height - top_margin

                for exp in data['experiences']['descriptions'][i]:
                    y_start = draw_wrapped_text(f"- {exp}", x_start, y_start)
                    if y_start < bottom_margin:
                        pdf.showPage()
                        y_start = height - top_margin


                y_start -= line_height / 2



    add_experience()

    pdf.showPage()
    pdf.save()
