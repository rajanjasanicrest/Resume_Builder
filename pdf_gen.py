from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

data = {
    "full_name": "John Doe",
    "skill_list": ["Python", "JavaScript", "HTML/CSS"],
    "n_years": 5,
    "experiences": [
        ("Software Engineer", "ABC Inc.", "2018", "2022", "Developed web applications."),
        ("Senior Developer", "XYZ Corp.", "2015", "2018", "Led a team of developers.")
    ],
    "gen_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nSed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "education": [
        ("Bachelor's", "University of XYZ", "2015", "Major in Computer Science.\nMinor in Mathematics."),
        ("Master's", "University of ABC", "2017", "Specialization in Software Engineering.")
    ],
    "certification": [
        ("Python Certification", "Python Institute", "2019", "Certified Python Programmer.\nScore: 95%"),
        ("JavaScript Certification", "JS Certification Board", "2020", "Certified JavaScript Developer.")
    ]
}

def generate_pdf(data, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    
    
    # Write content to the PDF
    y = 750  # Starting y coordinate
    
    # Full name
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, y, data["full_name"])
    y -= 20
    
    
    # Add a horizontal line
    c.line(100, y, 500, y)
    y -= 25
    
    # Description
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, y, "Description:")
    c.setFont("Helvetica", 12)
    y -= 20
    count = 1
    lines = ''
    description_lines = data["gen_description"].split(" ")
    for char in description_lines:
        lines += char + ' '
        if count % 10 == 0:
            count = 1
            c.drawString(100, y, lines)
            lines = ''
            y -= 15
            y -= 5  # Add line break
        count+=1
    c.drawString(100, y, lines)
    
    # Add a horizontal line
    c.line(100, y, 500, y)
    y -= 25
    

    # Skill set
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, y, "Skill Set:")
    c.setFont("Helvetica", 12)
    y -= 25
    for skill in data["skill_list"]:
        c.drawString(100, y, "- " + skill)
        y -= 15
    
    # Add a horizontal line
    c.line(100, y, 500, y)
    y -= 25
    
    # Education
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, y, "Education:")
    c.setFont("Helvetica", 12)
    y -= 25
    for edu in data["education"]:
        degree, university, year, edu_description = edu
        c.drawString(100, y, "- {} from {} ({})".format(degree, university, year))
        y -= 15
        edu_description_lines = edu_description.split("\n")
        for line in edu_description_lines:
            c.drawString(100, y, line)
            y -= 15
            y -= 5  # Add line break
    
    # Add a horizontal line
    c.line(100, y, 500, y)
    y -= 25
    
    # Experiences
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, y, "Experiences:")
    c.setFont("Helvetica", 12)
    y -= 20
    for exp in data["experiences"]:
        job_title, company, start_year, end_year, job_description = exp
        c.drawString(100, y, "- {} at {} ({} - {})".format(job_title, company, start_year, end_year))
        y -= 15
        job_description_lines = job_description.split("\n")
        for line in job_description_lines:
            c.drawString(100, y, line)
            y -= 15
            y -= 5  # Add line break
    
    # Add a horizontal line
    c.line(100, y, 500, y)
    y -= 25
    
    # Certificates
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, y, "Certificates:")
    c.setFont("Helvetica", 12)
    y -= 20
    for cert in data["certification"]:
        title, issuer, year, cert_description = cert
        c.drawString(100, y, "- {} from {} ({})".format(title, issuer, year))
        y -= 15
        cert_description_lines = cert_description.split("\n")
        for line in cert_description_lines:
            c.drawString(100, y, line)
            y -= 15
            y -= 5  # Add line break
    
    # Save the PDF
    c.save()


# # Generate the PDF
# generate_pdf(data, "resume.pdf")
