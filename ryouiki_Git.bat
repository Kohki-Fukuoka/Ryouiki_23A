chcp 65001
:TOP
:ADD

set /p file_name="file name >>> "
git add %file_name%

:MOREADD
set /p moreAdd="add more?[y/n] >>> "
if %moreAdd:Y=Y%==Y (
goto ADD
) else if %moreAdd:N=N%==N (
rem
) else (
echo "!!! illegal inputing !!!"
goto MOREADD
)

git config --global user.email "dzd65062@kwansei.ac.jp"
git config --global user.name "Kohki-Fukuoka"
set /p comment="comment of file >>> "
git commit -m %comment%
git push

:REPUSH
set /p repush="push other programs?[y/n] >>> "
if %repush:Y=Y%==Y (
goto TOP
) else if %repush:N=N%==N (
rem
) else (
echo "!!! illegal inputing !!!"
goto REPUSH
)

pause