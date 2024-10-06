# Key_logger

Update_2024: pwd should be google (app password generated) because less secure app is depreicated from sept 2024

Keylogger Project:
This keylogger application captures and logs keystrokes entered on a system, processing the data into a human-readable format. It uses SMTP to send the captured keystrokes to a specified email address. The email credentials are provided by the user, and it requires enabling "less secure app access" on the email account for the SMTP connection. The tool is designed for ethical testing and research purposes, highlighting potential security risks associated with keystroke logging attacks.






![key-log](https://github.com/user-attachments/assets/a4b93a5a-66e2-48ec-9c09-3fe16d219205)






This keylogger, coded in Python, logs keystrokes and processes them into a human-readable format. It sends the captured data to a specified email address using SMTP, with email credentials provided by the user (requires "less secure app access"). The keylogger continues to run in the background even if the file is deleted from the system, and can only be stopped via Task Manager.

For delivery to a target, social engineering techniques such as disguising the file, zipping it multiple times to bypass antivirus detection, or using a USB drive can be employed to deploy the keylogger on a victim's machine.
