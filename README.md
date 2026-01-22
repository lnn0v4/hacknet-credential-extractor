# hacknet-credential-extractor

Script en Python para extraer credenciales del desafío Hacknet (HTB) explotando una condición de carrera en el sistema de likes.

## Descripción

Este script automatiza la extracción de credenciales aprovechando una vulnerabilidad de race condition en la funcionalidad de likes de la plataforma Hacknet HTB.
# 🎥 Video demostración

[![Hacknet Credential Extractor - HTB](https://img.youtube.com/vi/37Zr8ApyuFc/0.jpg)](https://youtu.be/37Zr8ApyuFc)

En este video se documenta **el desarrollo paso a paso** de un script en Python utilizado durante la resolución de la máquina **HackNet [Medium]** de Hack The Box.
El enfoque del video está en la **lógica del código**, las **técnicas empleadas** y cómo el script permite la **extracción de credenciales** dentro de un entorno controlado.
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
