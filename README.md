# Nick Osipov - MLOps Engineer Resume

<p align="center">
<img src="https://raw.githubusercontent.com/NickOsipov/resume/main/assets/mlops.gif" width="1000">
</p>

## 🌐 Live Website

**https://nickosipov.github.io/resume/**

Modern resume website with:
- 📄 Downloadable PDF resumes (English & Russian)
- 💼 Work experience and skills
- 🔗 Social links (GitHub, LinkedIn, Telegram)
- 📱 Fully responsive design

## 📥 PDF Resumes

- 🇬🇧 [English Version](pdf/Resume_NickOsipov_MLOps_EN.pdf)
- 🇷🇺 [Russian Version](pdf/Resume_NickOsipov_MLOps_RU.pdf)

## 🚀 Quick Start

```bash
# Build HTML from LaTeX
invoke build-site

# Build everything (compile LaTeX → copy PDFs → generate HTML)
invoke build-all

# Deploy to GitHub Pages
invoke deploy

# Local preview
invoke serve
```

See [Quick Start Guide](docs/QUICKSTART.md) for more commands.

## 📚 Documentation

- **[Quick Start](docs/QUICKSTART.md)** - Essential commands and typical workflow
- **[Tasks Guide](docs/README_TASKS.md)** - Complete guide to all Invoke tasks
- **[Project Structure](docs/PROJECT_STRUCTURE.md)** - Directory layout and data flow
- **[Migration Guide](docs/MIGRATION.md)** - Migrating from old structure
- **[Build System](docs/BUILD_SITE.md)** - How the build system works

## 🛠️ Tech Stack

**Build System:**
- [Invoke](https://www.pyinvoke.org/) - Python task automation
- Python 3.8+ - Build scripts
- LaTeX (latexmk) - PDF compilation

**Resume Format:**
- LaTeX - Source format
- HTML/CSS - Website
- PDF - Downloadable versions

## 📁 Project Structure

```
resume/
├── tex/                    # LaTeX source files
│   ├── en/                # English version
│   └── ru/                # Russian version
├── pdf/                    # Generated PDFs
├── scripts/                # Build scripts
├── docs/                   # Documentation
├── index.html             # Generated website
└── tasks.py               # Invoke automation
```

## 🔄 Workflow

When you update LaTeX files:

```bash
# 1. Edit LaTeX
vim tex/en/resume_sections/experience.tex

# 2. Build everything
invoke build-all

# 3. Deploy
invoke deploy
```

The website automatically updates from LaTeX sources!

## 🎯 Features

### Automated Build System
- ✅ Single command to build everything
- ✅ Automatic HTML generation from LaTeX
- ✅ PDF compilation and copying
- ✅ Live preview server
- ✅ Git deployment automation

### Content Synchronization
- ✅ Website syncs with LaTeX (experience, skills)
- ✅ Dual language support (EN/RU)
- ✅ PDF download buttons
- ✅ Social links integration

### Developer Experience
- ✅ Invoke task runner (Python-based)
- ✅ Watch mode for auto-compilation
- ✅ Clean temporary files
- ✅ Status checking
- ✅ Comprehensive documentation

## 📋 Available Commands

```bash
invoke --list              # Show all tasks
invoke build-site          # Build HTML from LaTeX
invoke build-all           # Full build pipeline
invoke compile-latex       # Compile both LaTeX versions
invoke copy-pdfs           # Copy PDFs to pdf/
invoke clean               # Clean temp files
invoke watch-latex-en      # Auto-compile on changes
invoke serve               # Local web server
invoke deploy              # Deploy to GitHub Pages
invoke status              # Show project status
```

## 🔧 Setup

### Prerequisites
- Python 3.8+
- LaTeX distribution (optional, for PDF compilation)
- Git

### Installation

```bash
# Install dependencies
pip install invoke

# Or with uv
uv sync

# Initialize
invoke init
```

## 🤝 Contributing

This is a personal resume repository. For questions or suggestions:
- Open an issue
- Contact via [Telegram](https://t.me/NickOsipov)
- Email: nick.osipov.91@gmail.com

## 📄 License

Personal resume - All rights reserved

## 🔗 Links

- **Website**: https://nickosipov.github.io/resume/
- **GitHub**: https://github.com/NickOsipov
- **LinkedIn**: https://linkedin.com/in/nickosipov
- **Telegram**: https://t.me/NickOsipov

---

Built with ❤️ using Python, LaTeX, and Invoke
