RESUME_RU_PDF=Resume_NickOsipov_MLOps_RU.pdf
RESUME_EN_PDF=Resume_NickOsipov_MLOps_EN.pdf
INDEX_HTML=index.html

copy-ru:
	cp tex/ru/resume.pdf ${RESUME_RU_PDF}

copy-en:
	cp tex/en/resume.pdf ${RESUME_EN_PDF}

copy-all: copy-ru copy-en

# Build HTML site from LaTeX source
build-site:
	python3 build_site.py

# Build everything: PDFs and HTML site
build-all: copy-all build-site

.PHONY: copy-ru copy-en copy-all build-site build-all