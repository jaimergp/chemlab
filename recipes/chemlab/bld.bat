python setup.py build --compiler=mingw32
if errorlevel 1 exit 1
python setup.py install
if errorlevel 1 exit 1
