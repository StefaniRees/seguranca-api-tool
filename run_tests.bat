@echo off
setlocal

echo Limpando arquivos antigos...
if exist report.html del report.html
if exist log.txt del log.txt

echo Definindo PYTHONPATH...
set PYTHONPATH=%CD%

echo Rodando testes com pytest...
pytest --html=report.html --self-contained-html --log-cli-level=INFO > pytest_output.log 2>&1

echo Abrindo relatório HTML...
start report.html

echo Testes concluídos. Logs em pytest_output.log e log.txt.

endlocal
pause
