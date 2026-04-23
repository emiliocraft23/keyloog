#Poryecto de Keyboard 
Un codigo malicioso para saber que esta escribiendo el usuario

## Requisitos

- **Python 3.10+** (Recomendado)
- La librería de Python `keyboard`.
- **Privilegios de Administrador:** En sistemas Windows (y root en Linux), la librería `keyboard` requiere permisos de administrador para poder interceptar los eventos globales de teclado a nivel del sistema operativo.

## Instalación

1. Clona o descarga el repositorio en tu máquina.
2. Abre una terminal y navega hasta el directorio del proyecto.
3. Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

## Ejecución

Para iniciar el keylogger, debes abrir una terminal o consola de comandos **como Administrador** y ejecutar el siguiente comando:

```bash
python main.py
```

### Ejemplo de Ejecución y Uso

1. Al iniciar el programa, verás el siguiente mensaje en la consola:
   ```text
   ========================================
      KEYLOGGER EDUCATIVO INICIADO
   ========================================
   Todas las pulsaciones se guardarán en: C:\Users\...\keylog.txt
   Presiona la tecla 'ESC' en cualquier momento para detener.
   ========================================

   Escuchando eventos de teclado...
   ```
2. Mientras el programa se está ejecutando, minimiza la consola y escribe texto en un bloc de notas, en tu navegador o en cualquier otra aplicación. (Por ejemplo: escribe "Hola mundo" usando la tecla mayúscula para la H).
3. Cuando desees detener la captura de teclas, presiona la tecla `ESC`. Verás el mensaje de finalización en la consola.
4. Abre el archivo `keylog.txt` que se ha generado en la misma carpeta. El contenido registrado se verá similar a esto:
   ```text
   [shift]Hola mundo
   [enter]
   Prueba de [backspace][backspace]keylogger
   ```

## Análisis Educativo
Una vez concluida la ejecución, revisa el archivo `keylog.txt`. Esto ilustra de manera práctica cómo información sensible (contraseñas, correos, conversaciones) puede ser fácilmente interceptada en un entorno donde un atacante ha logrado ejecutar software malicioso, demostrando la importancia de usar antivirus y no descargar software de fuentes no confiables.
