#!/usr/bin/env python3
"""
Build HTML resume site from LaTeX source files.
This script parses the English LaTeX resume and generates index.html.
"""

import re
from pathlib import Path
from typing import List, Dict, Any


class LatexResumeParser:
    """Parser for LaTeX resume files."""

    def __init__(self, tex_dir: Path):
        self.tex_dir = tex_dir
        self.resume_data = {}

    def parse(self) -> Dict[str, Any]:
        """Parse all LaTeX files and extract content."""
        # Parse main file for header info
        main_file = self.tex_dir / "resume.tex"
        self.resume_data['header'] = self._parse_header(main_file)

        # Parse experience
        exp_file = self.tex_dir / "resume_sections" / "experience.tex"
        self.resume_data['experience'] = self._parse_experience(exp_file)

        # Parse skills
        skills_file = self.tex_dir / "resume_sections" / "skills.tex"
        self.resume_data['skills'] = self._parse_skills(skills_file)

        return self.resume_data

    def _parse_header(self, file_path: Path) -> Dict[str, str]:
        """Extract header information."""
        content = file_path.read_text(encoding='utf-8')

        # Extract name
        name_match = re.search(r'\\textbf\{\\Huge\s+(.+?)\}', content)
        name = name_match.group(1).strip() if name_match else "Nick Osipov"

        # Extract title
        title_match = re.search(r'\\textbf\{MLOps Engineer\}', content)
        title = "MLOps Engineer" if title_match else "MLOps Engineer"

        # Extract contact info
        location_match = re.search(r'Georgia, Batumi, (\d+)', content)
        phone_match = re.search(r'\+995\s+[\d\s]+', content)
        linkedin_match = re.search(r'in/(\w+)', content)
        telegram_match = re.search(r'@(\w+)', content)
        email_match = re.search(r'([\w\.\-]+@[\w\.\-]+)', content)

        return {
            'name': name,
            'title': title,
            'location': location_match.group(0) if location_match else "",
            'phone': phone_match.group(0) if phone_match else "",
            'linkedin': linkedin_match.group(1) if linkedin_match else "nickosipov",
            'telegram': telegram_match.group(1) if telegram_match else "NickOsipov",
            'email': email_match.group(1) if email_match else ""
        }

    def _parse_experience(self, file_path: Path) -> List[Dict[str, Any]]:
        """Extract work experience."""
        content = file_path.read_text(encoding='utf-8')
        experiences = []

        # Find all resumeSubheadingWork blocks
        pattern = r'\\resumeSubheadingWork\s*\{\\href\{(.+?)\}\{(.+?)\}\}\{(.+?)\}\s*\{(.+?)\}\{(.+?)\}\s*\{(.+?)\}\{(.+?)\}\s*\\resumeItemListStart(.*?)\\resumeItemListEnd'

        matches = re.finditer(pattern, content, re.DOTALL)

        for match in matches:
            url = match.group(1)
            company = match.group(2)
            location = match.group(3)
            position = match.group(4)
            dates = match.group(5)
            department = match.group(6)
            work_type = match.group(7)
            items_block = match.group(8)

            # Extract resume items
            items = re.findall(r'\\resumeItem\{(.+?)\}', items_block)

            experiences.append({
                'company': company,
                'url': url,
                'location': location,
                'position': position,
                'dates': dates,
                'department': department,
                'work_type': work_type,
                'achievements': items
            })

        return experiences

    def _parse_skills(self, file_path: Path) -> Dict[str, List[str]]:
        """Extract skills by category."""
        content = file_path.read_text(encoding='utf-8')
        skills = {}

        # Find all skill categories
        pattern = r'\\textbf\{(.+?)\}\{:\s*(.+?)\}'

        matches = re.finditer(pattern, content)

        for match in matches:
            category = match.group(1)
            skills_list = match.group(2).split(',')
            skills[category] = [s.strip() for s in skills_list]

        return skills


class HTMLGenerator:
    """Generate HTML from parsed resume data."""

    def __init__(self, resume_data: Dict[str, Any]):
        self.data = resume_data

    def generate(self) -> str:
        """Generate complete HTML document."""
        header = self.data.get('header', {})

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{header.get('name', 'Nick Osipov')} - {header.get('title', 'MLOps Engineer')} Resume">
    <meta name="author" content="{header.get('name', 'Nick Osipov')}">
    <title>{header.get('name', 'Nick Osipov')} | {header.get('title', 'MLOps Engineer')}</title>
    <style>
        {self._get_css()}
    </style>
