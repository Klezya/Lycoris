# Ubuntu Security Helper

> Herramienta CLI para simplificar la gestión de seguridad en servidores basados en Debian/Ubuntu.
> Reemplaza el stack fragmentado de herramientas (fail2ban, UFW manual, lynis, chkrootkit, etc.) con una única solución integrada, amigable y guiada.

---

## Información General

| Campo | Valor |
|---|---|
| Proyecto | Ubuntu Security Helper |
| Nombre Oficial | Pendiente |
| Fecha de Inicio | 01 de Abril de 2026 |
| Desarrolladores | Benjamín Nuñez, Vicente Estay |
| Lenguaje | Python 3.10+ |
| Plataforma Objetivo | Debian, Ubuntu 20.04+, distros basadas en Debian |
| Distribución | Paquete `.deb` via GitHub Releases |
| Estado | En desarrollo — v1 MVP |

---

## Propuesta de Valor

El problema que resuelve: asegurar un servidor Ubuntu hoy implica instalar y configurar múltiples herramientas por separado, cada una con su propia sintaxis y curva de aprendizaje.

**Ubuntu Security Helper reemplaza:**

| Herramienta típica | Módulo equivalente |
|---|---|
| UFW / iptables manual | `network` |
| fail2ban | `monitor` |
| lynis / chkrootkit | `audit` |
| adduser + visudo manual | `users` |
| Scripts bash personalizados | `templates` |

**Principios de diseño:**
- Una sola herramienta, instalada localmente en el servidor a proteger
- Más simple y accesible que un SIEM o SOAR tradicional
- Lenguaje claro, sin requerir conocimientos avanzados de seguridad
- Sin múltiples dependencias: todo en un solo comando

---

## Usuarios Objetivo

- Desarrolladores con servidor propio (VPS, homelab) sin perfil de sysadmin
- Sysadmins junior que necesitan una base de seguridad sólida rápidamente
- Equipos pequeños sin presupuesto para soluciones enterprise
- Estudiantes y profesionales con infraestructura propia

---

## Módulos del Sistema

### `users` — Gestión de Usuarios

Administrar cuentas del servidor y sus permisos.

**Funcionalidades:**
- Crear, eliminar y modificar cuentas de usuario
- Asignar y revocar permisos sudo
- Gestionar grupos y membresías
- Listar el estado actual de todas las cuentas y permisos
- Detectar cuentas inactivas o con configuraciones inseguras

---

### `network` — Seguridad de Red

Analizar y configurar el firewall de forma guiada.

**Funcionalidades:**
- Configurar reglas de firewall (UFW) de forma guiada
- Habilitar o deshabilitar puertos específicos con descripción del servicio asociado
- Mostrar resumen de servicios expuestos y su justificación
- Sugerir configuraciones base según el tipo de servidor (web, base de datos, SSH only)

---

### `templates` — Plantillas de Configuración

Exportar e importar configuraciones de seguridad reutilizables.

**Funcionalidades:**
- Exportar la configuración de seguridad actual como archivo de plantilla
- Importar y aplicar plantillas en nuevos servidores con un solo comando
- Plantillas predefinidas para casos de uso comunes (servidor web, SSH only, etc.)
- Versionar y comparar plantillas

---

### `audit` — Auditoría de Aplicaciones

Escanear aplicaciones instaladas en búsqueda de vulnerabilidades conocidas.

**Funcionalidades:**
- Escanear paquetes y aplicaciones instaladas
- Detectar versiones desactualizadas con vulnerabilidades conocidas
- Consultar base de datos CVE (NVD API) para reportar severidad y descripción
- Generar reporte de auditoría exportable

---

### `monitor` — Monitor de Conexiones

Detectar conexiones sospechosas y reaccionar automáticamente.

**Funcionalidades:**
- Escanear conexiones activas en la red del servidor
- Detectar IPs sospechosas o no reconocidas
- Bloquear IPs automáticamente ante comportamiento anómalo (equivalente a fail2ban)
- Generar alertas configurables (log local)

---

## Alcance

### v1 — MVP (Alcance Actual)

