import smtplib

# Set up the sender, receiver, and email content
sender = "chess2k23@gmail.com"
password = "fqiu bxhn cifd wvcl"
receiver = "04.tushar.mishra@gmail.com"

# Create the email message
message = f"Subject: {'Testing'}\n\n{'kya re chor'}"

# Set up the SMTP server and send the email
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.sendmail(from_addr=sender, to_addrs=receiver, msg=message)

print("Email sent successfully!")