import os

def parse_telegram_messages_to_file()
	files = os.listdir('train')

	s = ''

	for file in files:
		with open('train/messages.html', 'r') as f:
			lines = f.readlines()

		from_name = 0
		text_flag = 0
		for line in lines:
			if text_flag:
				text = line.strip('\n')
				s += name + '---' + text + '\n'
				text_flag = 0

			if from_name:
				name = line.strip('\n')
				from_name = 0

			if '<div class="from_name">' in line:
				from_name = 1
			elif '<div class="text">' in line:
				text_flag = 1

	with open('messages.txt', 'w') as f:
		f.writelines(s)


def messages_file_to_pd_dataframe(name='messages.txt'):
	d = {'context2': [], 'context1': [], 'context0': [], 'message': []}
	


