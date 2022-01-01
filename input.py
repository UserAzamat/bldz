from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.title='программа'


class Main(App):
	
	def __init__(self):
		super().__init__()
		self.btn = Button(text = 'pass',color = (0, 1, 0.7, 1))
		self.lab = Label(text = '- + - + - + - + - + - + - + - + -', color = (0, 1, 0.7, 1) )
		self.ti = TextInput(multiline = False, 
			padding = [105, 22,],
			password = False,
			cursor_color = [0, .1, 8, 1], 
			cursor_width = '3sp',
			font_size = '17sp',
			hint_text = '- + - + - + - + - + - + - + - + -  ',
			hint_text_color = [0, 1, 0.7, 1],
			foreground_color = (1, 0, 0, 1),
			on_text_validate = self.oll,
			text = '' )
		try:
			if v==0:
				pass
		except NameError:
			v=1

		if v==1:
			self.ti.focus=True
			v=0
	
	def oll(self, *arg):
		ff()
		o_f()

	def ff(self, *arg):
		
		if self.ti.text != '':
			self.btn.text = self.ti.text
			self.ti.text = ''
		else:
			self.btn.text = '- + - + - + - + - + - + - + - + -  '
	def o_f(self, *arg):
		self.ti.focus=True
		
		

		


	def build(self):


		layout = AnchorLayout(padding = [200])

		sub_layout = GridLayout(rows = 3, spacing = 3)

		
		
		sub_grid_layout = GridLayout(rows = 1, spacing = 2)
		sub_grid_layout.add_widget(self.lab)
		

		self.btn.bind(on_press = self.ff)
		self.btn.bind(on_release = self.o_f)


		
		sub_layout.add_widget(sub_grid_layout)
		sub_layout.add_widget( self.ti )
		sub_layout.add_widget( self.btn )
		
		
		layout.add_widget(sub_layout)

	

		
		return layout

	


if __name__ == "__main__":
	
    app = Main()
    app.run()