html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ name }} </title>
    <style>
        /* Font and Basic Styling */
        body {
            font-family: 'Cormorant Garamond', serif;
            color: #666666; /* LightGrey */
            margin: 40px;
        }

        h1, h2 {
            color: #0E5484; /* cvblue */
            margin-bottom: 10px;
        }

        h1 {
            font-size: 28px;
            color: black; /* Name */
        }

        p {
            margin: 0;
            padding: 0;
            font-size: 16px;
        }

        .section-title {
            font-size: 20px;
            font-weight: bold;
            border-bottom: 1px solid #0E5484;
            margin-top: 40px;
            margin-bottom: 10px;
            padding-bottom: 5px;
        }

        .contact-info {
            font-size: 14px;
            color: #0F4539; /* tagline */
        }

        .contact-info a {
            color: teal;
            text-decoration: none;
        }

        .resume-section {
            margin-bottom: 20px;
        }

        .experience-title {
            font-weight: bold;
        }

        .subheading {
            font-style: italic;
            color: #0F4539; /* tagline */
        }

        .bullet-list {
            list-style-type: none;
            padding: 0;
        }

        .bullet-list li {
            position: relative;
            margin-bottom: 10px;
            font-size: 15px;
        }

        .bullet-list li:before {
            content: "\2022"; /* Bullet symbol */
            color: #0F4539;
            font-size: 20px;
            position: absolute;
            left: -20px;
            top: 0;
        }

        .project-title {
            font-weight: bold;
        }

        .link {
            color: teal;
            text-decoration: underline;
        }

    </style>
</head>
<body>

    <!-- Header Section -->
    <div class="header">
        <h1>{{ name }}</h1>
        <p class="contact-info">
            {{ phone }} - <a href="mailto:{{ email }}">email</a> 
            {% if linkedin %} - <a href="{{ linkedin }}">LinkedIn</a>{% endif %}
            {% if github %} - <a href="{{ github }}">GitHub</a>{% endif %}
        </p>
    </div>

    <!-- Education Section -->
    <div class="resume-section">
        <h2 class="section-title">Education</h2>
        <ul>
        {% for institution, program, duration, marks in zip(educations['institutions'], educations['programs'], educations['durations'], educations['marks']) %}
            {% if institution %}
                <li>
                    <strong>{{ institution }}</strong> - {{ program }} ({{ duration }}) <br> {{ marks }}
                </li>
            {% endif %}
        {% endfor %}
    </ul>
    </div>

    <!-- Technical Skills Section -->
    <div class="resume-section">
        <h2 class="section-title">Technical Skills</h2>
        <ul class="bullet-list">
            <li><strong>Programming Languages:</strong> {{ skills['technical_skills'] | join(', ') }}</li>
            <li><strong>Tools/Frameworks:</strong> {{ skills['tools/frameworks'] | join(', ') }}</li>
            <li><strong>Soft Skills:</strong> {{ skills['soft_skills'] | join(', ') }}</li>
            <li><strong>Analytical Skills:</strong> {{ skills['analytical_skills'] | join(', ') }}</li>
        </ul>
    </div>

    <!-- Work Experience Section -->
    <div class="resume-section">
        <h2 class="section-title">Work Experience</h2>
        <ul>
            {% for company, position, description, duration, technologies in zip(experiences['company_names'], experiences['positions'], experiences['descriptions'], experiences['durations'], experiences['technologies']) %}
                <li>
                    <strong>{{ position }} at {{ company }}</strong> ({{ duration }})<br>
                    {% for desc in description %}
                        {{ desc }}<br>
                    {% endfor %}
                    <em>Technologies used: {{ technologies | join(', ') }}</em>
                </li>
            {% endfor %}
        </ul>
    </div>

    <!-- Projects Section -->
    <div class="resume-section">
        <h2 class="section-title">Projects</h2>
        <ul>
            {% for name, description, technologies in zip(projects['names'], projects['descriptions'], projects['technologies']) %}
                <li>
                    <strong>{{ name }}</strong><br>
                    {% for desc in description %}
                        {{ desc }}<br>
                    {% endfor %}
                    <em>Technologies used: {{ technologies | join(', ') }}</em>
                </li>
            {% endfor %}
        </ul>
    </div>

    <!-- Certifications and Extracurricular Activities Section -->
    <div class="resume-section">
        <h2 class="section-title">Certifications and Extracurricular Activities</h2>
        <ul class="bullet-list">
            <li>Won AI Hackathon 2024 powered by Infoedge Ventures.</li>
            <li>Artificial Primer Certification by Infosys – July 2023.</li>
            <li>Won 7 gold medals in basketball and achieved 1st prize in extempore, poetry, and quiz contests five times.</li>
        </ul>
    </div>

</body>
</html>
"""
