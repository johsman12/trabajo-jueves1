# Reto integrador: Simulador de inscripciones de un curso
class Curso:
    def __init__(self):
        self.estudiantes = []
        
    def inscribir(self, nombre, edad):
        # Solo permite inscribir a mayores de 15 años
        if edad > 15:
            self.estudiantes.append({"nombre": nombre, "edad": edad})
            print(f"Éxito: {nombre} ha sido inscrito.")
        else:
            print(f"Rechazado: {nombre} no cumple con la edad mínima (> 15).")
            
    def listar_mayores_edad(self):
        # Usa list comprehension para filtrar estudiantes mayores de 18 años
        return [e["nombre"] for e in self.estudiantes if e["edad"] > 18]

# --- Probando el Reto Integrador ---
curso_python = Curso()
curso_python.inscribir("Carlos", 14)  # No se inscribe
curso_python.inscribir("Ana", 17)     # Se inscribe
curso_python.inscribir("Mateo", 20)   # Se inscribe

print("Estudiantes mayores de edad (> 18):", curso_python.listar_mayores_edad())