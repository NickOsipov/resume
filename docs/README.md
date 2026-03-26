# Resume Project Documentation

Welcome to the documentation for Nick Osipov's resume build system!

## 📚 Documentation Index

### Getting Started
- **[QUICKSTART.md](QUICKSTART.md)** - Quick start guide with essential commands
  - Basic commands
  - Typical workflow
  - Why Invoke over Makefile

### Comprehensive Guides
- **[README_TASKS.md](README_TASKS.md)** - Complete Invoke tasks documentation
  - All available commands
  - Usage examples
  - Troubleshooting
  - Project structure
  - Workflow descriptions

### Technical Details
- **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Project architecture
  - Directory structure
  - Data flow diagrams
  - Build pipeline
  - Dependencies

- **[BUILD_SITE.md](BUILD_SITE.md)** - Build system internals
  - How LaTeX parsing works
  - HTML generation
  - Customization guide

### Migration & Maintenance
- **[MIGRATION.md](MIGRATION.md)** - Directory structure migration guide
  - Old vs new structure
  - Migration steps
  - Rollback instructions

## 🎯 Quick Navigation

**I want to...**

- **Start using the system** → [QUICKSTART.md](QUICKSTART.md)
- **See all available commands** → [README_TASKS.md](README_TASKS.md#available-commands)
- **Understand the project structure** → [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
- **Customize the website** → [BUILD_SITE.md](BUILD_SITE.md#customization)
- **Migrate old directories** → [MIGRATION.md](MIGRATION.md)
- **Troubleshoot issues** → [README_TASKS.md](README_TASKS.md#troubleshooting)

## 🚀 Quick Start Summary

```bash
# Build HTML from LaTeX
invoke build-site

# Build everything
invoke build-all

# Deploy to GitHub Pages
invoke deploy

# See all commands
invoke --list
```

## 📖 Documentation Structure

```
docs/
├── README.md              # This file - documentation index
├── QUICKSTART.md          # Quick start guide
├── README_TASKS.md        # Complete tasks reference
├── PROJECT_STRUCTURE.md   # Architecture documentation
├── BUILD_SITE.md          # Build system details
└── MIGRATION.md           # Migration guide
```

## 🔗 External Links

- **Live Website**: https://nickosipov.github.io/resume/
- **GitHub Repository**: https://github.com/NickOsipov/resume
- **Invoke Documentation**: https://www.pyinvoke.org/

## 💡 Tips

1. **Start with QUICKSTART.md** if you're new to the project
2. **Use README_TASKS.md** as a reference for all commands
3. **Check PROJECT_STRUCTURE.md** to understand how everything fits together
4. **Read BUILD_SITE.md** if you want to customize the website

## 🤝 Need Help?

- Check the [Troubleshooting section](README_TASKS.md#troubleshooting)
- Open an issue on GitHub
- Contact: [Telegram](https://t.me/NickOsipov) | [Email](mailto:nick.osipov.91@gmail.com)

---

**Last Updated**: March 2026
