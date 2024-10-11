RESUME_RU_PDF=Resume_OsipovNO_MLOps_RU.pdf
RESUME_EN_PDF=Resume_OsipovNO_MLOps_EN.pdf

copy_ru:
	cp tex_ru/resume.pdf ${RESUME_RU_PDF}

copy_en:
	cp tex_en/resume.pdf ${RESUME_EN_PDF}

copy_all: copy_ru copy_en

git_config:
	git config --local user.name "NickOsipov"
	git config --local user.email "nick.osipov.91@gmail.com"