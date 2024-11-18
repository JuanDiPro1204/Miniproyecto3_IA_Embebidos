import numpy as np
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
from gpiozero import AngularServo
import time

# Configuración de GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Pines para actuadores
BUZZER_PIN = 17
RELAY_PIN_7 = 19
RELAY_PIN_8 = 26
SERVO_PIN = 18

# Configurar pines como salida
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(RELAY_PIN_7, GPIO.OUT)
GPIO.setup(RELAY_PIN_8, GPIO.OUT)

# Inicializar los relés en "apagado" (HIGH, por lógica inversa)
GPIO.output(RELAY_PIN_7, GPIO.HIGH)
GPIO.output(RELAY_PIN_8, GPIO.HIGH)

# Configuración del servomotor
servo = AngularServo(SERVO_PIN, min_pulse_width=0.0006, max_pulse_width=0.0023)

# Cargar el modelo de TensorFlow Lite
interpreter = tf.lite.Interpreter(model_path='/home/juandipro/Desktop/Miniproyecto3/miniproyecto3_model.tflite')
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Inicializar cámara
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")

# Clases del modelo
class_names = ['bacteria', 'fungus', 'healthy']

def activate_buzzer(duration=5):
    """Función para activar el buzzer por un tiempo prolongado."""
    for _ in range(duration * 2):
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(0.5)

def activate_servo(duration=10):
    """Función para mover el servomotor por un tiempo prolongado."""

    end_time = time.time() + duration
    while time.time() < end_time:
        servo.angle = 90
        time.sleep(1)
        servo.angle = 0
        time.sleep(1)
        servo.angle = -90
        time.sleep(1)

def close_camera():
    """Cierra la cámara y libera los recursos."""
    cam.release()
    cv2.destroyAllWindows()

while True:
    # Captura de imagen en tiempo real
    ret, frame = cam.read()
    if not ret:
        print("Error al capturar el fotograma")
        break
    cv2.imshow("test", frame)

    # Espera a la tecla para capturar o cerrar
    k = cv2.waitKey(1)
    if k % 256 == 27:  # Tecla ESC para salir y cerrar cámara
        print("Escape presionado, cerrando...")
        close_camera()
        GPIO.cleanup()
        break
    elif k % 256 == 32:  # Tecla SPACE para capturar imagen y clasificar
        img_name = "opencv_frame_0.png"
        cv2.imwrite(img_name, frame)
        print(f"Imagen {img_name} guardada!")

        # Preprocesar imagen
        img = cv2.imread(img_name)
        img_resized = cv2.resize(img, (128, 128))
        img_resized = np.reshape(img_resized, [1, 128, 128, 3]) / 255.0
        test_imgs_numpy = np.array(img_resized, dtype=np.float32)

        # Realizar la predicción
        interpreter.allocate_tensors()
        interpreter.set_tensor(input_details[0]['index'], test_imgs_numpy)
        interpreter.invoke()
        predictions = interpreter.get_tensor(output_details[0]['index'])
       
        # Obtener clase predicha
        prediction_class = np.argmax(predictions, axis=1)[0]
        prediccion = class_names[prediction_class]
        print(f"Predicción: {prediccion}")

        # Activar actuadores según predicción
        if prediccion == "bacteria":
            GPIO.output(RELAY_PIN_7, GPIO.LOW)  # Activa el relé 7 de inmediato
            GPIO.output(RELAY_PIN_8, GPIO.HIGH) # Apaga el relé 8 si estaba encendido
            # Ejecuta el buzzer sin apagar el relé 7
            activate_buzzer(duration=5)

        elif prediccion == "fungus":
            GPIO.output(RELAY_PIN_7, GPIO.LOW)  # Activa el relé 7 de inmediato
            GPIO.output(RELAY_PIN_8, GPIO.HIGH) # Apaga el relé 8 si estaba encendido
            # Ejecuta el servomotor sin apagar el relé 7
            activate_servo(duration=10)

        elif prediccion == "healthy":
            GPIO.output(RELAY_PIN_7, GPIO.HIGH)  # Apaga el relé 7 si estaba encendido
            GPIO.output(RELAY_PIN_8, GPIO.LOW)   # Activa el relé 8 de inmediato para la clase healthy
            # Mantiene el relé 8 activado hasta la siguiente clasificación

        # Mostrar la imagen con la predicción
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plt.title(prediccion)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()

# Cierra recursos GPIO en caso de terminar el script
GPIO.cleanup()
