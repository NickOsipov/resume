"""
Invoke tasks for building resume PDFs and website.

Usage:
    invoke --list                 # List all available tasks
    invoke build-site             # Build HTML from LaTeX
    invoke copy-pdfs              # Copy PDFs from tex directories
    invoke build-all              # Build everything
    invoke clean                  # Clean temporary files
"""

import os
from invoke import task
from pathlib import Path

RESUMES_DIR = Path("pdf")
RESUME_RU_PDF = os.path.join(RESUMES_DIR, "Resume_NickOsipov_MLOps_RU.pdf")
RESUME_EN_PDF = os.path.join(RESUMES_DIR, "Resume_NickOsipov_MLOps_EN.pdf")
INDEX_HTML = "index.html"


@task
def copy_ru(c):
    """Copy Russian PDF from tex/ru directory."""
    print(f"📄 Copying Russian PDF...")
    c.run(f"cp tex/ru/resume.pdf {RESUME_RU_PDF}")
    print(f"✓ Copied to {RESUME_RU_PDF}")


@task
def copy_en(c):
    """Copy English PDF from tex/en directory."""
    print(f"📄 Copying English PDF...")
    c.run(f"cp tex/en/resume.pdf {RESUME_EN_PDF}")
    print(f"✓ Copied to {RESUME_EN_PDF}")


@task(copy_ru, copy_en)
def copy_pdfs(c):
    """Copy all PDFs from tex directories."""
    print("✓ All PDFs copied successfully!")


@task
def build_site(c):
    """Build HTML site from LaTeX source files."""
    print("🔨 Building HTML site from LaTeX sources...")
    c.run("python3 scripts/build_site.py")


@task
def compile_latex_en(c):
    """Compile English LaTeX resume."""
    print("📝 Compiling English LaTeX resume...")
    with c.cd("tex/en"):
        c.run("latexmk -pdf -interaction=nonstopmode resume.tex")
    print("✓ English resume compiled")


@task
def compile_latex_ru(c):
    """Compile Russian LaTeX resume."""
    print("📝 Compiling Russian LaTeX resume...")
    with c.cd("tex/ru"):
        c.run("latexmk -pdf -interaction=nonstopmode resume.tex")
    print("✓ Russian resume compiled")


@task(compile_latex_en, compile_latex_ru)
def compile_latex(c):
    """Compile all LaTeX resumes."""
    print("✓ All LaTeX files compiled successfully!")


@task(compile_latex, copy_pdfs, build_site)
def build_all(c):
    """Build everything: compile LaTeX, copy PDFs, and build HTML site."""
    print("\n" + "="*60)
    print("✓ Complete build finished successfully!")
    print("="*60)
    print(f"\nGenerated files:")
    print(f"  - {RESUME_EN_PDF}")
    print(f"  - {RESUME_RU_PDF}")
    print(f"  - {INDEX_HTML}")
    print(f"\nWebsite ready for deployment! 🚀")


@task
def clean(c):
    """Clean LaTeX temporary files."""
    print("🧹 Cleaning temporary files...")

    extensions = [
        "*.aux", "*.log", "*.out", "*.fdb_latexmk",
        "*.fls", "*.synctex.gz", "*.bbl", "*.bcf",
        "*.blg", "*.run.xml", "*.toc"
    ]

    for directory in ["tex/en", "tex/ru"]:
        for ext in extensions:
            c.run(f"rm -f {directory}/{ext}", warn=True)

    print("✓ Cleanup complete!")


@task
def watch_latex_en(c):
    """Watch and auto-compile English LaTeX on changes."""
    print("👀 Watching English LaTeX files for changes...")
    print("Press Ctrl+C to stop")
    with c.cd("tex/en"):
        c.run("latexmk -pdf -pvc -interaction=nonstopmode resume.tex")


@task
def watch_latex_ru(c):
    """Watch and auto-compile Russian LaTeX on changes."""
    print("👀 Watching Russian LaTeX files for changes...")
    print("Press Ctrl+C to stop")
    with c.cd("tex/ru"):
        c.run("latexmk -pdf -pvc -interaction=nonstopmode resume.tex")


