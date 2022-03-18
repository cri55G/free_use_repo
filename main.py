from kivy.app import App
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2


class CameraApp(App):
	def build(self):
		self.window = GridLayout()
		self.window.cols = 1

		self.image = Image()
		self.image.size_hint = (1, 1)
		self.window.add_widget(self.image)

		self.cap = cv2.VideoCapture(0)
		Clock.schedule_interval(self.video_loader, 1.0/30.0)

		self.window.size_hint = (0.9, 0.9)
		self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

		#button widget		
		self.button = Button(text="Cattura immagine", size_hint=(1, 0.5), bold=True, background_color="#00FFCE")
		self.window.add_widget(self.button)

		self.button2 = Button(text="Filtro 1", size_hint=(1, 0.5), pos_hint=(.3, .3), background_color="#00FFCE")
		self.window.add_widget(self.button2)


		return self.window



	def video_loader(self, *args):
		_, frame = self.cap.read()
		self.frame = frame	#rendo il frame un attributo della classe
		buffer = cv2.flip(frame, 0).tostring()
		texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt="bgr")
		texture.blit_buffer(buffer, colorfmt="bgr", bufferfmt="ubyte")
		self.image.texture = texture





# main
if __name__ == "__main__":
	CameraApp().run()
