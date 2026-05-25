"""
Nombre del Alumno: [Tu Nombre Completo]
Matrícula: [Tu Matrícula]
Fecha: [Fecha de entrega]
Examen Segundo Parcial - Programación Estructurada
"""
# ==========================================
# 1. IMPORTACIÓN DE BIBLIOTECAS ESTÁNDAR
# ==========================================
import datetime
import math
import random
import statistics
import sys
# ==========================================
# 2. DEFINICIÓN DE CONSTANTES
# ==========================================
MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO = 0.95
# ==========================================
# 3. FUNCIONES DEFINIDAS POR EL USUARIO
# ==========================================
def obtener_info_sistema():
    """
    Usa la biblioteca 'sys' para validar el entorno de ejecución.
    Requisitos: Realizar 3 llamadas distintas a la biblioteca 'sys'.
    """
    print("\n=== INFORMACIÓN DEL SISTEMA ===")
    plataforma = sys.platform
    version_python = sys.version
    executable = sys.executable
    print(f"Plataforma: {plataforma}")
    print(f"Versión de Python: {version_python}")
    print(f"Ejecutable: {executable}")

    if not version_python.startswith("3."):
        print("Error: Este programa requiere Python 3.x.")
        return False
    else:
        print("Entorno de ejecución válido.")
        return True



def simular_metricas_entrenamiento(cantidad_epochs):
 """
 Usa las bibliotecas 'random' y 'datetime' para simular los datos de entrenamiento.
 Requisitos: 3 llamadas a 'random' y 3 llamadas a 'datetime'.
 """
    inicio_real = datetime.datetime.now()
    formato = inicio_real.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n=== SIMULANDO ENTRENAMIENTO ===")
    
    lista_loss = []
    lista_latencia = []

    if cantidad_epochs <= 0:
        print("Error: La cantidad de epochs debe ser un número positivo.")
        return [], []

    print(" Entrenando modelo...")
    for epoch in range(1, cantidad_epochs + 1):
        # Simular pérdida (loss) y latencia
        loss = random.uniform(0.1, 1.2) 
        lista_loss.append(loss)

        prob_exito = random.random()

        eventos = ["Epoch exitoso", "Gradiente insetable", "Actualización de pesos"]
        evento_actual = random.choice(eventos)

        latencia_simulada = loss * 50
        print(f"  [Epoch {epoch}/{cantidad_epochs}] Loss: {loss_actual:.4f} | Prob. Éxito: {prob_exito:.2f} | Log: {evento_actual}")

        if loss_actual > UMBRAL_ERROR_CRITICO:
            print(f"\n[CRÍTICO] Se ha superado el Umbral de Error Crítico ({UMBRAL_ERROR_CRITICO}).")
            print("Ejecutando salida limpia de emergencia del sistema...")
            sys.exit(0)

    fin_real = inicio_real + datetime.timedelta(seconds=cantidad_epochs * 2)
    duracion = fin_real - inicio_real
    print(f"\nDuración total del entrenamiento: {duracion}")
    return lista_loss, lista_latencia, duracion.total_seconds()

def analizar_rendimiento(lista_loss):
 """
 Usa la biblioteca 'statistics' para analizar el comportamiento del entrenamiento.
 Requisitos: 3 llamadas distintas a la biblioteca 'statistics'.
 """
    # TODO: Implementar lógica
    return {}
def calcular_rmse(predicciones, reales):
 """
 Usa la biblioteca 'math' para calcular el Root Mean Squared Error (RMSE).
 Requisitos: 3 llamadas distintas a la biblioteca 'math'.
 """
    # TODO: Implementar lógica
    return 0.0
# ==========================================
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA)
# ==========================================
if __name__ == "__main__":
    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")
    # TODO: Invocar las funciones, orquestar el flujo y mostrar reportes ordenados.