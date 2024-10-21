import sys
import os
from cx_Freeze import setup, Executable

# Определение пути к Python
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# Добавление зависимостей и файлов
build_exe_options = {
    "packages": ["os", "pygame", "tkinter", "configparser", "holdem_utils"],
    "include_files": [
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
        "prefloptrain.ini",
        "Images/splash.png"  # путь к изображению в папке images
    ]
}


# Настройка базового режима для Windows
base = None
if sys.platform == 'win32':
    base = "Win32GUI"

# Настройка сборки
setup(
    name="Pre-Training",
    version="0.1",
    description="NLHE Preflop Range Trainer",
    options={"build_exe": build_exe_options},
    executables=[Executable("Pre-Training.py", base=base, icon='icon.ico')]
)
