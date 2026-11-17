#!/usr/bin/env python3
"""Generate self-contained profile SVGs with Python 3 (standard library only)."""
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
BG, PANEL, BORDER = "#11111b", "#181825", "#313244"
TEXT, MUTED = "#cdd6f4", "#a6adc8"
PURPLE, CYAN, GREEN, PEACH = "#cba6f7", "#89dceb", "#a6e3a1", "#fab387"
FONT = "'DejaVu Sans Mono', 'Liberation Mono', monospace"


def text(x, y, value, fill=TEXT, size=14, extra=""):
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" '
            f'{extra}>{escape(value)}</text>')


def frame(height, title, description):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" '
            f'viewBox="0 0 1000 {height}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>',
            '<defs><linearGradient id="spectrum" x1="0" y1="0" x2="1" y2="0">'
            f'<stop stop-color="{PURPLE}"/><stop offset=".5" stop-color="{CYAN}"/>'
            f'<stop offset="1" stop-color="{GREEN}"/></linearGradient></defs>',
            f'<rect x="1" y="1" width="998" height="{height-2}" rx="14" fill="{BG}" stroke="{BORDER}"/>',
            f'<path d="M15 1 H985 Q999 1 999 15 V45 H1 V15 Q1 1 15 1" fill="{PANEL}"/>',
            f'<path d="M1 45 H999" stroke="{BORDER}"/>',
            '<circle cx="23" cy="23" r="5" fill="#f38ba8"/>'
            '<circle cx="42" cy="23" r="5" fill="#f9e2af"/>'
            f'<circle cx="61" cy="23" r="5" fill="{GREEN}"/>',
            f'<g font-family="{FONT}">', text(88, 28, title, MUTED, 12)]


def save(name, parts):
    (ASSETS / name).write_text("\n".join(parts + ["</g></svg>" ]) + "\n", encoding="utf-8")


def prompt(command, y=80):
    return [text(28, y, "rodolfo@arch", GREEN), text(139, y, "~", PURPLE),
            text(158, y, "❯", CYAN), text(180, y, command)]


def palette(x, y):
    colors = ["#f38ba8", PEACH, "#f9e2af", GREEN, CYAN, "#89b4fa", PURPLE, "#f5c2e7"]
    return [f'<rect x="{x+i*26}" y="{y}" width="26" height="15" fill="{color}"/>'
            for i, color in enumerate(colors)]


def header():
    p = frame(386, "~/rodolfo-collado  —  profile.sh", "Rodolfo Ramírez Collado. Estudiante de Ingeniería de Sistemas en UAM. Backend, bases de datos y Linux. Managua, Nicaragua.")
    p += prompt("./profile.sh --intro")
    glyphs = {
        "R": ["██████╗ ","██╔══██╗","██║  ██║","██████╔╝","██╔══██╗","██║  ██║","╚═╝  ╚═╝"],
        "O": [" ██████╗ ","██╔═══██╗","██║   ██║","██║   ██║","██║   ██║","╚██████╔╝"," ╚═════╝ "],
        "D": ["██████╗ ","██╔══██╗","██║  ██║","██║  ██║","██║  ██║","██████╔╝","╚═════╝ "],
        "L": ["██╗     ","██║     ","██║     ","██║     ","██║     ","███████╗","╚══════╝"],
        "F": ["███████╗","██╔════╝","██║     ","█████╗  ","██╔══╝  ","██║     ","╚═╝     "]}
    for row in range(7):
        line = " ".join(glyphs[ch][row] for ch in "RODOLFO")
        p.append(text(28, 123 + row*20, line, "url(#spectrum)", 19,
                      'xml:space="preserve"'))
    p += [text(30, 280, "RAMÍREZ COLLADO", TEXT, 21, 'letter-spacing="7"'),
          text(30, 312, "Backend · Bases de datos · Linux", MUTED, 16),
          f'<path d="M28 331 H972" stroke="{BORDER}"/>',
          text(30, 361, "ING. DE SISTEMAS / UAM", CYAN, 12),
          text(400, 361, "MANAGUA, NICARAGUA", GREEN, 12),
          text(771, 361, "ES / EN B2", PURPLE, 12)]
    save("terminal-header.svg", p)


