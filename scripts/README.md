# Generar la terminal del perfil

Desde la raíz del repositorio:

```bash
python3 scripts/generate_assets.py
```

Requiere Python 3, `rsvg-convert` y DejaVu Sans Mono en la máquina que genera el archivo. En Arch Linux, los paquetes son `librsvg` y `ttf-dejavu`; en Debian/Ubuntu, `librsvg2-bin` y `fonts-dejavu-core`. No requiere paquetes de Python.

Los textos, tamaños, colores y secciones se editan en `generate_assets.py`. El generador convierte las letras y los símbolos en trazados vectoriales antes de guardar `assets/terminal-profile.svg`. El archivo publicado ya no depende de las fuentes instaladas ni de las restricciones de fuentes de la vista previa de VS Code o del navegador.

El SVG conserva título y descripción accesibles; el README conserva el texto alternativo y los enlaces. Sube el SVG regenerado junto con los cambios del generador.
