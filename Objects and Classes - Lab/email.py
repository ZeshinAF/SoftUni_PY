class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


line = input()
emails = []
while line != 'Stop':
    parm = line.split(' ')
    s, r, c = parm[0], parm[1], parm[2]
    emails.append(Email(s, r, c))
    line = input()
indices = input().split(', ')
for i in indices:
    emails[int(i)].send()
for i in emails:
    print(i.get_info())
