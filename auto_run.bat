REM Anhui CT yang
pause

cd /d d:\wlnews
echo "Starting get_a_all.py”
python get_a_all.py

echo "Starting get_bozhou.py“
python get_bozhou.py

echo "Starting txt_to_db.py”
python txt_to_db.py

pause