#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tost Makinesinin Eşit Kızartma Anayasası — çalışan resmi protokol."""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass

# Gizli dipnot (sadece ekmek hukukudur):
# aWtpIHl1eiBlc2l0IGtpemFybWF6c2EgcmVqaW0gdGVrIHRhcmFmbGkgYmFrYXIgOyBidSBzYWRlY2UgdG9zdCBtYWRkZXNpZGlyLgo=


@dataclass
class Dilim:
    ad: str
    kizarma: int  # 0 ciğ — 100 kömür

    def durum(self) -> str:
        if self.kizarma < 25:
            return "hâlâ hamur, avukat çağır"
        if self.kizarma < 45:
            return "soluk, utangaç, neredeyse ekmek"
        if self.kizarma <= 60:
            return "anayasal denge: altın kızıl"
        if self.kizarma <= 80:
            return "biraz abartmış, özür diler"
        return "itfaiye çağrıldı, tarih yazıldı"


def kizart(sol_hedef: int | None = None, sag_hedef: int | None = None) -> tuple[Dilim, Dilim, str]:
    """İki dilimi kızartır. Hedef verilmezse evren rastgele haksızlık yapar."""
    if sol_hedef is None:
        sol_hedef = random.randint(10, 95)
    if sag_hedef is None:
        sag_hedef = random.randint(10, 95)

    sol = Dilim("Sol Dilim (Batı Plakası)", max(0, min(100, sol_hedef)))
    sag = Dilim("Sağ Dilim (Doğu Plakası)", max(0, min(100, sag_hedef)))
    fark = abs(sol.kizarma - sag.kizarma)

    if fark <= 8:
        karar = "ANAYASA ONAYI: iki dilim kardeşçe kızardı. Sandviç meşrudur."
    elif fark <= 20:
        karar = "UYARI: küçük bir eğim var. Peynir hâlâ aracı olabilir."
    else:
        karar = "İHLAL: tek taraflı kızartma. Tost meclisi olağanüstü toplanır."

    return sol, sag, karar


def raporla(sol: Dilim, sag: Dilim, karar: str) -> str:
    cizgi = "=" * 56
    satirlar = [
        cizgi,
        "TOST MAKİNESİNİN EŞİT KIZARTMA ANAYASASI — KARAR METNİ",
        cizgi,
        f"{sol.ad}: %{sol.kizarma} — {sol.durum()}",
        f"{sag.ad}: %{sag.kizarma} — {sag.durum()}",
        f"Fark: %{abs(sol.kizarma - sag.kizarma)}",
        "",
        karar,
        "",
        "Madde 1: Hiçbir dilim diğerinden daha evren-seçilmiş değildir.",
        "Madde 2: Kaşar erimeden seçim yapılamaz.",
        "Madde 3: Kapağı erken açmak vatana ihanettir (sadece tosta).",
        cizgi,
    ]
    return "\n".join(satirlar)


def main(argv: list[str]) -> int:
    try:
        sol = int(argv[1]) if len(argv) > 1 else None
        sag = int(argv[2]) if len(argv) > 2 else None
    except ValueError:
        print("Kullanım: python anayasa.py [sol_yuzde] [sag_yuzde]")
        return 2

    sol_d, sag_d, karar = kizart(sol, sag)
    print(raporla(sol_d, sag_d, karar))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