</head>
<body>
    <div class="container">
        {self._generate_header()}
        {self._generate_content()}
        {self._generate_footer()}
    </div>
</body>
</html>'''
        return html

    def _get_css(self) -> str:
        """Return CSS styles."""
        return '''* {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            color: #333;
        }

        .container {
            max-width: 900px;
            width: 100%;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
            animation: fadeIn 0.6s ease-in;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 40px;
            text-align: center;
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            font-weight: 700;
        }

        .header h2 {
            font-size: 1.5rem;
            font-weight: 300;
            opacity: 0.9;
        }

        .content {
            padding: 50px 40px;
        }

        .section {
            margin-bottom: 40px;
        }

        .section h3 {
            font-size: 1.3rem;
            color: #667eea;
            margin-bottom: 20px;
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .download-buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 15px 40px;
            font-size: 1.1rem;
            font-weight: 600;
            text-decoration: none;
            border-radius: 50px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            min-width: 250px;
        }

        .btn-english {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .btn-russian {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        }

        .btn:active {
            transform: translateY(-1px);
        }

        .btn svg {
            margin-right: 10px;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }

        .social-link {
            display: inline-flex;
            align-items: center;
            padding: 12px 25px;
            text-decoration: none;
            color: #333;
            border: 2px solid #667eea;
            border-radius: 50px;
            transition: all 0.3s ease;
            font-weight: 500;
        }

        .social-link:hover {
            background: #667eea;
            color: white;
            transform: translateY(-2px);
        }

        .social-link svg {
            margin-right: 8px;
        }

        .gif-container {
            text-align: center;
            margin-bottom: 30px;
        }

        .gif-container img {
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .experience-item {
            margin-bottom: 30px;
            padding: 25px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }

        .experience-header {
            margin-bottom: 15px;
        }

        .company {
            font-size: 1.3rem;
            font-weight: 700;
            color: #667eea;
            text-decoration: none;
        }

        .company:hover {
            text-decoration: underline;
        }

        .position {
            font-size: 1.1rem;
            font-weight: 600;
            color: #333;
            margin-top: 5px;
        }

        .dates {
            color: #666;
            font-style: italic;
            margin-top: 5px;
        }

        .department {
            color: #666;
            margin-top: 5px;
        }

        .achievements {
            margin-top: 15px;
            list-style-position: inside;
        }

        .achievements li {
            margin-bottom: 8px;
            line-height: 1.6;
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .skill-category {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
        }

        .skill-category-name {
            font-weight: 700;
            color: #667eea;
            margin-bottom: 8px;
        }

        .skill-items {
            color: #666;
            line-height: 1.6;
        }

        .about-text {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            line-height: 1.8;
            text-align: left;
        }

        .footer {
            text-align: center;
            padding: 30px;
            background: #f8f9fa;
            color: #666;
            font-size: 0.9rem;
        }

        @media (max-width: 600px) {
            .header h1 {
                font-size: 2rem;
            }

            .header h2 {
                font-size: 1.2rem;
            }

            .content {
                padding: 30px 20px;
            }

            .btn {
                min-width: 100%;
            }

            .social-link {
                min-width: 100%;
                justify-content: center;
            }

            .skills-grid {
                grid-template-columns: 1fr;
            }
        }'''

    def _generate_header(self) -> str:
        """Generate header section."""
        header = self.data.get('header', {})
        return f'''<div class="header">
            <h1>{header.get('name', 'Nick Osipov')}</h1>
            <h2>{header.get('title', 'MLOps Engineer')}</h2>
        </div>'''

    def _generate_content(self) -> str:
        """Generate main content section."""
        return f'''<div class="content">
            <div class="section">
                <div class="gif-container">
                    <img src="https://raw.githubusercontent.com/NickOsipov/resume/main/assets/mlops.gif" alt="MLOps Animation">
                </div>
            </div>

            <div class="section">
                <h3>About Me</h3>
                <div class="about-text">
                    {self._generate_about()}
                </div>
            </div>

            <div class="section">
                <h3>Download Resume</h3>
                <div class="download-buttons">
                    <a href="pdf/Resume_NickOsipov_MLOps_EN.pdf" class="btn btn-english" download>
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                            <polyline points="7 10 12 15 17 10"></polyline>
                            <line x1="12" y1="15" x2="12" y2="3"></line>
                        </svg>
                        English Version
                    </a>
                    <a href="pdf/Resume_NickOsipov_MLOps_RU.pdf" class="btn btn-russian" download>
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                            <polyline points="7 10 12 15 17 10"></polyline>
                            <line x1="12" y1="15" x2="12" y2="3"></line>
                        </svg>
                        Русская Версия
                    </a>
                </div>
            </div>

            {self._generate_experience()}

            {self._generate_skills()}

            <div class="section">
                <h3>Connect with Me</h3>
                <div class="social-links">
                    <a href="https://github.com/NickOsipov" class="social-link" target="_blank" rel="noopener noreferrer">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                        </svg>
                        GitHub
                    </a>
                    <a href="https://www.linkedin.com/in/nickosipov/" class="social-link" target="_blank" rel="noopener noreferrer">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                        </svg>
                        LinkedIn
                    </a>
                    <a href="https://t.me/NickOsipov" class="social-link" target="_blank" rel="noopener noreferrer">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>
                        </svg>
                        Telegram
                    </a>
                </div>
            </div>
        </div>'''

    def _generate_about(self) -> str:
        """Generate about section from experience summary."""
        experiences = self.data.get('experience', [])

        if not experiences:
            return "Senior MLOps Engineer with expertise in designing, deploying, and maintaining machine learning systems in production."

        # Get current position
        current = experiences[0] if experiences else {}

        about = f'''<p>
            Senior MLOps Engineer currently working at <strong>{current.get('company', 'Kadam')}</strong>
            as {current.get('position', 'Senior MLOps Engineer')}.
        </p>
        <p style="margin-top: 15px;">
            Specialized in building production-grade ML systems, implementing CI/CD pipelines,
            orchestration with Airflow/Prefect, containerization with Docker/Kubernetes,
            and establishing MLOps best practices across organizations.
        </p>
        <p style="margin-top: 15px;">
            Experienced in leading teams, mentoring engineers, and designing scalable
            ML infrastructure for CTR prediction, anti-fraud systems, and various ML applications.
        </p>'''

        return about

    def _generate_experience(self) -> str:
        """Generate experience section."""
        experiences = self.data.get('experience', [])

        if not experiences:
            return ""

        html = '<div class="section"><h3>Experience</h3>'

        for exp in experiences:
            achievements_html = '\n'.join([f'<li>{item}</li>' for item in exp.get('achievements', [])])

            html += f'''
            <div class="experience-item">
                <div class="experience-header">
                    <a href="{exp.get('url', '#')}" class="company" target="_blank" rel="noopener noreferrer">
                        {exp.get('company', '')}
                    </a>
                    <div class="position">{exp.get('position', '')}</div>
                    <div class="dates">{exp.get('dates', '')}</div>
                    <div class="department">{exp.get('department', '')} • {exp.get('work_type', '')}</div>
                </div>
                <ul class="achievements">
                    {achievements_html}
                </ul>
            </div>'''

        html += '</div>'
        return html

    def _generate_skills(self) -> str:
        """Generate skills section."""
        skills = self.data.get('skills', {})

        if not skills:
            return ""

        html = '<div class="section"><h3>Skills</h3><div class="skills-grid">'

        for category, items in skills.items():
            items_str = ', '.join(items)
            html += f'''
            <div class="skill-category">
                <div class="skill-category-name">{category}</div>
                <div class="skill-items">{items_str}</div>
            </div>'''

        html += '</div></div>'
        return html

    def _generate_footer(self) -> str:
        """Generate footer section."""
        header = self.data.get('header', {})
        return f'''<div class="footer">
            <p>&copy; 2026 {header.get('name', 'Nick Osipov')}. Python Engineer | MLOps Specialist</p>
            <p>Machine Learning Operations & Data Engineering</p>
        </div>'''


def main():
    """Main function to build the site."""
    # Parse LaTeX resume (project root is parent of scripts/)
    project_root = Path(__file__).parent.parent
    tex_dir = project_root / "tex" / "en"
    parser = LatexResumeParser(tex_dir)
    resume_data = parser.parse()

    # Generate HTML
    generator = HTMLGenerator(resume_data)
    html_content = generator.generate()

    # Write to index.html in project root
    output_file = project_root / "index.html"
    output_file.write_text(html_content, encoding='utf-8')

    print(f"✓ Successfully built {output_file}")
    print(f"✓ Parsed {len(resume_data.get('experience', []))} work experiences")
    print(f"✓ Parsed {len(resume_data.get('skills', {}))} skill categories")


if __name__ == "__main__":
    main()
