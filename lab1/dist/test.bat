rem @echo off
SET program="triangle.exe"
if %program% == "" goto err

echo Test1
%program% 0 0 0 > out1.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out1.txt" "Reference/reference1.txt"
if ERRORLEVEL 1 goto testFailed

echo Test2
%program% > out2.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out2.txt" "Reference/reference2.txt"
if ERRORLEVEL 1 goto testFailed

echo Test3
%program% 1 2 3 > out3.txt
if ERRORLEVEL 1 goto testFailed
fc.exe "out3.txt" "Reference/reference3.txt"
if ERRORLEVEL 1 goto testFailed

echo Test4
%program% 4 4 4 > out4.txt
fc.exe "out4.txt" "Reference/reference4.txt"
if ERRORLEVEL 1 goto testFailed

echo Test5
%program% 5 5 6 > out5.txt
fc.exe "out5.txt" "Reference/reference5.txt"
if ERRORLEVEL 1 goto testFailed

echo Test6
%program% 5 6 7 > out6.txt
fc.exe "out6.txt" "Reference/reference6.txt"
if ERRORLEVEL 1 goto testFailed


echo OK
exit /B

:noFile
echo file is missing
exit /B

:testFailed
echo Testing failed
exit /B

:err
echo Usage: test.bat <Path to program>;