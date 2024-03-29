import smtplib
import ssl
from email.message import EmailMessage

subject = "Hello There I'm just an ordinary guy "
sender_email = "vaibhav007mahesh@gmail.com"
receiver_email = "abhibizman@gmail.com"
body =" " " Dear [] \n I Vaibhav Maheshwari, am writing to express my strong interest in Data Analyst Position at your company. I'm confident my skills and experience in Data Analyst would be a valuable asset to your team.I've been following Coforge’s work for providing services with latest technologies to the client. In my previous role at [Previous Company], I successfully [mention a relevant accomplishment that showcases your skills], which [demonstrate the impact of your accomplishment]. I'm confident I can replicate and expand upon this success at [Company Name] by [briefly explain how you could contribute]." " "


password = input("Enter ur password")

message = EmailMessage()
message["from"]=sender_email
message["To"]= receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html,subtype="html")

context = ssl.create_default_context()

print("Sending Email to " + receiver_email)


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())


print("Successful done")
