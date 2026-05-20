<p align="center">
  <img src="ipl_logo.png" alt="Logo IPL" width="150"/>
</p>

Instituto Profesional de Líderes (IPL)
Licenciatura en Inteligencia Artificial y Ciencia de Datos  

Proyecto Académico:   
Smart-Gate: Control de Acceso Biométrico con IA y Persistencia de Datos

Autor  
Nombre: Alvaro Moreno  
Licenciatura en Inteligencia Artificial y Ciencia de Datos  
Módulo: Programación Orientada a Objetos y Visión Artificial  

Profesor  
Profesor: Raúl Figuera  
 Institución: Instituto Profesional de Líderes (IPL)  


31 de mayo de 2026  
Panamá, Panamá  


PROYECTO INTEGRADOR APLICATIVO DE INTERVENCIÓN

1. TÍTULO DEL PROYECTO
Smart-Gate: Control de Acceso Biométrico con IA y Persistencia de Datos

2. CONTEXTUALIZACIÓN DEL PROBLEMA O NECESIDAD
El crecimiento de la inseguridad en entornos corporativos y residenciales ha evidenciado las limitaciones de los sistemas de acceso tradicionales (tarjetas magnéticas o códigos numéricos), los cuales son susceptibles de robo o duplicación. Smart-Gate surge como una respuesta tecnológica que utiliza la biometría facial para garantizar que la identidad del usuario sea única e intransferible.
El Smart-Gate: Es un sistema de seguridad inteligente que procesa video en tiempo real.  
Propuesta de Valor: Integra IA para decisiones autónomas y persistencia de datos para auditorias forenses inmediatas.  
Modelado: Arquitectura orientada a objetos (POO) que vincula visión artificial con SQL.  

3. JUSTIFICACIÓN
Optimiza la gestión de accesos, elimina errores humanos y garantiza trazabilidad mediante IA y SQL.  

4. OBJETIVO GENERAL DE INTERVENCIÓN
Desarrollar Smart-Gate integrando algoritmos de reconocimiento facial (Haar Cascades y LBPH) y gestión de datos en SQL para un control de acceso seguro y auditable.  

5. PREGUNTAS ORIENTADORAS
¿Cómo optimizar el control de acceso? Ajustando el confidence score.  
¿Qué métodos de seguridad se aplicarán? Encriptación, login administrativo y captura automática de intrusos.  
¿Qué desafíos surgen? Latencia en escritura de BD y variabilidad de iluminación.  



6. MARCO REFERENCIAL
Reconocimiento facial con Haar Cascades y LBPH. Persistencia con SQL para almacenar eventos con timestamp.  

7. METODOLOGÍA DE TRABAJO
1.	   Investigación de parámetros y diseño de BD.  
2.	   Desarrollo CRUD para usuarios y registros.  
3.	   Seguridad con lógica de cooldown y protocolo de intrusos.  
4.	   Pruebas de estrés y métricas de precisión.  

8. PROPUESTA APLICATIVA O SOLUCIÓN

 8.1 Arquitectura Técnica
a.	- Lenguaje: Python 3.x  
b.	- Librerías: OpenCV, SQLite3/MySQL, Tkinter  
c.	- Algoritmos: Haar Cascades y LBPH  

8.2 Modelo Entidad-Relación (DER)

Figura 1: Modelo Entidad-Relacion simplificado de Smart-Gate.
8.3 Diagrama de Clases UML

Figura 2: Diagrama UML simplificado del sistema Smart-Gate.
Ejemplos CRUD
•	- Create: Registro de rostros en .yml y BD.  
•	- Read: Consulta de logs filtrados por fecha.  

  9. CARACTERISTICAS PRINCIPALES
•	- Reconocimiento facial en tiempo real con LBPH.  
•	- Registro de accesos autorizados en SQLite.  
•	- Captura y almacenamiento de intentos de intrusión.  
•	- Botón visual “Salir” y tecla q para detener la cámara.  
•	- Scripts auxiliares: captura, renombrado, limpieza, mejora, verificación y entrenamiento.  

10. TECNOLOGIAS UTILIZADAS
•	- Python 3.11+  
•	- OpenCV  
•	- SQLite3  
•	- NumPy  
•	- Pillow  
•	- Logging  

