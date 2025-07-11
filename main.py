from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from datetime import date

class JobAppForm(BoxLayout):
    def generate_letter(self):
        recipient = self.ids.recipient.text
        company = self.ids.company.text
        position = self.ids.position.text
        skills = self.ids.skills.text

        letter = f"""
Dear {recipient},

I am writing to express my interest in the {position} position at {company}.
With my background in {skills}, I believe I can add value to your team.

Sincerely,
Sibusiso Kenneth
kenneth12.sk@gmail.com | 072 560 6940
        """.strip()

        self.ids.output.text = letter

class JobAppAssistant(App):
    def build(self):
        return JobAppForm()

if __name__ == "__main__":
    JobAppAssistant().run()