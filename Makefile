RESUME_RU_PDF=Resume_OsipovNO_MLOps_RU.pdf
RESUME_EN_PDF=Resume_OsipovNO_MLOps_EN.pdf

copy-ru:
	cp tex_ru/resume.pdf ${RESUME_RU_PDF}

copy-en:
	cp tex_en/resume.pdf ${RESUME_EN_PDF}

copy-all: copy_ru copy_en