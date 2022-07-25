Hardware Required: <br>
1) ESP-32 Dev Kit [Supplier P/N WROOM](https://acrobotic.com/products/acr-00024/) <br>
2) AM Radio IC [Manufacture P/N TODO](https://www.petervis.com/Radios/ta7642/ta7642-am-radio-ic.html)
3) Custom PCBA [P/N 100-0001-A](https://www.upverter.com)
4) OHP OBD2 Adapter Harness [Manufacture P/N 10246](www.amazon.com/dp/B08DXY5KVX/ref=cm_sw_r_cp_api_glt_fabc_M5VV59NMV6AZKJVCRG4D?) <br>
5) Parallax LASER rangefinder [SKU 28041](https://www.parallax.com/product/laserping-2m-rangefinder/) <br>
6) Custom 3D CAD file [TesMufflerCADv1.stl](https://github.com/OpenSourceIronman/Tes/blob/master/TesMuffler/TesMufflerCADv1.stl) 3D printed muffler with magnets <br>
<br>

Setting up and building the TesMuffler ESP-32 project: <br>
Make sure your USB cable works by running “lsusb” command in terminal: (I didnt waste 1 hour on this...) <br>
Something like "Bus 002 Device 001: ID 10c4:ea60 Silicon Laboratories, Inc. CP2104 USB to UART Bridge Controller  Serial: 020911PT" should display in terminal <br>
<br>

Commands: <br>
1) Run TODO "cd esp-rainmaker/TesMuffler/" to navigate to project code directory <br>
2) Run "idf.py monitor" on a 2nd terminal tab or click the computer monitor button along bottom of window inside VS Code to get serial debugging interface <br>
3) Run "idf.py menuconfig" on your 1st terminal tab to provision ESP and connect to internet https://rainmaker.espressif.com/docs/claiming.html <br>
4) Run "idf.py build" on your 1st terminal tab to complie the binary on your local PC / Mac
5) Run "idf.py -p /dev/cu.usbserial-020911PT flash" to push firmware to ESP-32 EEPROM <br>

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

Competition: <br>
1) https://madnessautoworks.com/tesla-model-3-active-exhaust-sound-controller-milltek-single-sound-generator-115036 <br>
<br>
2) https://www.amazon.com/gp/product/B0876QCYF4/ref=ox_sc_act_title_1?smid=A1H95AF7GCEQR&psc=1 <br>
3) https://www.amainhobbies.com/team-associated-sense-innovations-essone-2017-engine-sound-simulator-system-asc29262/p-qtaetquqyzzxactz <br>
<br>

Why?: <br>
1) https://www.nhtsa.gov/sites/nhtsa.gov/files/documents/812347-minimumsoundrequirements.pdf <br>
2) https://www.cnbc.com/2017/10/12/tesla-ceo-elon-musk-reveals-he-owns-two-gasoline-cars.html <br>
<br>

Feature requests: TODO Make Github Issue
1) https://twitter.com/u110110/status/1414227401521967104?s=21 <br>
<br>

TODO: 
Purchase LOGO: https://www.shutterstock.com/image-vector/tc-initial-letters-looping-linked-circle-1724747953
Display for PiPico https://www.hackster.io/news/miroslav-nemecek-s-picovga-brings-high-res-video-to-the-raspberry-pi-pico-just-add-resistors-88dd144e7d1c
FIND URLS I DELETED FROM TOP OF EngineSoundGenerator.py FILE https://whimsical.com/tesmuffler-64NBDWF5cd3stpZDvkubzw




