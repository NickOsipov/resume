# Структура проекта Resume

```
resume/
│
├── 📄 index.html                    # Главная страница сайта (генерируется автоматически)
│
├── 📁 tex/                          # LaTeX исходники
│   ├── en/                          # Английская версия
│   │   ├── resume.tex               # Главный файл
│   │   ├── fed-res.cls              # Стиль документа
│   │   ├── resume.pdf               # Скомпилированный PDF
│   │   └── resume_sections/         # Секции резюме
│   │       ├── experience.tex       # Опыт работы → index.html
│   │       ├── skills.tex          # Навыки → index.html
│   │       └── education.tex       # Образование
│   │
│   └── ru/                          # Русская версия
│       ├── resume.tex
│       ├── fed-res.cls
│       ├── resume.pdf
│       └── resume_sections/
│           ├── experience.tex
│           ├── skills.tex
│           └── education.tex
│
├── 📁 pdf/                          # Финальные PDF файлы
│   ├── Resume_NickOsipov_MLOps_EN.pdf
│   └── Resume_NickOsipov_MLOps_RU.pdf
│
├── 📁 scripts/                      # Скрипты сборки
│   └── build_site.py               # Python скрипт: LaTeX → HTML
│
├── 📁 assets/                       # Медиа файлы
│   └── mlops.gif                   # GIF для сайта
│
├── 🔧 tasks.py                      # Invoke задачи (автоматизация)
├── 📋 requirements.txt              # Python зависимости
├── 📋 pyproject.toml                # Конфигурация проекта (uv)
│
├── 📖 README.md                     # Главный README
├── 📖 README_TASKS.md               # Документация Invoke задач
├── 📖 QUICKSTART.md                 # Быстрый старт
├── 📖 MIGRATION.md                  # Гид по миграции структуры
│
├── 🛠️ Makefile                      # Make команды (legacy)
├── 🙈 .gitignore                    # Git ignore правила
└── 🔒 .python-version               # Версия Python (для uv)
```

## Workflow данных

```
LaTeX Sources           Build Process              Output
━━━━━━━━━━━━━          ━━━━━━━━━━━━━             ━━━━━━━━━

tex/en/resume.tex  ─┐
                    ├─→ latexmk ────→ tex/en/resume.pdf ─┐
tex/en/sections/   ─┘                                     │
                                                           ├─→ copy ─→ pdf/*.pdf
tex/ru/resume.tex  ─┐                                     │
                    ├─→ latexmk ────→ tex/ru/resume.pdf ─┘
tex/ru/sections/   ─┘

tex/en/sections/   ─┐
  experience.tex    │
  skills.tex        ├─→ build_site.py ─────────────────→ index.html
  education.tex    ─┘      (parser)
```

## Команды сборки

```bash
# Полный цикл
invoke build-all        # LaTeX → PDF → HTML

# Отдельные этапы
invoke compile-latex-en # LaTeX → PDF (EN)
invoke compile-latex-ru # LaTeX → PDF (RU)
invoke copy-pdfs        # PDF → pdf/
invoke build-site       # LaTeX → HTML
```

## Деплой

```bash
invoke deploy          # build-all + git commit + push
                       # → GitHub Pages автоматически обновляется
```

## Зависимости

- **Python 3.8+** - для скриптов
- **invoke** - автоматизация задач
- **latexmk** - компиляция LaTeX (опционально)
- **git** - версионный контроль
- **uv** - менеджер Python зависимостей (опционально)
