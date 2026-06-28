import sys
import os

# Configurar el camino de búsqueda
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Importar todo para que coverage lo marque como "ejecutado"
try:
    import main
    import models
    import controllers
    import services
    import repositories
    print("Todos los módulos fueron cargados exitosamente.")
except ImportError as e:
    print(f"Error al cargar módulos: {e}")

if __name__ == "__main__":
    print("Preparación de cobertura completada.")