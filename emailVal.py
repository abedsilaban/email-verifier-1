# # from validate_email import validate_email

# # from tqdm import tqdm
# # # DNS.defaults['server']=['8.8.8.8', '8.8.4.4']

# # if validate_email('varmaashik@gmail.com'):
# # 	print("Email is Valid")
# # else:
# # 	print("Invalid Email")
# # is_valid = validate_email('varmaashik@gmail.com',check_mx=True)

# # if is_valid==True:
# # 	print("Email has SMTP Server")
# # else:
# # 	print("SMTP not found")
# # if validate_email('varmaashik@gmail.com',verify=True):
# # 	print("Email is Verified")
# # else:
# # 	print("Email not verified")
# import csv
# from emailverifier import Client
# from emailverifier import exceptions

# client = Client('at_9mJPBZyFvOEyDhVwv2tD2xYh7Qoh5')

# try:


# 	data = client.get("varmaashik@gmail.com")
# except exceptions.HttpException:
# # If you get here, it means service returned HTTP error code
# 	pass
# except exceptions.GeneralException:
# # If you get here, it means you cannot connect to the service
# 	pass
# except exceptions.UndefinedVariableException:
# # If you get here, it means you forgot to specify the API key
# 	pass
# except exceptions.InvalidArgumentException:
# # If you get here, it means you specified invalid argument
# # (options should be a dictionary)
# 	pass
# except:
# 	pass
# # Something else happened related. Maybe you hit CTRL-C
# # while the program was running, the kernel is killing your process, or
# # something else all together.

# print(data)

# # Use data.json_string to get raw data in JSON.
# # You can access any response field as a class property
# # by converting field name from "camelCase" to "snake_case"
# print("Email address: " + data.email_address)
# print("Format: " + str(data.format_check))
# print("DNS: " + str(data.dns_check))
# print("SMTP: " + str(data.smtp_check))
# print("Catch all: " + str(data.catch_all_check))
# print("Disposable: " + str(data.disposable_check))
# print("Free: " + str(data.free_check))
# print("Last audit date: " + str(data.audit.audit_updated_date))

import dns.resolver

records = dns.resolver.query('emailhippo.com', 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)

import socket
import smtplib

# Get local server hostname
host = socket.gethostname()

# SMTP lib setup (use debug level for full output)
server = smtplib.SMTP()
server.set_debuglevel(0)

# SMTP Conversation
server.connect(mxRecord)
server.helo(host)
server.mail('varmaashik@gmail.com.com')
code, message = server.rcpt(str('varmaashik@gmail.com'))
server.quit()

# Assume 250 as Success
if code == 250:
	print('Success')
else:
	print('Bad')