import time, os, pygame
def establecer_alarma():
    hora_alarma = input("Formato de hora: HH:MM (24 horas) \n Ingresa la hora de la alarma: ")
    try:
        hora, minuto = map(int, hora_alarma.split(":"))
        if 0 <= hora < 24 and 0 <= minuto < 60: return hora, minuto
        else: print("Hora no válida. Intenta de nuevo."); return establecer_alarma()
    except ValueError:
        print("Formato incorrecto. Intenta de nuevo."); return establecer_alarma()
def reproducir_audio(audio_path):
    if os.path.exists(audio_path):
        pygame.mixer.init(); pygame.mixer.music.load(audio_path); pygame.mixer.music.play()
        print("Presiona Ctrl+C para detener la alarma.")
        while pygame.mixer.music.get_busy(): time.sleep(1)
    else: print(f"Archivo de audio no encontrado: {audio_path}")
def main():
    print("¡Bienvenido a la alarma en Python!")
    hora, minuto = establecer_alarma()
    print(f"Alarma configurada para las {hora:02d}:{minuto:02d}.")
    while True:
        ahora = time.localtime()
        if ahora.tm_hour == hora and ahora.tm_min == minuto:
            (print("¡Es hora! Reproduciendo alarma..."), reproducir_audio("alarma.mp3"))
            break
        time.sleep(30)
main()