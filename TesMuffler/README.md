License: GNU General Public License V2

Commmands to use after recently GitHub repo move:
git config --get remote.origin.url
git remote set-url origin https://github.com/TesCustoms/Tes.git

Two options for setting up Git on command line: <br>
1) Using offical gh CLI (HIGHLY RECOMMENDED) - https://cli.github.com/ and for Raspberry Pi see https://github.com/cli/cli/blob/trunk/docs/install_linux.md also <br>
2) Create one time personal token - https://aka.ms/gcm/credstores and key command to run export GCM_CREDENTIAL_STORE=secretservice <br>
<br>

Hardware Required: <br>
1) Hardware Dongle from CANOPi [TesCustoms P/N 100-0001-A](https://github.com/TesCustoms/TesMufflerDongle) <br>
2) OHP OBD2 Adapter Harness [Manufacture P/N 10246](www.amazon.com/dp/B08DXY5KVX/ref=cm_sw_r_cp_api_glt_fabc_M5VV59NMV6AZKJVCRG4D?) <br>
3) Custom 3D CAD file [TesMufflerCADv1.stl](https://github.com/OpenSourceIronman/Tes/blob/master/TesMuffler/TesMufflerCADv1.stl) 3D printed muffler with magnets <br>
<br>

Python APIs project is exploring: <br>
1) Tesla API is a community of developers who are reverse engineering Tesla's API: https://teslaapi.dev/ <br> 
2) Smartcar API lets you read vehicle data (location, odometer) and send commands to vehicles (lock, unlock) to connected vehicles using HTTP requests: https://github.com/smartcar/python-sdk <br>
3) The Comma Pedal is a gas pedal interceptor. It is a device that is inserted between a car's electronic gas pedal and the ECU (Engine Control Unit): https://github.com/commaai/openpilot/wiki/comma-pedal <br>
4) All Comma Software: https://github.com/commaai/panda/tree/ad12330d506ca31fe16f99a5b5aca76aab8a1ec9 <br>
5) TODO https://teslascope.com/
<br>

Next steps: <br>
Download the following sounds using "youtube-dl --extract-audio --audio-format mp3 http://videoURL" linux command
1) [McLaren F1](www.youtube.com/watch?v=mOI8GWoMF4M) <br>
2) [Ferrari LaFerrari](https://www.youtube.com/watch?v=B4Th3LxCgb4) <br>
3) [Porcshe 911](https://www.youtube.com/watch?v=O1Kyt1qDL30) <br>
4) [BWM M4](https://www.youtube.com/watch?v=0RFoYCG4_TE) <br>
5) [Jaguar E Type Series 1](https://www.youtube.com/watch?v=44sNpPYw5Bo) <br>
6) [Ford Model T](https://www.dailymotion.com/video/x35n5if) <br>
7) [Subaru WRX STI](https://youtu.be/d7Gszyz62e0?t=193) <br>
8) [Motor whine directly from your Tesla](https://www.youtube.com/watch?v=j4AxsGk-LdQ) <br>
9) [Star Wars Pod Racer](https://www.youtube.com/watch?v=f7ogSqLwNQ0) <br>
8) OTHER SUGGESTIONS? Tweet me @BlazeDSanders or submit GitHub issue <br>
<br>

Why?: <br>
1) https://www.nhtsa.gov/sites/nhtsa.gov/files/documents/812347-minimumsoundrequirements.pdf <br>
2) https://www.cnbc.com/2017/10/12/tesla-ceo-elon-musk-reveals-he-owns-two-gasoline-cars.html <br>
<br>


TODO: 
Display for PiPico https://www.hackster.io/news/miroslav-nemecek-s-picovga-brings-high-res-video-to-the-raspberry-pi-pico-just-add-resistors-88dd144e7d1c
FIND URLS I DELETED FROM TOP OF EngineSoundGenerator.py FILE https://whimsical.com/tesmuffler-64NBDWF5cd3stpZDvkubzw
AM Radio IC [Manufacture P/N TODO](https://www.petervis.com/Radios/ta7642/ta7642-am-radio-ic.html)
