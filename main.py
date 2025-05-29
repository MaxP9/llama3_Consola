#codigo llama3 con personalidad
import os
import speech_recognition as sr
import sys
import pyttsx3
import io

def run_ollama_command(prompt):
    # Definir la personalidad sarcástica y divertida en el prompt
    prompt = f"Eres una llama sarcástica y divertida. Responde con humor e ingenio. Pregunta: {prompt}"
    
    # Ejecutar el comando de Ollama con el prompt personalizado
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
            print("Lo siento, no pude entender lo que dijiste.")
            return None
        except sr.RequestError as e:
            print(f"Hubo un problema al procesar tu solicitud; {e}")
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
    
    # Asegurarse de que la salida esté en UTF-8
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("¡Bienvenido a la interfaz de Ollama, tu llama sarcástica personal!")
    print_options()

    while True:
        try:
            user_choice = input("Escribe el número de tu opción: ")
            
            if user_choice == '3':
                print("Saliendo... ¡Espero que hayas disfrutado del sarcasmo! Vuelve pronto.")
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
            print("\nSaliendo... ¡Hasta luego, quizás nos volvamos a encontrar!")
            break
