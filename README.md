## ddns_ovh
The DDNS script for OVH automatically updates the public IP address assigned to an OVH domain every 30 minutes. It uses the ipify API to retrieve the current IP address and sends an update to the OVH DDNS system. All operational messages are logged in a log file, making it easy to monitor the process.

## Configuration

Before running the script, you need to configure it with your specific details:

1. **Username and Password**: Open the `script.py` file in a text editor and locate the following lines:

   ```python
   USERNAME = "your_username"  # Replace with your OVH username
   PASSWORD = "your_password"  # Replace with your OVH password
   
2. **Domain**: In the same file, find this line:
   
   hostname = "your_domain.pl"  # Replace with your domain

3. **Update Interval**: You can change the update interval according to your needs by modifying the following line:

   time.sleep(1800)  # This sets the interval to 30 minutes (1800 seconds)
