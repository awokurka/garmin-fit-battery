# garmin-fit-battery
Python Flask Script which tries to get Sensors Battery Levels from a Garmin .fit File if any where recorded.

## Disclaimer: Do not run this image on a Public or Internet facing Computer/Server
This was built in mind to run it locally. Do not run it on public servers, as there are no security mechanisms int the code, preventing that other files than .fit Files (e.g. malware, malicious code, unwanted data) can be uploaded with this script! You have been warned.

## Where do i find my .fit File?
Login to connect.garmin.com
Choose your activity -> right upper corner click on the gearwheel and select export original.
Extract the .zip File and as a result you will get your Activity .fit File

## How do i run this Script?
Install Docker Runtime on your Computer -> see https://docs.docker.com/engine/install/ for details

Pull and Run a precompiled Image from dockerhub:
`docker run -p 5000:5000 nailz/garmin-fit-battery:latest`

Open your Browser and open http://localhost:5000
Select the .fit File which you have downloaded and extracted from https://connect.garmin.com and click upload.

![Upload Form](https://raw.githubusercontent.com/awokurka/garmin-fit-battery/master/static/index.png "Upload .fit")

You should now see a Table containing the Sensors and their Battery Levels. Keep in mind that not everytime a Value for Battery Level or Voltage is written into the .fit File. If this is the cause, then the Tool has no Data to read out of the file.

![Result Table](https://raw.githubusercontent.com/awokurka/garmin-fit-battery/master/static/content.png "Result Table")

## How do i build my own Docker Image?
Clone the Repository with git and change into the cloned directory. Then run:
`docker build -t garmin-fit-battery .`

## Can you check my .fit File? Can you add the follwing feature?
This Code is free software, published under MIT License. Feel free to clone and edit it so that it fits your needs.

## Did you write the .fit Parser on your own?
No i just wrote some wrapper around it, you can find the original Library here: https://github.com/dtcooper/python-fitparse

