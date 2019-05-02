template = """<html>
				<head>
					<link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet"> 
					<style>
						body{
							font-family: 'Poppins', sans-serif;
						}

						[STYLE]

					</style>
				</head>
				<body>

					[CONTENT]

				</body>
			</html>"""

class textviz():
	def __init__(self, viz_type='block',attn_color='red'):
		# viz_type block | attn
		# attn_color red | green | blue
		self.template = template
		self.viz_type = viz_type
		self.attn_color = attn_color
		self.markers = {'none':'none'}
		self.texts = []
		self.labels = []
		self.non_label_texts = []

	def add_marker(self, name, color):
		# color string eg. red, blue, #df536c
		# name string
		self.markers[name] = color

	def add_text(self, text, labels, non_label_text=None, attn=False):
		# text list (list sentence -> words seperated by space)
		# labels list (list of list names for each sentence | list of attention weights) 
		# attn bool 

		assert len(text) == len(labels)

		def sep(sent):
			return sent.split(' ')

		self.texts += list(map(sep,text))
		self.labels += labels
		if non_label_text is None:
			non_label_text = ['']*len(text)
		self.non_label_texts += non_label_text

	def gen_viz(self, fname=None):
		# fname to save html viz else None will return html
		self.create_style()
		html_content = ''
		for i in range(len(self.texts)):
			html_content += '<b> Sample : '+str(i+1)+' </b><br>'
			for j in range(len(self.texts[i])):
				word = self.texts[i][j]
				label = self.labels[i][j]

				if label not in self.markers and self.viz_type=='block':
					print('label',label,'not in markers.')

				if word.strip()[:2] == '</':
					word = '['+word[2:-1].upper()+']'
				if word.strip()[0] == '<' and word.strip()[-1] == '>':
					word = '['+word[1:-1].upper()+']'

				if label == 'none':
					html_content += word+' '
				else:
					if self.viz_type == 'block':
						html_content += '<span class='+label+'> '+word+' </span> '
					else:
						color = hex(int(255 - float(label) * 255))[-2:]
						if self.attn_color == 'red':
							color = '#ff'+color+color
						elif self.attn_color == 'green':
							color = '#'+color+'ff'+color
						elif self.attn_color == 'blue':
							color = '#'+color+color+'ff'

						html_content += '<span style="background-color:'+color+';"> '+word+' </span> '

			html_content += '<br>'
			if self.non_label_texts[i] != '':
				html_content += self.non_label_texts[i].replace('\n','<br>')
			html_content += '<br><br>'

		self.template = self.template.replace('[CONTENT]',html_content)

		if fname is not None:
			f = open(fname, 'w')
			f.write(self.template)
			f.close()
		else:
			return html_content

	def create_style(self):
		if len(self.markers) == 0:
			print('please add markers first.') 
		style = ''
		for m in self.markers:
			style += '.'+m+'{ background-color : '+ self.markers[m] +';}\n'
		self.template = self.template.replace('[STYLE]',style)






