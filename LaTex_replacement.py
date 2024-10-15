def generate_latex(data):
    education_section = ""
    skills_section = ""
    experience_section = ""
    projects_section = ""

    for institution, program, duration, mark in zip(data['educations']['institutions'], data['educations']['programs'],
                                                    data['educations']['durations'], data['educations']['marks']):
        if institution and program and duration:
            education_section += f"""
    \\resumeSubheading
      {{{institution}}}{{{mark}}}
      {{{program}}}{{{duration}}}
    \\vspace{{-4pt}}
    """

    if 'skills' in data:
        skills = data['skills']
        skills_section = f"""
     \\textbf{{\\normalsize{{Programming Languages:}}}} {{ \\normalsize{{{', '.join(skills['technical_skills'])}}}}} \\\\
     \\vspace{{1.2pt}}
     \\textbf{{\\normalsize{{Tools/Frameworks:}}}} {{ \\normalsize{{{', '.join(skills['tools/frameworks'])}}}}} \\\\
     \\vspace{{1.2pt}}
     \\textbf{{\\normalsize{{Soft Skills:}}}} {{ \\normalsize{{{', '.join(skills['soft_skills'])}}}}} \\\\
     \\vspace{{1.2pt}}
     \\textbf{{\\normalsize{{Analytical Skills:}}}} {{ \\normalsize{{{', '.join(skills['analytical_skills'])}}}}} \\\\
     \\vspace{{1.2pt}}
     \\textbf{{\\normalsize{{Spoken Languages:}}}} {{ \\normalsize{{{', '.join(skills['spoken_languages'])}}}}}
        """

    for company, position, duration, location, descs, techs in zip(
            data['experiences']['company_names'],
            data['experiences']['positions'],
            data['experiences']['durations'],
            data['experiences']['locations'],
            data['experiences']['descriptions'],
            data['experiences']['technologies']
    ):
        experience_section += f"""
    \\resumeSubheading
      {{{company}}}{{{position}}} 
      {{{location}}}{{{duration}}}
    \\resumeItemListStart
    """
        for desc in descs:
            if desc:
                experience_section += f"\\resumeItem{{\\normalsize{{{desc}}}}}\n"
        experience_section += "\\resumeItemListEnd\n"

    for name, descs, date, techs in zip(
            data['projects']['names'],
            data['projects']['descriptions'],
            data['projects']['dates'],
            data['projects']['technologies']
    ):
        projects_section += f"""
    \\resumeItem{{\\normalsize{{\\textbf{{{name}}}: {', '.join(descs)} }}\\href{{}}{{\\color{{teal}}\\underline{{GitHub}}}}}} \\\\
        """

    resume_template = f"""
    \\documentclass[letterpaper,11pt]{{article}}

    \\usepackage{{latexsym}}
    \\usepackage[empty]{{fullpage}}
    \\usepackage{{titlesec}}
    \\usepackage{{marvosym}}
    \\usepackage[usenames,dvipsnames]{{color}}
    \\usepackage{{verbatim}}
    \\usepackage{{enumitem}}
    \\usepackage[hidelinks]{{hyperref}}
    \\usepackage[english]{{babel}}
    \\usepackage{{tabularx}}
    \\usepackage{{fontawesome5}}
    \\usepackage{{multicol}}
    \\usepackage{{graphicx}}
    \\setlength{{\\multicolsep}}{{-3.0pt}}
    \\setlength{{\\columnsep}}{{-1pt}}
    \\input{{glyphtounicode}}

    \\RequirePackage{{tikz}}
    \\RequirePackage{{xcolor}}

    \\definecolor{{cvblue}}{{HTML}}{{0E5484}}
    \\definecolor{{black}}{{HTML}}{{130810}}
    \\definecolor{{darkcolor}}{{HTML}}{{0F4539}}
    \\definecolor{{cvgreen}}{{HTML}}{{3BD80D}}
    \\definecolor{{taggreen}}{{HTML}}{{00E278}}
    \\definecolor{{SlateGrey}}{{HTML}}{{2E2E2E}}
    \\definecolor{{LightGrey}}{{HTML}}{{666666}}
    \\colorlet{{name}}{{black}}
    \\colorlet{{tagline}}{{darkcolor}}
    \\colorlet{{heading}}{{darkcolor}}
    \\colorlet{{headingrule}}{{cvblue}}
    \\colorlet{{accent}}{{darkcolor}}
    \\colorlet{{emphasis}}{{SlateGrey}}
    \\colorlet{{body}}{{LightGrey}}

    % serif
    \\usepackage{{CormorantGaramond}}
    \\usepackage{{charter}}

    % Adjust margins
    \\addtolength{{\\oddsidemargin}}{{-0.6in}}
    \\addtolength{{\\evensidemargin}}{{-0.5in}}
    \\addtolength{{\\textwidth}}{{1.19in}}
    \\addtolength{{\\topmargin}}{{-.7in}}
    \\addtolength{{\\textheight}}{{1.4in}}
    \\urlstyle{{same}}

    \\definecolor{{airforceblue}}{{rgb}}{{0.36, 0.54, 0.66}}

    \\raggedbottom
    \\raggedright
    \\setlength{{\\tabcolsep}}{{0in}}

    % Sections formatting
    \\titleformat{{\\section}}{{
      \\vspace{{-4pt}}\\scshape\\raggedright\\large\\bfseries
    }}{{}}{{0em}}{{}}[\\color{{black}}\\titlerule \\vspace{{-5pt}}]

    % Ensure that generated PDF is machine readable/ATS parsable
    \\pdfgentounicode=1

    %-------------------------
    % Custom commands
    \\newcommand{{\\resumeItem}}[1]{{
      \\item\\small{{
        {{#1 \\vspace{{-1pt}}}}
      }}
    }}

    \\newcommand{{\\resumeSubheading}}[4]{{
      \\vspace{{-2pt}}\\item
        \\begin{{tabular*}}{{1.0\\textwidth}}[t]{{l@{{\\extracolsep{{\\fill}}}}r}}
          \\textbf{{#1}} & \\textbf{{#2}} \\\\
          \\textit{{#3}} & \\textit{{#4}} \\\\
        \\end{{tabular*}}\\vspace{{-7pt}}
    }}

    \\newcommand{{\\resumeSubHeadingListStart}}{{\\begin{{itemize}}[leftmargin=0.0in, label={{}}]}}
    \\newcommand{{\\resumeSubHeadingListEnd}}{{\\end{{itemize}}}}
    \\newcommand{{\\resumeItemListStart}}{{\\begin{{itemize}}[leftmargin=0.1in]}}
    \\newcommand{{\\resumeItemListEnd}}{{\\end{{itemize}}\\vspace{{-5pt}}}}

    %-------------------------------------------\\usepackage{{fontspec}}

    %%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%

    \\begin{{document}}

    % Heading
    \\begin{{center}}
        {{\\huge {data['name']}}} \\\\ \\ \\vspace{{2pt}}
        {{+91 {data['phone']}}} ~
        \\small{{-}}
        \\href{{mailto:{data['email']}}}{{\\color{{teal}}{{{data['email']}}}}} ~
        \\small{{-}}
        \\href{{{data['linkedin']}}}{{\\color{{teal}}{{Linkedin}}}} ~
        \\small{{-}}
        \\href{{{data['github']}}}{{\\color{{teal}}{{Github}}}} ~
        \\vspace{{-7pt}}
    \\end{{center}}

    % Education Section
    \\section{{\\color{{airforceblue}}EDUCATION}}
    \\resumeSubHeadingListStart
    {education_section}
    \\resumeSubHeadingListEnd
    \\vspace{{-10pt}}

    % Skills Section
    \\section{{\\color{{airforceblue}}TECHNICAL SKILLS}}
    \\begin{{itemize}}[leftmargin=0in, label={{}}]
      \\small{{\\item{{
        {skills_section}
        }}}}
    \\end{{itemize}}
    \\vspace{{-14pt}}

    % Experience Section
    \\section{{\\color{{airforceblue}}WORK EXPERIENCE}}
    \\resumeSubHeadingListStart
    {experience_section}
    \\resumeSubHeadingListEnd
    \\vspace{{-12pt}}

    % Projects Section
    \\section{{\\color{{airforceblue}}PROJECTS}}
    \\resumeItemListStart
    {projects_section}
    \\resumeItemListEnd

    \\end{{document}}
    \\vspace{{-3pt}}
    """

    return resume_template