def stack():
    p = frame(370, "~/toolbox  —  stack --list", "Tecnologías: Java, Spring Boot, Python, Kotlin; SQL, PostgreSQL, SQL Server; Linux, Arch Linux, Docker, Git, GitHub y Markdown. Sin porcentajes de dominio.")
    p += prompt("stack --list --no-percentages")
    groups = [
        (28, "01 / DESARROLLO", PURPLE, ["Java", "Spring Boot", "Python", "Kotlin", "POO"]),
        (351, "02 / DATOS", CYAN, ["SQL", "PostgreSQL", "Microsoft SQL Server"]),
        (674, "03 / SISTEMAS", GREEN, ["Linux / Arch Linux", "Docker", "Git / GitHub", "Markdown"]),
    ]
    for x, label, color, entries in groups:
        p += [f'<rect x="{x}" y="107" width="298" height="200" rx="8" fill="{PANEL}" stroke="{BORDER}"/>',
              text(x+15, 134, label, color, 13),
              f'<path d="M{x+15} 147 H{x+283}" stroke="{BORDER}"/>']
        for i, entry in enumerate(entries):
            p += [text(x+16, 174+i*26, "[+]", color, 13), text(x+53, 174+i*26, entry, TEXT, 14)]
    p += [text(28, 342, "EDITOR", MUTED, 11),
          text(95, 342, "IntelliJ IDEA · DataGrip · PyCharm · VS Code", TEXT, 13)]
    save("terminal-stack.svg", p)


def inside_ring(x, y, ring):
    inside = False
    for a, b in zip(ring, ring[1:] + ring[:1]):
        if (a[1] > y) != (b[1] > y) and x < (b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]:
            inside = not inside
    return inside


def inside_geometry(x, y, geometry):
    polygons = geometry["coordinates"] if geometry["type"] == "MultiPolygon" else [geometry["coordinates"]]
    return any(inside_ring(x, y, polygon[0]) and not any(inside_ring(x, y, hole) for hole in polygon[1:])
               for polygon in polygons)


def location():
    p = frame(432, "~/home  —  whereami --ascii", "Mapa ASCII de Centroamérica, con Nicaragua resaltada. Ubicación: Managua, Nicaragua. Zona horaria America/Managua (UTC−06:00). Siluetas simplificadas de Natural Earth.")
    p += prompt("whereami --ascii --region central-america")
    features = json.loads((ASSETS / "data/central-america.geojson").read_text())["features"]
    # Equirectangular sampling: each character is one geographic sample.
    west, east, south, north = -98, -76, 6, 23
    cols, rows, dx, dy, left, top = 60, 26, 8.0, 10.3, 28, 111
    for row in range(rows):
        lat = north - (row+.5)*(north-south)/rows
        for col in range(cols):
            lon = west + (col+.5)*(east-west)/cols
            country = next((f["properties"]["name"] for f in features if inside_geometry(lon, lat, f["geometry"])), None)
            if country:
                p.append(text(left+col*dx, top+row*dy, "#" if country == "Nicaragua" else ":",
                              GREEN if country == "Nicaragua" else "#6c7086", 12))
    # Marker uses Nicaragua's centroid, not a claimed street or live location.
    mx = left + (-85.2-west)/(east-west)*cols*dx
    my = top + (north-12.9)/(north-south)*rows*dy - 2
    p += [f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="5" fill="{GREEN}" stroke="{BG}" stroke-width="2"/>',
          f'<path d="M{mx+8:.1f} {my:.1f} h37 l15 -21 h63" fill="none" stroke="{GREEN}"/>',
          text(round(mx+65), round(my-28), "NICARAGUA", GREEN, 11),
          text(28, 398, ": tierra", MUTED, 11), text(150, 398, "# Nicaragua", GREEN, 11),
          text(310, 398, "N ↑  /  ASCII MAP", MUTED, 11),
          f'<path d="M541 111 V366" stroke="{BORDER}"/>',
          text(573, 138, "rodolfo@nicaragua", PURPLE, 18),
          text(573, 163, "────────────────────────────", MUTED, 13)]
    for i, (label, value) in enumerate([
        ("Location", "Managua, Nicaragua"),
        ("Timezone", "UTC−06:00"),
        ("Education", "Ing. de Sistemas · UAM"),
        ("Focus", "Backend / SQL / Linux"),
        ("Languages", "Español · English B2"),
    ]):
        p += [text(573, 195+i*28, label, CYAN, 13), text(675, 195+i*28, value, TEXT, 13)]
    p += palette(573, 345)
    save("terminal-location.svg", p)


if __name__ == "__main__":
    header()
    stack()
    location()
    print("Generated 3 profile SVGs in assets/")
