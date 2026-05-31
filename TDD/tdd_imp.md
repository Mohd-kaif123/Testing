1) Pip Environment Active karke liye:-
==> pipenv shell

2) Verify karne ke liye:-
==> pip list | grep selenium

3) bahar aane ke liye:-
==> exit

4) file run karne ke liye:-
==> python3 yourfilename.py

# fir bhi run na ho tu VS code ko batoa ki ham virtual env me hai:-
1) Apne keyboard par Ctrl + Shift + P dabayein. Isse VS Code ka Command Palette khulega.

2) Upar ek search bar aayega, usme likhiye: Python: Select Interpreter aur uspar click kar dijiye.

3) Ab aapke samne ek list aayegi. Us list me dhyan se dekhiye, aapko ek option dikhega jiske aage Pipenv ya aapka wahi folder name Gitflow-vBET9Dks likha hoga.

4) Us wale Python par click karke select kar lijiye.

# Best Method (Another Method) :-
1) Apne terminal me (jahan aapne pipenv shell chalaya hua hai), yeh command run kijiye:
==> which python
(Yeh aapko aapke virtual environment ka exact path nikal kar dega, jaise: /home/manso/.local/share/virtualenvs/Gitflow-vBET9Dks/bin/python)

2) Us poore path ko terminal se copy kar lijiye.

3) Wapas Ctrl + Shift + P dabayein aur Python: Select Interpreter par jayein.

4) List me sabse upar ek option hoga: + Enter interpreter path..., us par click karein.

5) Jo path aapne copy kiya tha, usse wahan paste karke Enter daba dein.

############################################################################

Situation                  Command
Venv activatesource        /mnt/d/Gitflow/TDD/venv/bin/activate
Script run karo             runpy fb_test.py
Chrome hang kare            sudo systemctl start haveged
Selenium reinstall          pip install selenium (jab venv active ho)ChromeDriver check          chromedriver --version
Chrome check                google-chrome-stable --version