# 1. Создать корневую папку
mkdir agi-consciousness-engineering
cd agi-consciousness-engineering

# 2. Создать структуру папок
mkdir config core modules mathematics philosophy tests reports

# 3. Создать пустые __init__.py
touch config/__init__.py core/__init__.py modules/__init__.py
touch mathematics/__init__.py philosophy/__init__.py tests/__init__.py
touch reports/.gitkeep

# 4. Скопировать содержимое файлов (см. ниже)
# Откройте каждый файл в текстовом редакторе и вставьте код

# 5. Инициализировать git-репозиторий
git init
git add .
git commit -m "Initial commit: AGI Consciousness Engineering - обезличенная версия"

# 6. Создать ZIP-архив
cd ..
zip -r agi-consciousness-engineering.zip agi-consciousness-engineering/