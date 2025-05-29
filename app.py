#codigo llama3 simple
import os
import speech_recognition as sr
import sys
import pyttsx3
import io

def run_ollama_command(prompt):
    command = f'ollama run llama3 "{prompt}"'
    result = os.popen(command).read().strip()
    
    try:
        result = result.encode('latin1').decode('utf-8')  
    except Exception as e:
        print(f"Error de codificación: {e}")
        return  

    print(f"Resultado: {result}")
    speak_result(result)

def listen_to_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di tu pregunta...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='es-ES')
            return text
        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
            return None
        except sr.RequestError as e:
            print(f"Error al solicitar resultados; {e}")
            return None

def speak_result(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def print_options():
    print("\nElige una opción:")
    print("1. Escribir una pregunta.")
    print("2. Grabar una pregunta.")
    print("3. Salir.")

if __name__ == "__main__":
    
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("Bienvenido a la interfaz de Ollama.")
    print_options()

    while True:
        try:
            user_choice = input("Escribe el número de tu opción: ")
            
            if user_choice == '3':
                print("Saliendo...")
                break
            elif user_choice == '1':
                user_input = input("Escribe tu pregunta: ")
                run_ollama_command(user_input)
                print_options() 
            elif user_choice == '2':
                audio_question = listen_to_audio()
                if audio_question:
                    print(f"Pregunta reconocida: {audio_question}")
                    run_ollama_command(audio_question)
                print_options()  
            else:
                print("Opción no válida. Por favor, elige 1, 2 o 3.")
        except KeyboardInterrupt:
            print("\nSaliendo...")
            break
