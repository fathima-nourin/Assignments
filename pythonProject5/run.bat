@REM Feel free to comment/uncomment things based on your use case.


@REM Data and config initializers.
mkdir "conf"
copy nul "conf/application.conf" > nul
mkdir "data/keys"

@REM Default structures.
mkdir "scripts"
copy nul "scripts/__init__.py" > nul

mkdir "scripts/config"
copy nul "scripts/config/__init__.py" > nul

mkdir "scripts/constants"
copy nul "scripts/constants/__init__.py" > nul

mkdir "scripts/core"
copy nul "scripts/core/__init__.py" > nul

mkdir "scripts/core/engines"
copy nul "scripts/core/engines/__init__.py" > nul

mkdir "scripts/core/handlers"
copy nul "scripts/core/handlers/__init__.py" > nul

mkdir "scripts/db"
copy nul "scripts/db/__init__.py" > nul

mkdir "scripts/errors"
copy nul "scripts/errors/__init__.py" > nul

mkdir "scripts/logging"
copy nul "scripts/logging/__init__.py" > nul

mkdir "scripts/schemas"
copy nul "scripts/schemas/__init__.py" > nul

mkdir "scripts/services"
copy nul "scripts/services/__init__.py" > nul

mkdir "scripts/utils"
copy nul "scripts/utils/__init__.py" > nul



@REM Basic files initializers
copy nul "___init___.py" > nul
copy nul "app.py" > nul
copy nul "main.py" > nul
copy ".vscode\n.idea\n__pycache__\/\nlogs\ndata\n" ".gitignore" > nul
copy nul ".env" > nul
copy nul "default_env" > nul
copy nul "requirements.txt" > nul
copy nul "__version__.py" > nul