from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout 
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2


class CameraApp(MDApp):
	def build(self):
		layout = MDBoxLayout(orientation='vertical')
		self.image = Image()
		layout.add_widget(self.image)
		layout.add_widget(MDRaisedButton(text="CATTURA", pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(None, None)))

		self.cap = cv2.VideoCapture(0)
		Clock.schedule_interval(self.video_loader, 1.0/30.0)


		return layout



	def video_loader(self, *args):
		ret, frame = self.cap.read()
		self.frame_image = frame	#rendo il frame un attributo della classe
		buffer = cv2.flip(frame, 0).tostring()
		texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
		texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
		self.image.texture = texture



# main
if __name__ == '__main__':
	CameraApp().run()