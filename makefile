RESUME_RU_PDF=Resume_OsipovNO_MLE_RU.pdf
RESUME_EN_PDF=Resume_OsipovNO_MLE_EN.pdf

copy_ru:
	cp tex_ru/resume.pdf ${RESUME_RU_PDF}

copy_en:
	cp tex_en/resume.pdf ${RESUME_EN_PDF}

copy_all: copy_ru copy_en