11. INSTALACION
git clone https://github.com/pitsburg8280-cmyk/SmartGate-AI-FacialAccess.git
cd SmartGate
pip install opencv-python pillow numpy
Opcional: Instala DB Browser for SQLite para revisar registros.  

12. ESTRUCTURA DEL PROYECTO
SmartGate/
│
├── dataset/                # Imágenes capturadas de usuarios
├── dataset_enhanced/       # Imágenes mejoradas para entrenamiento
├── intrusos/               # Fotos de intentos de acceso no autorizados
│
├── smart_gate.py           # Sistema principal con reconocimiento facial y BD
├── capture_dataset.py      # Script para capturar imágenes desde la cámara
├── train_model.py          # Entrenamiento del modelo LBPH
├── rename_dataset.py       # Renombrado automático de imágenes
├── clean_dataset.py        # Limpieza de duplicados y corruptos
├── enhance_images.py       # Mejora de calidad de imágenes
├── verificar_dataset.py    # Verificación de IDs e imágenes
│
├── trainer.yml             # Modelo entrenado LBPH
├── smart_gate.db           # Base de datos SQLite
├── smart_gate.log          # Archivo de logs del sistema
│
├── config.json             # Configuración del sistema
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto

13. USO DEL SISTEMA
      1. Capturar dataset  
          python capture_dataset.pY
      2. Renombrar dataset viejo  
          python rename_dataset.py
      3. Limpiar dataset  
          python clean_dataset.py
     4. Mejorar imágenes  
          python enhance_images.py
     5. Verificar dataset  
          python verificar_dataset.py
      6. Entrenar modelo LBPH  
          python train_model.py
      7. Ejecutar SmartGate  
          python smart_gate.py
     
14. BASE DE DATOS
•	- usuarios → ID, nombre, rostro_id.  
•	- registros_acceso → accesos autorizados con fecha/hora.  
•	- intrusos → intentos de acceso no reconocidos con foto.  

15. LOGS
Archivo smart_gate.log registra: conexión a BD, carga de modelo, accesos, intrusos y errores.

16. Conclusión Final
El proyecto Smart-Gate representa un avance significativo en la aplicación práctica de la Inteligencia Artificial y la Programación Orientada a Objetos. La integración de algoritmos de visión artificial con un sistema de persistencia de datos en SQLite demuestra cómo la teoría puede transformarse en soluciones concretas para problemas reales de seguridad y control de acceso.  
Durante el desarrollo se enfrentaron retos técnicos como la gestión de datasets, el entrenamiento de modelos LBPH y la implementación de protocolos de detección de intrusos. Superar estos desafíos permitió consolidar competencias en Python, OpenCV y diseño de arquitecturas modulares, fortaleciendo la capacidad de crear proyectos reproducibles y escalables.  
En conclusión, Smart-Gate no solo cumple con los objetivos académicos del módulo, sino que también aporta un marco sólido para futuras investigaciones y aplicaciones en entornos corporativos y residenciales. Este trabajo refleja el compromiso con la excelencia técnica y la presentación profesional, consolidando la formación en Inteligencia Artificial y Ciencia de Datos.

17. REFERENCIAS BIBLIOGRÁFICAS (APA 7.ª)
•	- Bradski, G., & Kaehler, A. (2017). Learning OpenCV 3: Computer Vision in C++ with the OpenCV Library. O’Reilly Media.  
•	- Nixon, M., & Aguado, A. (2019). Feature Extraction and Image Processing for Computer Vision (4th ed.). Academic Press.  
•	- Sarkar, A., & Pandey, S. (2020). Introduction to Face Recognition and Its Applications in Security. CRC Press.  
•	- Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020). Database System Concepts (7th ed.). McGraw-Hill Education.  

18. LICENCIA
Este proyecto está bajo la licencia [MIT](LICENSE).
Esto significa que puedes usar, copiar, modificar y distribuir el código con libertad, siempre y cuando se incluya la nota de copyright original y la licencia MIT en cualquier copia o derivado del software.

17. REPOSITORIO EN GitHub
El código fuente completo esta disponible en: https://github.com/pitsburg8280-cmyk/SmartGate-AI-FacialAccess
