# hacknet-credential-extractor
Script de Python para extraer credenciales del desafío Hacknet HTB .

# Hacknet Credential Extractor

Script en Python para extraer credenciales del desafío Hacknet (HTB) explotando una condición de carrera en el sistema de likes.

## Descripción

Este script automatiza la extracción de credenciales aprovechando una vulnerabilidad de race condition en la funcionalidad de likes de la plataforma Hacknet HTB.

## Requisitos

- Python 3.x
- requests

## Instalación
```bash
pip install requests
```

## Uso

1. Actualiza las cookies en el script:
```python
MIS_COOKIES = {
    'csrftoken': 'tu_csrf_token',
    'sessionid': 'tu_session_id'
}
```

2. Ejecuta el script:
```bash
python3 hacknet_extractor.py
```

## Características

- ✅ Extracción automática de 30 IDs
- ✅ Sistema de reintentos con race condition
- ✅ Filtrado de credenciales duplicadas
- ✅ Formato de salida usuario:contraseña

## Advertencia

⚠️ Este script es solo para propósitos educativos y uso en entornos autorizados como HackTheBox. No uses este código en sistemas sin autorización explícita.

## Licencia

MIT License
