# garmin-fit-battery
Python Flask Script which tries to get Sensors Battery Levels from a Garmin .fit File if any where recorded.

## Where do i find my .fit File?
Login to connect.garmin.com
Choose your activity -> right upper corner click on the gearwheel and select export original.
Extract the .zip File and as a result you will get your Activity .fit File

## How to run
Install Docker Runtime on your Computer -> see docker.com for details

Pull and Run Image from dockerhub:
docker run -p 5000:5000 nailz/garmin-fit-battery:latest

Open your Browser and open http://localhost:5000
Select the .fit File which you have downloaded and extracted from connect.garmin.com and click upload.

You should now see a Table containing the Sensors and their Battery Levels. Keep in mind that not everytime a Value for Battery Level or Voltage is written into the .fit File. If this is the cause, then the Tool has no Data to read out of the file.



