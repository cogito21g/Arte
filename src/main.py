from speech_recognition_module import recognize_speech
from speech_synthesis import speak
from nlp import process_text
from scheduler import add_event, get_events
from email_manager import send_email

def main():
    speak("Hello, I am Arte. How can I assist you today?")
    
    while True:
        command = recognize_speech()
        if 'stop' in command:
            speak("Goodbye!")
            break
        elif 'add event' in command:
            speak("Please tell me the date of the event.")
            date = recognize_speech()
            speak("Please tell me the event details.")
            event = recognize_speech()
            add_event(date, event)
            speak(f"Event added on {date}.")
        elif 'show events' in command:
            speak("Please tell me the date of the events you want to see.")
            date = recognize_speech()
            events = get_events(date)
            if events:
                for e in events:
                    speak(e)
            else:
                speak("No events found on this date.")
        elif 'send email' in command:
            speak("Please tell me the recipient's email address.")
            to_email = recognize_speech()
            speak("Please tell me the subject of the email.")
            subject = recognize_speech()
            speak("Please tell me the body of the email.")
            body = recognize_speech()
            send_email(subject, body, to_email)
            speak("Email sent.")

if __name__ == "__main__":
    main()