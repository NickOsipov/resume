# Resume Build System with Invoke

Автоматизированная система для сборки резюме и сайта с использованием Invoke.

## Установка

```bash
# Установка зависимостей
uv sync

# Или с pip
pip install invoke
```

## Доступные команды

### Основные команды

```bash
# Показать все доступные команды
invoke --list

# Собрать HTML сайт из LaTeX
invoke build-site

# Скопировать PDF из tex директорий
invoke copy-pdfs

# Собрать всё (LaTeX → PDF → HTML)
invoke build-all

# Деплой на GitHub Pages
invoke deploy
```

### Работа с LaTeX

```bash
# Скомпилировать английское резюме
invoke compile-latex-en

# Скомпилировать русское резюме
invoke compile-latex-ru

# Скомпилировать оба резюме
invoke compile-latex

# Автоматическая пересборка при изменениях (английский)
invoke watch-latex-en

# Автоматическая пересборка при изменениях (русский)
invoke watch-latex-ru
```

### Утилиты

```bash
# Очистка временных файлов LaTeX
invoke clean

# Показать статус проекта и размеры файлов
invoke status

# Запустить локальный веб-сервер для предпросмотра
invoke serve

# Проверить установленные зависимости
invoke check-deps

# Инициализировать окружение разработки
invoke init
```

## Структура проекта

```
resume/
├── tex/en/                          # Английские LaTeX исходники
│   ├── resume.tex
│   └── resume_sections/
│       ├── experience.tex           # → Сайт: Experience
│       ├── skills.tex              # → Сайт: Skills
│       └── education.tex
├── tex/ru/                          # Русские LaTeX исходники
│   ├── resume.tex
│   └── resume_sections/
├── pdf/                             # Скомпилированные PDF
│   ├── Resume_NickOsipov_MLOps_EN.pdf
│   └── Resume_NickOsipov_MLOps_RU.pdf
├── scripts/
│   └── build_site.py               # Генератор HTML из LaTeX
├── index.html                       # Сгенерированный сайт
├── tasks.py                         # Invoke задачи
└── requirements.txt                 # Python зависимости
```

## Workflow для обновления резюме

### 1. Обновить LaTeX файлы

```bash
# Редактируем LaTeX
vim tex/en/resume_sections/experience.tex
vim tex/en/resume_sections/skills.tex
```

### 2. Собрать всё

```bash
# Полная сборка: LaTeX → PDF → HTML
invoke build-all
```

Эта команда:
- ✅ Компилирует LaTeX → PDF (EN & RU)
- ✅ Копирует PDF в папку `pdf/`
- ✅ Генерирует HTML сайт из LaTeX

### 3. Деплой на GitHub Pages

```bash
# Деплой с коммитом и пушем
invoke deploy

# Деплой с кастомным сообщением
invoke deploy --message "Add new project experience"
```

Эта команда:
- ✅ Собирает всё (`build-all`)
- ✅ Добавляет файлы в git
- ✅ Создаёт коммит с сообщением
- ✅ Пушит на GitHub
- 🌐 GitHub Pages обновляется автоматически!

## Что синхронизируется с LaTeX

Следующий контент автоматически извлекается из LaTeX файлов и отображается на сайте:

- ✅ **Опыт работы** (все позиции, даты, достижения)
- ✅ **Навыки** (все категории и технологии)
- ✅ **Контактная информация** (имя, должность, соцсети)

## Расширенные примеры

### Разработка с авто-пересборкой

Открыть в двух терминалах:

```bash
# Терминал 1: Авто-компиляция LaTeX
invoke watch-latex-en

# Терминал 2: Локальный веб-сервер
invoke build-site && invoke serve
```

Теперь при изменении LaTeX файлов:
1. LaTeX автоматически пересобирается в PDF
2. Обновить сайт: `invoke build-site`
3. Обновить браузер на http://localhost:8000

### Быстрая проверка изменений

```bash
# Показать статус и размеры файлов
invoke status

# Собрать только HTML (быстро)
invoke build-site

# Посмотреть сайт локально
invoke serve
```

### Полный цикл разработки

```bash
# 1. Редактируем LaTeX
vim tex/en/resume_sections/experience.tex

# 2. Компилируем и смотрим PDF
invoke compile-latex-en
open tex/en/resume.pdf

# 3. Обновляем сайт
invoke build-site

# 4. Проверяем локально
invoke serve
# Открыть http://localhost:8000

# 5. Деплоим
invoke deploy
```

## Настройка CI/CD (опционально)

Можно добавить GitHub Actions для автоматической сборки:

```yaml
# .github/workflows/build.yml
name: Build Resume
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
      - run: pip install invoke
      - run: invoke build-site
      - run: git config user.name "GitHub Actions"
      - run: git config user.email "actions@github.com"
      - run: invoke deploy
```

## Troubleshooting

### LaTeX не компилируется

```bash
# Проверить зависимости
invoke check-deps

# Очистить временные файлы
invoke clean

# Попробовать снова
invoke compile-latex-en
```

### Сайт не обновляется

```bash
# Проверить что HTML сгенерирован
invoke build-site
ls -lh index.html

# Проверить что PDF в правильном месте
ls -lh pdf/

# Проверить ссылки в HTML
grep "pdf/" index.html
```

### GitHub Pages не показывает изменения

- Подождите 2-5 минут после пуша
- Проверьте Settings → Pages в GitHub
- Очистите кеш браузера (Ctrl+Shift+R)

## Полезные алиасы

Добавьте в `~/.bashrc` или `~/.zshrc`:

```bash
alias resume-build='invoke build-all'
alias resume-deploy='invoke deploy'
alias resume-serve='invoke serve'
alias resume-status='invoke status'
```

Теперь можно использовать:

```bash
resume-build    # Собрать всё
resume-deploy   # Деплой
resume-serve    # Локальный сервер
resume-status   # Статус
```
