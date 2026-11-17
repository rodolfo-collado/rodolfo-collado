# Publicar y personalizar el perfil

## Publicación

GitHub muestra el README del perfil cuando existe un repositorio **público** llamado exactamente **rodolfo-collado**, con `README.md` en su raíz. Referencia: [documentación de GitHub](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme).

1. Crea `rodolfo-collado/rodolfo-collado` en GitHub como repositorio público y vacío, sin generar README ni licencia.
2. Desde esta carpeta, revisa `git status` y sube los archivos:

   ```bash
   git add README.md assets scripts docs .gitignore .gitattributes
   git commit -m "Add terminal-style GitHub profile"
   git remote add origin https://github.com/rodolfo-collado/rodolfo-collado.git
   git push -u origin main
   ```

   Si ya existe un remoto `origin`, compruébalo con `git remote -v` y omite `git remote add` si apunta al repositorio correcto. Si el remoto ya tiene commits, integra su historial antes de subir: no uses `--force`.

3. Abre tu perfil y comprueba las tres imágenes, los enlaces y los desplegables.

Los archivos ya están preparados. No se ha creado un commit ni se ha publicado desde esta tarea.

## Diseño y edición

- `README.md`: presentación, proyectos, certificados, logros y enlaces.
- `scripts/generate_assets.py`: textos, colores y ASCII de los tres paneles.
- `assets/terminal-*.svg`: imágenes listas para GitHub, sin dependencias remotas, fuentes descargables, JavaScript ni servicios de estadísticas.
- `assets/data/central-america.geojson`: geometría para el mapa ASCII, con fuente y atribución en la misma carpeta.

Regenera las imágenes con Python 3, sin instalar paquetes:

```bash
python3 scripts/generate_assets.py
```

Sube también los SVG regenerados. No hace falta GitHub Actions ni configurar secretos. El README usa Markdown y HTML sencillo; los gradientes están dentro de los SVG porque GitHub limita estilos y scripts en el README. Los paneles se ajustan al ancho disponible; en móvil su texto se reduce. La introducción y los proyectos son texto nativo, y el stack tiene una alternativa desplegable en texto.

Abre `README.md` en la vista previa Markdown de tu editor. Para inspeccionar un panel, abre su SVG en un navegador. Los paneles mantienen su propio fondo oscuro también con el tema claro de GitHub.

## Recomendaciones para tu perfil

1. **Fija Arch Linux y PyGebra en los primeros lugares.** Arch muestra Linux y documentación; PyGebra añade algoritmos, una aplicación utilizable, pruebas y distribución. Ambos tienen más contexto para un visitante que un repositorio de ejercicios sin explicación.
2. **Dale evidencia al enfoque backend.** Un siguiente proyecto podría ser una API con Spring Boot, PostgreSQL y Docker, con instrucciones reproducibles, ejemplos de peticiones y pruebas de los casos importantes. Es una propuesta futura, no una capacidad de un repositorio actual.
3. **Prepara CashFlow antes de destacarlo.** La página consultada no mostraba README ni descripción. Añade objetivo, capturas, instalación y qué implementaste. No lo presenté como una API o como proyecto Spring Boot porque no había evidencia suficiente.
4. **Conserva el logro de Java.** El segundo lugar y la fecha concreta aportan más información que una barra de dominio o una lista extensa de badges.
5. **Mantén las certificaciones verificables.** Los enlaces de Credly vienen del PDF; los títulos se conservan tal como aparecen. Los cursos introductorios de IA no se presentan como experiencia profesional en machine learning.
6. **Prepara una versión pública de tu CV antes de añadir un botón de descarga.** El PDF recibido incluye teléfono. Aquí solo se publica el correo profesional, la ciudad y los datos académicos pertinentes.
7. **Opcional: añade un README en inglés.** Tu B2 permite presentar el mismo trabajo a una audiencia más amplia. Conviene mantener ambas versiones sincronizadas.

Bio sugerida para el campo de GitHub:

> Estudiante de Ingeniería de Sistemas @ UAM | Java · Spring Boot · Python · SQL | Linux / Arch | Managua, Nicaragua

## Fuentes utilizadas

- CV y certificados proporcionados por ti. El PDF original no se copia al repositorio.
- [Perfil público](https://github.com/rodolfo-collado).
- [Arch Linux Installation Guide](https://github.com/rodolfo-collado/arch-linux-installation-guide).
- [PyGebra / Algebra-Lineal](https://github.com/rodolfo-collado/Algebra-Lineal).
- [CashFlow](https://github.com/rodolfo-collado/CashFlow).

Consulta de repositorios: 17 de noviembre de 2026. Algunas páginas pueden proceder de la caché del proveedor; revisa su estado actual antes de ampliar las descripciones.
