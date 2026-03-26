# Building the Resume Website

This repository contains an automated system for building a GitHub Pages website from LaTeX resume files.

## Overview

The website at `https://nickosipov.github.io/resume/` is automatically generated from the English LaTeX resume files in the `tex_en/` directory.

## How It Works

### 1. Source Files

- **LaTeX Resume**: `tex_en/resume.tex` and files in `tex_en/resume_sections/`
  - `experience.tex` - Work experience
  - `skills.tex` - Technical skills
  - `education.tex` - Education

### 2. Build Script

- **`build_site.py`** - Python script that:
  - Parses LaTeX files to extract content
  - Generates HTML with styling
  - Creates `index.html` with:
    - About Me section
    - Work Experience (from LaTeX)
    - Skills (from LaTeX)
    - Download buttons for PDF resumes
    - Social links

### 3. Makefile Commands

```bash
# Build only the HTML site
make build-site

# Copy PDFs from tex directories
make copy-all

# Build everything (PDFs + HTML)
make build-all
```

## Workflow for Updating the Website

When you update your LaTeX resume:

1. **Edit LaTeX files** in `tex_en/`:
   ```bash
   vim tex_en/resume_sections/experience.tex
   vim tex_en/resume_sections/skills.tex
   ```

2. **Rebuild PDFs** (if using LaTeX compiler):
   ```bash
   cd tex_en && pdflatex resume.tex
   cd ../tex_ru && pdflatex resume.tex
   ```

3. **Build the website**:
   ```bash
   make build-all
   ```

4. **Commit and push**:
   ```bash
   git add index.html Resume_*.pdf
   git commit -m "Update resume and website"
   git push
   ```

5. **GitHub Pages** will automatically update within a few minutes.

## What Gets Synced

The following content is automatically extracted from LaTeX and displayed on the website:

- ✅ Work Experience (all positions, dates, achievements)
- ✅ Skills (all categories and technologies)
- ✅ Contact information (name, title, social links)

## Customization

To customize the website appearance, edit the CSS in `build_site.py` within the `_get_css()` method.

To change the layout or add sections, modify the HTML generation methods in `HTMLGenerator` class.

## Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

## File Structure

```
resume/
├── tex_en/                          # English LaTeX sources
│   ├── resume.tex
│   └── resume_sections/
│       ├── experience.tex           # → Website Experience section
│       ├── skills.tex              # → Website Skills section
│       └── education.tex
├── tex_ru/                          # Russian LaTeX sources
├── build_site.py                    # Build script (LaTeX → HTML)
├── index.html                       # Generated website
├── Resume_NickOsipov_MLOps_EN.pdf  # English PDF
├── Resume_NickOsipov_MLOps_RU.pdf  # Russian PDF
└── Makefile                         # Build automation
```

## Troubleshooting

**Website not updating?**
- Check that `index.html` is committed and pushed
- Wait 2-5 minutes for GitHub Pages to rebuild
- Check repository Settings → Pages for build status

**Content not parsing correctly?**
- Ensure LaTeX files use the expected format
- Run `make build-site` locally to see any errors
- Check the regex patterns in `build_site.py`

## Future Enhancements

Possible improvements:
- Add education section to website
- Support for multiple languages on website
- Automated LaTeX compilation in Makefile
- CI/CD with GitHub Actions to auto-rebuild on LaTeX changes
