cd "C:\Users\%USERNAME%\AMaDiA"
git pull
%@Try%
  call "C:\Users\%USERNAME%\Anaconda3\Scripts\activate.bat"
  "C:\Users\%USERNAME%\Anaconda3\python.exe" "C:\Users\%USERNAME%\AMaDiA\AMaDiA.py"
  if ["%errorlevel%"]==["0"] GOTO End
%@EndTry%
:@Catch
  call "C:\ProgramData\Anaconda3\Scripts\activate.bat"
  "C:\ProgramData\Anaconda3\python.exe" "C:\Users\%USERNAME%\AMaDiA\AMaDiA.py"
:@EndCatch
:End
if NOT ["%errorlevel%"]==["0"] pause