| Funcionalidad | Estado |
|---|---|
| Gestión de usuarios y permisos | ✅ Incluido |
| Configuración de firewall (UFW) | ✅ Incluido |
| Gestión de puertos y servicios expuestos | ✅ Incluido |
| Plantillas de exportación/importación | ✅ Incluido |
| Auditoría de paquetes con CVE | ✅ Incluido |
| Detección de conexiones sospechosas | ✅ Incluido |
| Bloqueo automático de IPs | ✅ Incluido |
| Alertas por log local | ✅ Incluido |
| Análisis de tráfico a nivel de paquetes | 🔜 Roadmap v2 |
| Hardening de aplicaciones específicas (nginx, mysql) | 🔜 Roadmap v2 |
| Alertas por email | 🔜 Roadmap v2 |
| Dashboard web multi-servidor | 🔜 Roadmap v3 |
| Reemplazo de antivirus | ❌ Fuera de alcance |
| Gestión de certificados SSL/TLS | ❌ Fuera de alcance |
| Análisis de tráfico profundo (SIEM/SOAR) | ❌ Fuera de alcance |

---

## Stack Técnico

| Componente | Decisión |
|---|---|
| Lenguaje | Python 3.10+ |
| Framework CLI | Typer (recomendado) |
| Fuente de CVEs | NVD API (National Vulnerability Database) |
| Firewall | UFW (Uncomplicated Firewall) |
| Testing | pytest |
| Linting | ruff |
| CI/CD | GitHub Actions |
| Distribución | Paquete `.deb` via GitHub Releases |
| Versionado | Semver con git tags (v1.0.0) |
| Gestión de tareas | GitHub Projects |

---

## Estructura del Repositorio

```
ubuntu-security-helper/
├── ush/                          # Código fuente principal
│   ├── __init__.py
│   ├── cli.py                    # Entry point del CLI
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── users.py              # Módulo gestión de usuarios
│   │   ├── network.py            # Módulo seguridad de red
│   │   ├── templates.py          # Módulo plantillas
│   │   ├── audit.py              # Módulo auditoría CVE
│   │   └── monitor.py            # Módulo monitor de conexiones
│   └── utils/
│       ├── __init__.py
│       ├── cve.py                # Cliente NVD API
│       └── system.py             # Helpers del sistema (permisos, OS, etc.)
├── debian/                       # Empaquetado .deb
│   ├── control                   # Metadatos del paquete
│   ├── postinst                  # Script post-instalación
│   └── prerm                     # Script pre-desinstalación
├── tests/
│   ├── test_users.py
│   ├── test_network.py
│   ├── test_audit.py
│   └── test_monitor.py
├── docs/
│   └── UBUNTU_SECURITY_HELPER.md
├── .github/
│   └── workflows/
│       └── build.yml             # CI/CD: tests + build .deb en cada release
├── pyproject.toml                # Configuración del proyecto y dependencias
└── README.md
```

---

## Modelo de Distribución

El software se instala directamente en el servidor a proteger. No existe servidor central de gestión en v1.

**Mecanismo:** Paquete `.deb` publicado en GitHub Releases.

```bash
# Instalación
apt install ./ubuntu-security-helper.deb
# o
dpkg -i ubuntu-security-helper.deb
```

El comando queda disponible globalmente en `/usr/bin/` para todos los usuarios del sistema.

**Roadmap de distribución:**
- v1: GitHub Releases (`.deb` manual)
- v2+: PPA de Ubuntu o repositorio APT propio

---

## Roadmap

| Versión | Contenido |
|---|---|
| **v1 — MVP** | Módulos core: `users`, `network`, `templates`, `audit` (CVE), `monitor` básico |
| **v2 — Expansión** | Análisis de tráfico, hardening de apps específicas, alertas email, mejoras monitor |
| **v3 — Plataforma** | Dashboard web para gestión de múltiples servidores |

---

## Decisiones Pendientes

- [ ] Nombre oficial del proyecto y comando CLI (ej: `ush`, `sechelper`, otro)
- [ ] Framework CLI final (Typer recomendado, alternativas: Click, argparse)
- [ ] Formato de reportes exportados (JSON, HTML, PDF)
- [ ] Branching strategy del repositorio (trunk-based, gitflow, etc.)
- [ ] Configuración de GitHub Projects (milestones, etiquetas, etc.)