@task
def serve(c, port=8000):
    """Start local HTTP server to preview the website."""
    print(f"🌐 Starting local server at http://localhost:{port}")
    print("Press Ctrl+C to stop")
    c.run(f"python3 -m http.server {port}")


@task
def deploy(c, message="Update resume and website"):
    """Build everything and deploy to GitHub Pages."""
    print("🚀 Deploying to GitHub Pages...")

    # Build everything
    build_all(c)

    # Git operations
    print("\n📦 Committing changes...")
    c.run("git add index.html pdf/ scripts/build_site.py tasks.py")

    commit_message = f'''{message}

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>'''

    c.run(f'git commit -m "{commit_message}"', warn=True)

    print("\n⬆️  Pushing to GitHub...")
    c.run("git push origin main")

    print("\n✓ Deployment complete!")
    print("Your site will be live at: https://nickosipov.github.io/resume/")


@task
def status(c):
    """Show git status and build info."""
    print("📊 Git Status:")
    print("=" * 60)
    c.run("git status --short")

    print("\n📁 Build Files:")
    print("=" * 60)

    files = [RESUME_EN_PDF, RESUME_RU_PDF, INDEX_HTML]
    for file in files:
        path = Path(file)
        if path.exists():
            size = path.stat().st_size / 1024  # KB
            print(f"  ✓ {file:<40} {size:>8.1f} KB")
        else:
            print(f"  ✗ {file:<40} (not found)")


@task
def check_deps(c):
    """Check if all required dependencies are installed."""
    print("🔍 Checking dependencies...")
    print("=" * 60)

    # Check Python
    print("\nPython:")
    c.run("python3 --version")

    # Check LaTeX
    print("\nLaTeX:")
    result = c.run("which latexmk", warn=True, hide=True)
    if result.ok:
        c.run("latexmk -v | head -1")
        print("  ✓ latexmk found")
    else:
        print("  ✗ latexmk not found (needed for LaTeX compilation)")

    # Check git
    print("\nGit:")
    c.run("git --version")

    # Check invoke
    print("\nInvoke:")
    c.run("python3 -c 'import invoke; print(f\"invoke {invoke.__version__}\")'")

    print("\n✓ Dependency check complete!")


@task
def init(c):
    """Initialize development environment."""
    print("🔧 Initializing development environment...")

    # Check dependencies
    check_deps(c)

    # Install Python dependencies if requirements.txt exists
    req_file = Path("requirements.txt")
    if req_file.exists():
        print("\n📦 Installing Python dependencies...")
        c.run("uv sync")

    # Build initial version
    print("\n🔨 Building initial version...")
    build_site(c)

    print("\n✓ Initialization complete!")
    print("\nYou can now run:")
    print("  invoke build-site    # Build HTML from LaTeX")
    print("  invoke build-all     # Build everything")
    print("  invoke deploy        # Deploy to GitHub Pages")
    print("  invoke --list        # See all available tasks")


@task
def migrate_structure(c):
    """Migrate from old tex_en/tex_ru structure to new tex/en, tex/ru structure."""
    import shutil
    from pathlib import Path
    
    print("🔄 Migrating directory structure...")
    
    old_dirs = ["tex_en", "tex_ru"]
    new_mapping = {"tex_en": "tex/en", "tex_ru": "tex/ru"}
    
    for old_dir in old_dirs:
        old_path = Path(old_dir)
        if old_path.exists():
            new_dir = new_mapping[old_dir]
            new_path = Path(new_dir)
            
            print(f"  Migrating {old_dir} → {new_dir}")
            
            # Create parent directory
            new_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy files if new directory doesn't exist
            if not new_path.exists():
                shutil.copytree(old_path, new_path)
                print(f"  ✓ Copied {old_dir} to {new_dir}")
            else:
                print(f"  ⚠ {new_dir} already exists, skipping")
            
            # Ask for confirmation before removing old directory
            response = input(f"  Remove old directory {old_dir}? [y/N]: ")
            if response.lower() == 'y':
                shutil.rmtree(old_path)
                print(f"  ✓ Removed {old_dir}")
            else:
                print(f"  ⊘ Keeping {old_dir}")
    
    print("\n✓ Migration complete!")
    print("\nNew structure:")
    c.run("tree -L 2 tex/ || ls -la tex/")
