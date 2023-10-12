import pywhatkit

nums = ['+919400642679', '+916381952489', '+919895614598', '+919526556575', '+919567779341']
msg = '''Heyy! This is Adithya from ACM.
Please use the following link to join the SIG AI WhatsApp group.
https://chat.whatsapp.com/G9PEp3cS2sN1BUc7foQBKr'''

for num in nums:
    pywhatkit.sendwhatmsg_instantly(num, msg)