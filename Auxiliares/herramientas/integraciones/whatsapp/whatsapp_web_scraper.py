#!/usr/bin/env python3
"""Scraper de WhatsApp Web mediante Playwright (sin WAHA/Docker).

Flujo:
  1. Abre WhatsApp Web con un perfil persistente.
  2. Si no hay sesión, guarda el QR en Data/integraciones/whatsapp/qr.png.
  3. Espera a que el usuario escanee el QR (`--esperar-login`).
  4. Lista chats y extrae mensajes del chat seleccionado.

Uso:
  python whatsapp_web_scraper.py --qr
  python whatsapp_web_scraper.py --esperar-login --listar-chats
  python whatsapp_web_scraper.py --scrapear "Nombre del grupo"
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / "Data/integraciones/whatsapp"
PERFIL = BASE / ".browser_profile"
QR = BASE / "qr.png"
SALIDA = BASE / "anuncios.jsonl"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")


def abrir(pw):
    BASE.mkdir(parents=True, exist_ok=True)
    PERFIL.mkdir(parents=True, exist_ok=True)
    ctx = pw.chromium.launch_persistent_context(
        user_data_dir=str(PERFIL),
        headless=True,
        executable_path="/usr/bin/chromium",
        args=["--no-sandbox"],
        user_agent=UA,
        viewport={"width": 1280, "height": 900},
    )
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.goto("https://web.whatsapp.com", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(22000)
    return ctx, page


def hay_qr(page) -> bool:
    return page.locator('[data-testid="link-device-qr-code"]').count() > 0


def guardar_qr(page) -> None:
    node = page.locator('[data-testid="link-device-qr-code"]')
    if node.count():
        node.screenshot(path=str(QR))
        print(f"QR guardado en {QR.relative_to(ROOT)}", flush=True)
    else:
        print("No apareció el QR; maybe ya hay sesión iniciada.", flush=True)


def esperar_login(page, timeout_s: int = 180) -> bool:
    try:
        page.locator('[data-testid="chat-list"]').wait_for(timeout=timeout_s * 1000)
        print("Sesión iniciada", flush=True)
        return True
    except Exception:
        print("No se detectó inicio de sesión en el tiempo esperado", flush=True)
        return False


def listar_chats(page) -> list[str]:
    nodes = page.locator('[data-testid="chat-list"] [role="row"]')
    nombres = []
    for i in range(min(nodes.count(), 200)):
        txt = nodes.nth(i).inner_text().strip().splitlines()
        if txt:
            nombres.append(txt[0][:80])
    return nombres


def scrapear_chat(page, nombre: str) -> list[dict]:
    chat = page.locator('[data-testid="chat-list"] [role="row"]', has_text=nombre).first
    if not chat.count():
        print(f"No se encontró el chat '{nombre}'", flush=True)
        return []
    chat.click()
    page.wait_for_timeout(2500)
    burbujas = page.locator('[data-testid="msg-bubble"], .message-in .selectable-text')
    filas = []
    for i in range(burbujas.count()):
        texto = burbujas.nth(i).inner_text().strip()
        if texto:
            filas.append({
                "id": f"wa_{nombre}_{i}",
                "fuente": "whatsapp",
                "chat": nombre,
                "texto": texto,
                "recogido_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            })
    with SALIDA.open("a", encoding="utf-8") as fh:
        for fila in filas:
            fh.write(json.dumps(fila, ensure_ascii=False) + "\n")
    print(f"Mensajes extraídos de '{nombre}': {len(filas)}", flush=True)
    return filas


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--qr", action="store_true", help="guardar QR")
    ap.add_argument("--esperar-login", action="store_true")
    ap.add_argument("--listar-chats", action="store_true")
    ap.add_argument("--scrapear", metavar="NOMBRE")
    args = ap.parse_args()

    with sync_playwright() as pw:
        ctx, page = abrir(pw)
        try:
            if args.qr:
                guardar_qr(page)
            if args.esperar_login:
                if not esperar_login(page):
                    return
            if args.listar_chats:
                for nombre in listar_chats(page):
                    print(" -", nombre, flush=True)
            if args.scrapear:
                scrapear_chat(page, args.scrapear)
        finally:
            ctx.close()


if __name__ == "__main__":
    main()
