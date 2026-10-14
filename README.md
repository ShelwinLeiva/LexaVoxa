# LexaVoxa - Aplicativo Web de Aprendizaje de Idiomas y Analítica de Datos

Integrantes del Equipo
* Luis Fernando Davila Ramirez
* Shelwin Giovanny Leiva Longa
* Diego Martínez Guevara

## Descripción del Problema
Actualmente, el aprendizaje del idioma inglés presenta diversas dificultades para estudiantes y personas que desean desarrollar sus competencias lingüísticas. Una de las principales problemáticas está relacionada con la falta de constancia y motivación durante el proceso de aprendizaje, especialmente cuando los métodos utilizados resultan repetitivos, poco interactivos o no se adaptan al ritmo y las necesidades de cada persona. Esto puede ocasionar que los estudiantes pierdan el interés con facilidad y abandonen sus procesos de formación antes de alcanzar los resultados esperados.

A esta situación se suma la dificultad para realizar un seguimiento adecuado del progreso en el aprendizaje. En algunos casos, los estudiantes no cuentan con mecanismos claros que les permitan identificar sus avances, reconocer sus fortalezas y conocer los aspectos en los que necesitan mejorar. La ausencia de una retroalimentación constante y de objetivos que permitan medir el progreso puede generar una percepción de estancamiento y disminuir la motivación para continuar estudiando.

Como consecuencia, muchas personas presentan dificultades para mantener un proceso de aprendizaje continuo y desarrollar de manera progresiva habilidades relacionadas con el idioma inglés, lo que limita sus oportunidades académicas, laborales y personales. Ante esta problemática, el desarrollo de LexaVoxa se plantea como una alternativa tecnológica que incorpora un componente analítico de Minería de Datos para predecir y hacer un seguimiento oportuno del rendimiento del estudiante.

## Objetivos del Proyecto

### Objetivo General
Desarrollar un aplicativo web para el aprendizaje de idiomas que contribuya a mejorar la motivación, la constancia y el seguimiento del progreso de los estudiantes durante su proceso de formación.

### Objetivos Específicos
* Analizar los requerimientos funcionales y no funcionales de los problemas actuales en el ámbito del aprendizaje de idiomas para diseñar un aplicativo que permita aprender de manera fácil, intuitiva y que brinde la motivación que el usuario necesita.
* Diseñar la arquitectura del software que permita gestionar eficientemente los usuarios activos en la plataforma, cursos, lecciones y contenidos para que estos usuarios puedan acceder fácilmente a ellos y aprender de los mismos.
* Codificar las funcionalidades del aplicativo en Spring Boot, asegurando la integración de módulos para el acceso a cursos, lecciones, test, ranking y logros si el usuario desea y que estos se muestren correctamente.
* Verificar (Testear) por medio de pruebas exhaustivas del aplicativo para asegurar que cumple con los requisitos funcionales y técnicos, incluyendo pruebas de rendimiento, seguridad y verificación de acceso a los cursos correctos dependiendo de su rango y que las lecciones estén acorde al idioma que se está aprendiendo.
* Implementar un aplicativo web que permita resolver problemas en el aprendizaje de idiomas como falta de motivación, simplicidad de las aplicaciones existentes y exceso de funciones de pago que limiten el aprendizaje del usuario.

## Tecnologías Utilizadas
* Backend: Java con el framework Spring Boot
* Frontend: HTML, CSS, JavaScript y Bootstrap
* Base de Datos: MongoDB
* Herramienta de Análisis: MinedApp (Guía práctica de Minería de Datos I)

## Fuente de los Datos (Minería de Datos)
* Dataset utilizado: Student Performance Dataset (student-por.csv)
* Fuente: UCI Machine Learning Repository
* Enlace de origen: https://archive.ics.uci.edu/dataset/320/student+performance
* Tipo de Tarea: Regresión (Predicción de la calificación final G3)
* Modelo implementado: Árbol de Decisión para Regresión (Decision Tree Regressor)

## Estructura del Repositorio
* Anexos/: Evidencias e historiales de usuario del proyecto.
* Diagramas/: Arquitectura del sistema y diagramas lógicos.
* Innovación y Emprendimiento/: Documentación del modelo de negocio del aplicativo.
* Minería de Datos/: Scripts, análisis exploratorio y reportes generados.
* Código.zip: Paquete con el código fuente integral del software.
* Informe metodológico LexaVoxa.docx: Documento metodológico oficial del proyecto.

## Cómo Acceder y Ejecutar
1. Clonar el repositorio actual.
2. Descomprimir el archivo Código.zip para revisar la implementación en Spring Boot y el frontend web.
3. Consultar la carpeta Minería de Datos/ para verificar los experimentos predictivos y estadísticos realizados con MinedApp.
4. Revisar el archivo Informe metodológico LexaVoxa.docx para el detalle completo del proceso de investigación y modelado.
