pytest -v -s --disable-warnings -m "group2" --browser chrome --html=HTMLReports/xyzAbat.html -n=2 --alluredir="AllureReports"
allure serve "AllureReports"