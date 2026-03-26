# Quick Start Guide

## Основные команды

```bash
# 📋 Список всех команд
invoke --list

# 🔨 Собрать сайт из LaTeX
invoke build-site

# 🚀 Полная сборка (LaTeX → PDF → HTML)
invoke build-all

# 📤 Деплой на GitHub Pages
invoke deploy

# 📊 Статус проекта
invoke status

# 🌐 Локальный сервер (http://localhost:8000)
invoke serve
```

## Типичный workflow

```bash
# 1️⃣ Редактируем резюме
vim tex/en/resume_sections/experience.tex

# 2️⃣ Собираем всё
invoke build-all

# 3️⃣ Проверяем локально
invoke serve

# 4️⃣ Деплоим
invoke deploy
```

## Автоматизация

Вместо Makefile теперь используется **Invoke** (Python task runner).

**Преимущества:**
- ✅ Кроссплатформенность (Linux, macOS, Windows)
- ✅ Python синтаксис вместо Make
- ✅ Лучшая обработка ошибок
- ✅ Более читаемый код
- ✅ Встроенная документация

Подробнее: [README_TASKS.md](README_TASKS.md)
