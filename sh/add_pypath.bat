:: Ajoute le path de la racine du projet
:: Attention lancer sous la recine projet !
@echo off
set proj_path=%cd%
set proj_path=%proj_path:\sh=%
echo %proj_path%
set PYTHONPATH=%PYTHONPATH%;%proj_path%
echo variable PYTHONPATH:
echo %PYTHONPATH%

