# BabyMonitor

To Run:

Ensure that you are working on the correct virtual environment and in the correct directory.  
python3 babymonitor.py 

On a device connected to the same network search for hostname:5000 in any browser. eg. http://192.168.1.101:5000/  
hostname -l (will display the correct hostname)

Hardware:

Raspberry Pi 4  
[Camera](https://thepihut.com/collections/raspberry-pi-camera/products/wide-angle-1080p-uvc-compliant-usb-camera-module-with-metal-case) - this works for me as it has a built in microphone. The Rpi camera will work but small changes to the code will be required. A separate microphone will be required.  
[Temperature Probe](https://www.amazon.co.uk/gp/product/B07TKTFKMW/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1) - I used one of these. It seems fairly accurate compared to a normal thermometer.  

To Do:

1. Improve the index.html so that the webpage looks better.  
2. Create a threshold for the microphone - it is very sensitive.
3. Reduce the time delay of the microphone.

Guides:

[Setting up opencv](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/)  
[Setting up the temperature probe](https://pimylifeup.com/raspberry-pi-temperature-sensor/) - I used a breadboard for testing and then soldered.  
[Video Streaming](https://towardsdatascience.com/video-streaming-in-web-browsers-with-opencv-flask-93a38846fe00)  
[Setting up the microphone](https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone)  
[Twilio Blog](https://www.twilio.com/blog/smart-baby-monitor-python-raspberry-pi-twilio-sms-peripheral-sensors)  
