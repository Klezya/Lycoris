# Lycoris

> CLI para simplificar la gestión de seguridad en servidores Debian/Ubuntu.

Reemplaza el stack fragmentado de herramientas (fail2ban, UFW manual, lynis, chkrootkit, etc.) con una única solución integrada, amigable y guiada.

## Instalación

```bash
pip install -e .
```

## Uso

```bash
lycoris --help
```

## Desarrollo

```bash
# Instalar dependencias de desarrollo
pip install -e .
pip install pytest ruff

# Correr tests
pytest

# Linter
ruff check .
```

## Módulos

| Módulo      | Descripción                              |
|-------------|------------------------------------------|
| `users`     | Gestión de usuarios, grupos y permisos   |
| `network`   | Configuración de firewall (UFW)          |
| `audit`     | Auditoría de paquetes y CVEs             |
| `monitor`   | Detección y bloqueo de IPs sospechosas   |
| `templates` | Exportación e importación de configuraciones |

## Licencia

Apache 2.0
