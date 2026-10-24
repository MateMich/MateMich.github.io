"""Generator stron: strona główna (index.html), strony projektów (<slug>.html)
i wersja dla rekrutera (portfolio/index.html).

Wszystkie treści są w listach poniżej. Po zmianie uruchom z katalogu repo:

    python tools/build.py

Skrypt tworzy też lekkie miniatury WebP w images/thumbs/.
"""

from html import escape
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://matemich.github.io"
EMAIL = "mateusz.michalik.poczta@gmail.com"
GITHUB = "https://github.com/MateMich"
YOUTUBE = "https://www.youtube.com/channel/UCTquNp9Y1NekVNhJ2daFtcA"

# ---------------------------------------------------------------------------
# Projekty z własną podstroną
# kind: play = gra w przeglądarce, store = Google Play, web = strona/aplikacja,
#       file = do pobrania
# ---------------------------------------------------------------------------

PROJECTS = [
    dict(
        slug="civduel",
        name="Civilization Duel",
        tagline="Karcianka strategiczna o władzę nad światem",
        section="graj",
        chip=("play", "Graj w przeglądarce"),
        cover="images/civduel/civduel1.png",
        gallery=["images/civduel/civduel1.png", "images/civduel/civduel2.png"],
        body=[
            "Gracze rywalizują o dominację nad światem: możesz wygrać, budując cuda, albo podbijając przeciwnika. "
            "Zagrasz online z innymi, przeciwko sztucznej inteligencji albo lokalnie jeden na jednego.",
        ],
        note="Projekt został zaprogramowany przy użyciu agentów AI (w tym z pomocą modeli Gemini 3 Flash oraz Pro).",
        actions=[("Zagraj na pełnym ekranie", "https://turn-card-civ.onrender.com/")],
        embed=dict(src="https://turn-card-civ.onrender.com/", style="tall"),
    ),
    dict(
        slug="zenithrush",
        name="Zenith Rush",
        tagline="Wyścigi na czas, ulepszenia i nowe auta do odblokowania",
        section="graj",
        chip=("play", "Graj w przeglądarce"),
        cover="images/zenithrush/zenith1.png",
        gallery=["images/zenithrush/zenith1.png", "images/zenithrush/zenith2.png"],
        body=[
            "Zbieraj ulepszenia w trakcie jazdy, żeby poprawić swój czas i odblokować nowe samochody oraz trasy. "
            "Za zdobyte pieniądze kupujesz kolejne auta i ulepszenia. Pobijaj swoje rekordy!",
        ],
        actions=[],
        embed=dict(
            src="https://html5.gamedistribution.com/953cf9c3407f4fda9407724436d00065/?gd_sdk_referrer_url=https://www.example.com/games/{game-path}",
            style="wide",
        ),
    ),
    dict(
        slug="carintime",
        name="Chrono Drive",
        tagline="Samochodówka, w której manipulujesz czasem",
        section="graj",
        chip=("play", "Graj w przeglądarce"),
        cover="images/carintime/carintime0.png",
        gallery=[f"images/carintime/carintime{i}.png" for i in range(5)],
        body=[
            "Twoim zadaniem jest dojechać do końca mapy, pokonując po drodze przeszkody. "
            "Inne pojazdy i bramy poruszają się razem z Tobą, a czasem reagują na Twój ruch inaczej, niż się spodziewasz. "
            "Nawet teren potrafi okazać się dodatkową przeszkodą.",
        ],
        actions=[("Chrono Drive na itch.io", "https://myteq.itch.io/chrono-drive")],
        video="https://www.youtube.com/embed/VVy5RCzSEcs",
        embed=dict(
            src="https://html5.gamedistribution.com/0d2264b08cac4c1684c98c9574d83bb2/?gd_sdk_referrer_url=https://www.example.com/games/{game-path}",
            style="wide",
        ),
        itch=("https://itch.io/embed/2521919", "https://myteq.itch.io/chrono-drive", "Chrono Drive by myteq"),
    ),
    dict(
        slug="spaceshift",
        name="SpaceShift",
        tagline="Leć jak najdalej przez kolejne strefy galaktyki",
        section="graj",
        chip=("play", "Graj w przeglądarce"),
        cover="images/spaceshift/spaceshift0.png",
        gallery=[f"images/spaceshift/spaceshift{i}.png" for i in range(5)],
        body=[
            "Celem jest polecieć jak najdalej. Sterujesz prędkością statku, a później także nadlatującymi przeszkodami. "
            "Po drodze trafiasz do różnych stref, które mają własne przeszkody i wygląd.",
        ],
        actions=[],
        embed=dict(
            src="https://html5.gamedistribution.com/25a9cabb062640209571dd2b13948ee1/?gd_sdk_referrer_url=https://www.example.com/games/{game-path}",
            style="wide",
        ),
    ),
    dict(
        slug="rebounce",
        name="ReBounce",
        tagline="Odbijaj piłkę od platform tak długo, jak dasz radę",
        section="telefon",
        chip=("look", "Archiwum"),
        archived=True,
        cover="images/rebounce/rebounce0.png",
        gallery=[f"images/rebounce/rebounce{i}.png" for i in range(4)],
        body=[
            "Prosta gra zręcznościowa: odbijasz piłkę od pojawiających się platform. "
            "Z czasem rozgrywka przyspiesza, a za zdobyte punkty odblokowujesz nowe piłki.",
        ],
        actions=[("Stary link do Google Play", "https://play.google.com/store/apps/details?id=com.Mateq.Rebounce2&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1")],
    ),
    dict(
        slug="komuwinien",
        name="Komu Winien?",
        tagline="Apka, która pilnuje, kto komu ile jest winien",
        section="telefon",
        chip=("look", "Archiwum"),
        archived=True,
        cover="images/komuwinien/komuwinien0.png",
        portrait=True,
        gallery=[f"images/komuwinien/komuwinien{i}.png" for i in range(5)],
        body=[
            "Prosta aplikacja do kontrolowania długów wobec znajomych. "
            "Możesz ustawić każdej osobie awatar, przejrzeć historię i sprawdzić całkowity bilans.",
        ],
        actions=[("Stary link do Google Play", "https://play.google.com/store/apps/details?id=com.Mateq.KomuWinien&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1")],
    ),
    dict(
        slug="janusz",
        name="Janusz: Misja Passat",
        tagline="Uzbieraj 200 cebulionów na Passata w 30 dni",
        section="telefon",
        chip=("look", "itch.io"),
        cover="images/janusz/janusz1.jpg",
        portrait=True,
        gallery=[f"images/janusz/janusz{i}.jpg" for i in range(1, 5)],
        body=[
            "Sąsiad kupił sobie nowego Passata, a Twoja godność Janusza nie pozwoli Ci żyć ze świadomością, że somsiad ma lepiej. "
            "Postanawiasz w ciągu 30 dni uzbierać 200 cebulionów na własnego Passata, nie tracąc przy tym całej godności.",
        ],
        note="Gra stworzona razem z Barteboj.",
        actions=[("Janusz na itch.io", "https://onebytestudio.itch.io/janusz-misja-passat")],
        itch=("https://itch.io/embed/2351328", "https://onebytestudio.itch.io/janusz-misja-passat", "Janusz Misja Passat by OneByteStudio"),
    ),
    dict(
        slug="ilenetto",
        name="IleNetto",
        tagline="Kalkulator wynagrodzeń: UoP, B2B, ZUS i podatki",
        section="web",
        chip=("web", "Otwórz"),
        cover="images/ilenetto/ilenetto1.png",
        gallery=[f"images/ilenetto/ilenetto{i}.png" for i in range(1, 4)],
        body=[
            "Aplikacja webowa do szybkiego i dokładnego liczenia podatków, składek ZUS i wynagrodzeń "
            "w różnych formach zatrudnienia, m.in. na umowie o pracę i na B2B.",
        ],
        actions=[("Otwórz IleNetto.pl", "https://ilenetto.pl/")],
        embed=dict(src="https://ilenetto.pl/", style="tall", title="Sprawdź od razu"),
    ),
    dict(
        slug="uczenie",
        name="Uczenie parkowania",
        tagline="Sieci neuronowe uczą się parkować: GA kontra PPO",
        section="lab",
        chip=("file", "Do pobrania"),
        cover="images/uczenie/uczenie0.png",
        gallery=[f"images/uczenie/uczenie{i}.png" for i in range(6)],
        body=[
            "Efekt mojej pracy magisterskiej. Porównałem dwa algorytmy uczenia sieci neuronowych, które miały nauczyć samochód jeździć i parkować w środowisku 3D: "
            "algorytm genetyczny (GA) i optymalizację polityki proksymalnej (PPO).",
            "Oba uczyły się na jednej mapie, a porównałem je na trzech. Przy przyjętych założeniach zdecydowanie lepiej sprawdził się GA. "
            "Możesz pobrać aplikację i zobaczyć to porównanie na własne oczy.",
        ],
        actions=[("Pobierz aplikację (ZIP, 32 MB)", "/showcasebuild.zip")],
    ),
    # Projekt zawodowy z własną podstroną (sekcja "pro" nie pojawia się w kafelkach na stronie głównej)
    dict(
        slug="inteligentny-dom",
        name="Inteligentny dom",
        tagline="Przewodowy inteligentny dom DIY sterowany przez Domoticza",
        section="pro",
        chip=("look", "Projekt zawodowy"),
        cover="images/domoticz/schemat.png",
        gallery=["images/domoticz/blockly.png"],
        credits=[("Zrzut ekranu Domoticza: PeterRozenveld, Wikimedia Commons, CC BY-SA 4.0",
                  "https://commons.wikimedia.org/wiki/File:Domoticz_Event_AllesOn_-2018-6-5_Domoticz.png")],
        body=[
            "Inteligentny dom, który zamiast urządzeń na Wi-Fi stoi na kablu. Centralą jest Raspberry Pi z Domoticzem, "
            "a moduły na Arduino rozmawiają z nią przez sieć MySensors po magistrali RS485. "
            "Całość spina bramka Ethernet montowana na szynie DIN, z zabezpieczeniami ESD i szerokim zakresem napięć zasilania.",
            "Projekt zaczął się jako domowe DIY, które – jak przyznaje jego autor – szybko wymknęło się spod kontroli: "
            "Raspberry Pi, Arduino, Domoticz, potem także Home Assistant i kilometry skrętki. "
            "Bramka RS485 to pierwszy z modułów systemu; zanim powstała jej finalna wersja, przeszła kilka prototypów.",
            "W CodeGarage pomagałem przy tym projekcie na wczesnym etapie, po stronie oprogramowania: "
            "rozwijałem w C++ oprogramowanie do sterowania domem oparte na Domoticzu, pracując na Linuksie.",
        ],
        note="Schemat jest poglądowy. Zrzut ekranu poniżej pokazuje, jak wygląda Domoticz w użyciu, ale nie pochodzi z tej instalacji.",
        # Szczegóły od autora projektu – link tylko na podstronie, nie na stronie głównej
        more_links=("Więcej o projekcie pisze jego autor na blogu Leniwiec.org:", [
            ("Inteligentny dom DIY – projekt wymknął się spod kontroli",
             "https://www.leniwiec.org/2021/12/17/inteligentny-dom-diy-projekt-wymknal-sie-spod-kontroli/"),
            ("Bramka RS485 MySensors – inteligentny dom DIY po kablu",
             "https://www.leniwiec.org/2022/01/04/bramka-rs485-mysensors-inteligentny-dom-diy-po-kablu/"),
        ]),
        actions=[],
    ),
]

# Projekty bez podstrony – link prowadzi prosto na zewnątrz
EXTERNAL = [
    dict(name="PostawStrone.pl", tagline="Strony www dla małych firm, z szablonami i działającymi demami",
         section="web", chip=("web", "Otwórz"), cover="images/postawstrone.png", url="https://postawstrone.pl/"),
    dict(name="CenyKart.pl", tagline="Porównywarka cen kart kolekcjonerskich z ponad 40 sklepów",
         section="web", chip=("web", "Otwórz"), cover="images/cenykart.png", url="https://cenykart.pl/"),
    dict(name="Wykrywanie twarzy", tagline="Detekcja twarzy z rejestracją i logowaniem do konta w chmurze",
         section="lab", chip=("web", "Otwórz"), cover="images/detekcja/detekcja0.png", url=f"{SITE}/faceDetector"),
    dict(name="RoboFriends", tagline="Moje pierwsze kroki w React: lista pobierana z API",
         section="lab", chip=("web", "Otwórz"), cover="https://robohash.org/test2", url=f"{SITE}/robofriends"),
]

# Gry i atrakcje, przy których pracowałem zawodowo
COMMERCIAL = [
    dict(name="Elven Assassin", line="Sieciowa gra VR: bronisz wioski przed hordami orków",
         img="https://steamcdn-a.akamaihd.net/steam/apps/503770/header.jpg?t=1575530876",
         url="https://store.steampowered.com/app/503770/Elven_Assassin/", link_label="Steam",
         role="Programista C#/Unity (Wenkly Studio, 2016–2019) – implementacja kluczowych mechanik rozgrywki i interakcji w sieciowej grze VR.",
         tech="Unity, C#, Photon, VR SDK", where="Steam, VR"),
    dict(name="Battle of Kings VR", line="Tower defense w VR, z trybem PvP",
         img="https://steamcdn-a.akamaihd.net/steam/apps/778250/header.jpg?t=1575542895",
         url="https://store.steampowered.com/app/778250/Battle_of_Kings_VR/", link_label="Steam",
         role="Programista C#/Unity (Wenkly Studio, 2016–2019) – implementacja kluczowych mechanik rozgrywki i interakcji w sieciowej grze VR.",
         tech="Unity, C#, Photon, VR SDK", where="Steam, VR"),
    dict(name="Adventure Planet", line="Wyprawa w VR do świata dinozaurów w JuraParku Bałtów",
         img="https://juraparkbaltow.pl/wp-content/uploads/2024/08/Adventure-Planet.png.webp",
         url="https://juraparkbaltow.pl/atrakcje/adventure-planet/", link_label="Strona parku",
         role="Programista C#/Unity (LucasVision, 2022–2025) – rozwój wieloosobowej symulacji VR dla JuraParku Bałtów.",
         tech="Unity, C#, OpenXR, Unity Netcode", where="Instalacja VR w parku rozrywki"),
    dict(name="Foczka Nina", line="Interaktywna atrakcja o morskich zwierzętach w Sea Parku",
         img="https://www.seapark.pl/img/atrakcje/25.jpg",
         url="https://www.seapark.pl/foczka-nina", link_label="Strona parku",
         role="Programista C#/Unity (LucasVision, 2022–2025) – rozwój wieloosobowej, interaktywnej instalacji dla parku rozrywki w Sarbsku.",
         tech="Unity, C#, Unity Netcode", where="Instalacja w parku rozrywki"),
    dict(name="Into BeYond", line="Mobilna gra RPG akcji w mistycznym świecie",
         img="/images/intobeyond.png",
         url="https://www.facebook.com/intobeyond.game/", link_label="Facebook",
         role="Programista C#/Unity (LucasVision, 2022–2025) – rozwój kluczowych mechanik rozgrywki i systemów UI w mobilnej grze RPG na iOS.",
         tech="Unity, C#, SQLite, REST API, JSON", where="iOS"),
    dict(name="Inteligentny dom", line="Przewodowy inteligentny dom DIY na Domoticzu: Raspberry Pi, Arduino i moduły MySensors po RS485. Pomagałem przy oprogramowaniu na wczesnym etapie.",
         img="/images/domoticz/schemat.png",
         url="/inteligentny-dom.html", link_label="Zobacz projekt",
         role="Junior Software Developer (CodeGarage, 2020–2021) – pomoc na wczesnym etapie projektu: rozwój oprogramowania (C++) do sterowania inteligentnym domem opartym na Domoticz. "
              "Projekt to przewodowa instalacja DIY: Raspberry Pi, Arduino i moduły MySensors komunikujące się po RS485, z bramką Ethernet na szynie DIN.",
         tech="C++, Linux, Domoticz", where="Inteligentny dom, CodeGarage"),
    # Gry nie ma już w App Store (stary link: apps.apple.com/gb/app/.../id1053989443), więc bez linku
    dict(name="MTB Downhill Simulator", line="Zjazdy na czas i akrobacje na rowerze. Gry nie ma już w App Store.",
         img="/images/downhill.jpg",
         url=None, link_label="Niedostępna",
         role="Programista C#/Unity (Wenkly Studio, 2016–2019) – implementacja mechanik rozgrywki w grze mobilnej.",
         tech="Unity, C#", where="iOS, gra już niedostępna"),
]

# Kanał YouTube – miniatury wybranych filmów
YT_VIDEOS = [
    ("G9RAOkauEPE", "La Vie En Rose na ukulele"),
    ("6yTu_lrv6zE", "Clocks (Coldplay) na ukulele"),
    ("BZfMV0aZ2Vg", "Nad pięknym modrym Dunajem na ukulele"),
    ("JPhpEVtM7So", "Devlog: jak powstawało Chrono Drive"),
]

SECTIONS = [
    ("graj", "Zagraj w przeglądarce", "Bez instalowania. Kliknij i grasz.", True),
    ("telefon", "Do pobrania i archiwum", "Janusz czeka na itch.io. ReBounce i Komu Winien zniknęły już z Google Play, zostały zrzuty ekranu.", False),
    ("web", "Strony i narzędzia", "Rzeczy, z których można po prostu korzystać.", False),
    ("lab", "Eksperymenty", "Projekty, na których się uczyłem, w tym praca magisterska.", False),
]

# ---------------------------------------------------------------------------
# Treści dla rekrutera (z CV)
# ---------------------------------------------------------------------------

CV_SUMMARY = (
    "Inżynier (mgr inż.) z ponad 8-letnią praktyką, głównie jako programista C# i C++ oraz z bazami danych (SQL). "
    "Mam zróżnicowane doświadczenie: od gier VR, symulacji 3D, Smart Home i projektów webowych (JS/HTML/CSS), "
    "po wsparcie systemów enterprise (WMS) wraz z zarządzaniem incydentami."
)

EXPERIENCE = [
    dict(title="Specjalista IT Help Desk", org="Mecalux Sp. z o.o., Gliwice", when="kwiecień 2026 – czerwiec 2026",
         points=["Wsparcie EasyWMS: rozwiązywanie problemów, np. blokad zleceń wysyłkowych i synchronizacji danych między oprogramowaniem a automatyką, w ramach systemu ITSM i dyżurów on-call."],
         tech="EasyWMS, SQL (Oracle, PL/SQL Developer), VPN, system ITSM"),
    dict(title="Programista C#/Unity Engine", org="LucasVision, zdalnie / Bielsko-Biała", when="luty 2022 – październik 2025",
         points=["Rozwój wieloosobowych instalacji VR dla klientów B2B (np. „Adventure Planet”, „Foczka Nina”).",
                 "Implementacja kluczowych mechanik i systemów UI dla mobilnej gry RPG „Into BeYond”."],
         tech="Unity, C# (.NET), LINQ, VR, Unity Netcode, SQLite, REST API, JSON, TortoiseSVN, Python"),
    dict(title="Junior Software Developer (C++, Web)", org="CodeGarage, Tarnowskie Góry", when="sierpień 2020 – grudzień 2021",
         points=["Rozwój oprogramowania do sterowania inteligentnymi domami Domoticz (C++).",
                 "Utrzymanie mniejszych projektów webowych i sklepu e-commerce."],
         tech="C++, Linux, VirtualBox, JavaScript, HTML/CSS, Bash, Git, Shoper"),
    dict(title="Programista C#/Unity Engine", org="Wenkly Studio, Gliwice", when="maj 2016 – wrzesień 2019",
         points=["Implementacja mechanik rozgrywki w komercyjnych grach VR (Elven Assassin, Battle of Kings) i mobilnych (MTB Downhill Simulator).",
                 "Optymalizacja i portowanie tytułów pod kątem wydajności na Oculus Quest i Nintendo Switch."],
         tech="Unity, C# (.NET), LINQ, Photon, VR SDK, Sourcetree"),
    dict(title="Informatyk (dział IT)", org="ZACH „Chemet” S.A., Tarnowskie Góry", when="maj 2015",
         points=["Modyfikacja programów w MS Access, wsparcie sprzętowe, tłumaczenie instrukcji Symantec Backup Exec."],
         tech="MS Access, VBA, Symantec Backup Exec"),
]

OWN_FOR_CV = [
    dict(name="CenyKart.pl", url="https://cenykart.pl/", img="/images/cenykart.png",
         line="Porównywarka cen kart kolekcjonerskich: oferty z ponad 40 sklepów, kalendarz premier i historia cen."),
    dict(name="PostawStrone.pl", url="https://postawstrone.pl/", img="/images/postawstrone.png",
         line="Usługa tworzenia stron dla małych firm, z szablonami branżowymi, konfiguratorem i działającymi demami."),
    dict(name="IleNetto", url="/ilenetto.html", img="/images/ilenetto/ilenetto1.png",
         line="Kalkulator wynagrodzeń UoP i B2B: podatki i składki ZUS."),
    dict(name="Uczenie parkowania", url="/uczenie.html", img="/images/uczenie/uczenie0.png",
         line="Praca magisterska: porównanie algorytmów GA i PPO w uczeniu sieci neuronowych jazdy i parkowania.",
         tech="Unity, Python"),
    dict(name="Civilization Duel", url="/civduel.html", img="/images/civduel/civduel1.png",
         line="Karcianka strategiczna o władzę nad światem: gra online, z AI lub lokalnie, w przeglądarce."),
    dict(name="Zenith Rush", url="/zenithrush.html", img="/images/zenithrush/zenith1.png",
         line="Wyścigi na czas z ulepszeniami i odblokowywaniem nowych aut, grywalne w przeglądarce."),
    dict(name="Chrono Drive", url="/carintime.html", img="/images/carintime/carintime0.png",
         line="Samochodówka, w której manipulujesz czasem: pojazdy i bramy poruszają się razem z graczem."),
    dict(name="SpaceShift", url="/spaceshift.html", img="/images/spaceshift/spaceshift0.png",
         line="Gra zręcznościowa: lot przez kolejne strefy galaktyki z własnymi przeszkodami."),
    dict(name="ReBounce", url="/rebounce.html", img="/images/rebounce/rebounce0.png",
         line="Mobilna gra zręcznościowa: odbijanie piłki od platform, opublikowana w Google Play."),
    dict(name="Janusz: Misja Passat", url="/janusz.html", img="/images/janusz/janusz1.jpg",
         line="Gra mobilna o zbieraniu na Passata w 30 dni, współtworzona z Barteboj."),
]

SKILLS = [
    ("Języki", ["C# (.NET)", "C++", "SQL", "JavaScript", "HTML/CSS", "Python", "VBA", "Bash"]),
    ("Silniki i narzędzia", ["Unity", "Unreal Engine", "Unity Netcode", "Photon", "OpenXR", "LINQ", "REST API", "JSON", "Git", "Sourcetree", "TortoiseSVN"]),
    ("Bazy i systemy", ["SQLite", "Oracle", "Linux", "TCP/IP", "VPN", "Active Directory (podstawy)", "ITSM", "WMS"]),
    ("AI programming", ["Claude Code", "ChatGPT", "Antigravity", "MCP"]),
    ("Praca", ["SOLID, KISS, DRY", "wzorce projektowe", "Agile/Scrum", "Jira"]),
]

CERTS = [
    ("Google IT Support (Professional Certificate)", "/assets/other/Coursera S2ZU3OGMK8P3.pdf"),
    ("Complete SQL Mastery", "/assets/other/certificate-of-completion-for-complete-sql-mastery.pdf"),
]

# ---------------------------------------------------------------------------
# Narzędzia
# ---------------------------------------------------------------------------

THUMB_DIR = ROOT / "images" / "thumbs"


def thumb(path, width=960):
    """Zwraca ścieżkę (od korzenia) do miniatury WebP dla lokalnego obrazka."""
    if path.startswith("http"):
        return path
    rel = path.lstrip("/")
    src = ROOT / rel
    name = rel.replace("images/", "", 1).replace("/", "-").rsplit(".", 1)[0] + f"-{width}.webp"
    out = THUMB_DIR / name
    if not out.exists() or out.stat().st_mtime < src.stat().st_mtime:
        THUMB_DIR.mkdir(parents=True, exist_ok=True)
        im = Image.open(src)
        im = im.convert("RGBA") if im.mode in ("P", "LA") else im
        if im.width > width:
            im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        im.save(out, "WEBP", quality=80, method=6)
    return "/images/thumbs/" + name


def e(text):
    return escape(text, quote=True)


def ext(url):
    """Atrybuty dla linków zewnętrznych."""
    return ' target="_blank" rel="noopener"' if url.startswith("http") else ""


GTAG = """	<script async src="https://www.googletagmanager.com/gtag/js?id=G-8J2FPZWNWB"></script>
	<script>
		window.dataLayer = window.dataLayer || [];
		function gtag(){dataLayer.push(arguments);}
		gtag('js', new Date());
		gtag('config', 'G-8J2FPZWNWB');
	</script>"""


def head(title, description, path, image, extra_class=""):
    url = SITE + path
    img = image if image.startswith("http") else SITE + "/" + image.lstrip("/")
    return f"""<!DOCTYPE html>
<html lang="pl">
<head>
{GTAG}
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<title>{e(title)}</title>
	<meta name="description" content="{e(description)}" />
	<meta name="author" content="Mateusz Michalik" />
	<link rel="canonical" href="{url}" />
	<meta property="og:type" content="website" />
	<meta property="og:locale" content="pl_PL" />
	<meta property="og:url" content="{url}" />
	<meta property="og:title" content="{e(title)}" />
	<meta property="og:description" content="{e(description)}" />
	<meta property="og:image" content="{img}" />
	<meta name="twitter:card" content="summary_large_image" />
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
	<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&amp;display=swap" />
	<link rel="stylesheet" href="/assets/site.css?v=12" />
	<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
	<link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32" />
	<link rel="apple-touch-icon" href="/apple-touch-icon.png" />
	<script>
		// Facebook dokleja ?fbclid=… do linków – usuń go z paska adresu
		if (location.search.indexOf('fbclid=') > -1) {{
			var u = new URL(location.href);
			u.searchParams.delete('fbclid');
			history.replaceState(null, '', u.pathname + u.search + u.hash);
		}}
	</script>
</head>
<body{' class="' + extra_class + '"' if extra_class else ''}>
	<a class="skip" href="#tresc">Przejdź do treści</a>
"""


def topbar(links):
    items = "\n".join(f'\t\t\t\t<a href="{href}"{cls}>{e(label)}</a>' for label, href, cls in links)
    return f"""	<header class="topbar">
		<div class="wrap">
			<a class="wordmark" href="/">Mateusz Michalik</a>
			<nav aria-label="Nawigacja">
{items}
			</nav>
		</div>
	</header>
"""


ICON_MAIL = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="5" width="19" height="14" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>'
ICON_YOUTUBE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .6 12a31 31 0 0 0 .4 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .4-4.8 31 31 0 0 0-.4-4.8zM9.7 15.1V8.9l5.8 3.1-5.8 3.1z"/></svg>'
ICON_GITHUB = '<svg viewBox="0 0 16 16" aria-hidden="true"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>'


def mail_attrs():
    """Adres nie trafia do HTML w całości – skrypt w stopce składa mailto: dopiero po kliknięciu."""
    user, domain = EMAIL.split("@")
    return f'href="#kontakt" data-u="{user[::-1]}" data-d="{domain[::-1]}"'


MAIL_SCRIPT = """	<script>
		document.querySelectorAll('[data-u]').forEach(function (a) {
			a.addEventListener('click', function (ev) {
				ev.preventDefault();
				var r = function (s) { return s.split('').reverse().join(''); };
				location.href = 'mailto:' + r(a.dataset.u) + '@' + r(a.dataset.d);
			});
		});
	</script>"""


def footer():
    return f"""	<footer class="footer" id="kontakt">
		<div class="wrap">
			<div>
				<h2>Masz pomysł albo pytanie?</h2>
				<p>Napisz, chętnie odpowiem.</p>
			</div>
			<ul class="socials">
				<li><a class="social" {mail_attrs()} aria-label="Napisz maila" title="Napisz maila">{ICON_MAIL}</a></li>
				<li><a class="social" href="{YOUTUBE}" target="_blank" rel="noopener" aria-label="YouTube" title="YouTube">{ICON_YOUTUBE}</a></li>
				<li><a class="social" href="{GITHUB}" target="_blank" rel="noopener" aria-label="GitHub" title="GitHub">{ICON_GITHUB}</a></li>
			</ul>
		</div>
	</footer>
{MAIL_SCRIPT}
</body>
</html>
"""


def tile(name, tagline, cover, href, chip):
    kind, label = chip
    return f"""				<a class="tile" href="{href}"{ext(href)}>
					<span class="tile-img"><img src="{thumb(cover)}" alt="" loading="lazy" /></span>
					<span class="tile-body">
						<span class="tile-name">{e(name)}</span>
						<span class="tile-line">{e(tagline)}</span>
						<span class="chip chip--{kind}">{e(label)}</span>
					</span>
				</a>"""


# ---------------------------------------------------------------------------
# Strona główna
# ---------------------------------------------------------------------------

def youtube_section():
    thumbs = "\n".join(
        f'\t\t\t\t\t<a href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">'
        f'<img src="https://i.ytimg.com/vi/{vid}/mqdefault.jpg" alt="" loading="lazy" /><span>{e(label)}</span></a>'
        for vid, label in YT_VIDEOS
    )
    return f"""		<section class="section section--band" id="youtube">
			<div class="wrap yt">
				<div class="yt-text">
					<h2>Na YouTube gram na ukulele</h2>
					<p>Na kanale Mateq głównie ukulele w wersji fingerstyle: od Coldplay i Green Day po Edith Piaf, Scotta Joplina i Straussa. Między nimi wpadają devlogi z Unity (tak rodziło się Chrono Drive), jakieś paczki z FIFY i drobne komputerowe porady. Bez spiny, jak znajdę chwilę.</p>
					<a class="btn" href="{YOUTUBE}" target="_blank" rel="noopener">Zajrzyj na kanał</a>
				</div>
				<div class="yt-thumbs">
{thumbs}
				</div>
			</div>
		</section>"""


def build_home():
    stickers = ["civduel", "carintime", "zenithrush", "ilenetto"]
    by_slug = {p["slug"]: p for p in PROJECTS}
    sticker_html = "\n".join(
        f'\t\t\t\t<a class="sticker" href="/{s}.html"><img src="{thumb(by_slug[s]["cover"], 640)}" alt="" /><span>{e(by_slug[s]["name"])}</span></a>'
        for s in stickers
    )

    sections = []
    for key, title, lead, big in SECTIONS:
        in_section = sorted((p for p in PROJECTS if p["section"] == key), key=lambda p: p.get("archived", False))
        tiles = [tile(p["name"], p["tagline"], p["cover"], f"/{p['slug']}.html", p["chip"]) for p in in_section]
        tiles += [tile(x["name"], x["tagline"], x["cover"], x["url"], x["chip"]) for x in EXTERNAL if x["section"] == key]
        if key == "web":
            tiles = tiles[1:] + tiles[:1]  # nowe strony najpierw, IleNetto na końcu
        sections.append(f"""		<section class="section{" section--band" if key == "telefon" else ""}" id="{key}">
			<div class="wrap">
				<div class="section-head">
					<h2>{e(title)}</h2>
					<p>{e(lead)}</p>
				</div>
				<div class="tiles{' tiles--big' if big else ''}">
{chr(10).join(tiles)}
				</div>
			</div>
		</section>""")
        if key == "web":
            def shelf_item(c):
                img = f'<img src="{thumb(c["img"], 480)}" alt="" loading="lazy" />' if c["img"] else '<span class="noimg"></span>'
                inner = f'{img}<strong>{e(c["name"])}</strong><small>{e(c["line"])}</small>'
                if c["url"]:
                    inner += f'<span class="chip chip--look">{e(c["link_label"])}</span>'
                    return f'\t\t\t\t\t<a href="{c["url"]}"{ext(c["url"])}>{inner}</a>'
                inner += f'<span class="chip chip--gone">{e(c["link_label"])}</span>'
                return f'\t\t\t\t\t<div class="gone">{inner}</div>'
            shelf = "\n".join(shelf_item(c) for c in COMMERCIAL)
            sections.append(f"""		<section class="section section--dark" id="zawodowo">
			<div class="wrap">
				<div class="section-head">
					<h2>Projekty, przy których pracowałem</h2>
					<p>Gry VR na Steamie, wieloosobowe symulacje VR, interaktywne atrakcje w parkach rozrywki, gry mobilne i trochę inteligentnego domu. Do tych rzeczy dokładałem swoją cegiełkę zawodowo.</p>
				</div>
				<div class="shelf">
{shelf}
				</div>
			</div>
		</section>""")

    html = head(
        "Mateusz Michalik – gry i aplikacje",
        "Gry w przeglądarce i na telefon, kalkulatory i strony www. Kolekcja projektów Mateusza Michalika – wybierz coś i pograj.",
        "/", "images/civduel/civduel1.png",
    )
    html += topbar([("Gry", "#graj", ""), ("Aplikacje", "#web", ""), ("YouTube", "#youtube", ""), ("Kontakt", "#kontakt", "")])
    html += f"""	<main id="tresc">
		<section class="hero">
			<div class="wrap">
				<div>
					<h1>Cześć, tu Mateusz</h1>
					<p class="lead">Po godzinach dłubię w grach i różnych apkach, a potem wrzucam je tutaj. Część odpalisz od razu w przeglądarce, część to starsze rzeczy na telefon. Klikaj śmiało, a jak coś nie działa, daj znać.</p>
					<div class="hero-actions">
						<a class="btn" href="#graj">Zagraj w coś</a>
					</div>
				</div>
				<div class="stickers" aria-label="Wybrane projekty">
{sticker_html}
				</div>
			</div>
		</section>
{chr(10).join(sections)}
{youtube_section()}
	</main>
"""
    html += footer()
    (ROOT / "index.html").write_text(html, encoding="utf-8", newline="\n")


# ---------------------------------------------------------------------------
# Strony projektów
# ---------------------------------------------------------------------------

def build_project(p):
    portrait = p.get("portrait", False)
    archived = p.get("archived", False)
    actions = "\n".join(
        f'\t\t\t\t<a class="btn{" btn--ghost" if i or archived else ""}" href="{url}"{ext(url)}>{e(label)}</a>'
        for i, (label, url) in enumerate(p["actions"])
    )
    if archived:
        actions = ('\t\t\t\t<p class="archived">Tej aplikacji nie ma już w Google Play, więc stary link może nie działać. '
                   'Projekt zostaje tu w archiwum, razem ze zrzutami ekranu.</p>\n' + actions)
    if p.get("embed") and not p["actions"]:
        actions = '\t\t\t\t<a class="btn" href="#zagraj">Zagraj poniżej</a>'
    elif p.get("embed") and p["section"] == "graj":
        actions += '\n\t\t\t\t<a class="btn btn--ghost" href="#zagraj">Zagraj tutaj</a>'

    body = "\n".join(f"\t\t\t\t<p>{e(t)}</p>" for t in p["body"])
    if p.get("more_links"):
        intro, links = p["more_links"]
        items = "".join(f'<li><a href="{url}" target="_blank" rel="noopener">{e(label)}</a></li>' for label, url in links)
        body += f'\n\t\t\t\t<div class="more-links"><p>{e(intro)}</p><ul>{items}</ul></div>'
    if p.get("note"):
        body += f'\n\t\t\t\t<p class="note">{e(p["note"])}</p>'

    play = ""
    blocks = []
    if p.get("video"):
        blocks.append(f'\t\t\t\t<div class="frame frame--wide"><iframe src="{p["video"]}" title="Zwiastun {e(p["name"])}" loading="lazy" allowfullscreen></iframe></div>')
    if p.get("embed"):
        em = p["embed"]
        if p.get("video"):
            blocks.append("\t\t\t\t<br />")
        blocks.append(f'\t\t\t\t<div class="frame frame--{em["style"]}"><iframe src="{e(em["src"])}" title="{e(p["name"])}" loading="lazy" allowfullscreen></iframe></div>')
    if p.get("itch"):
        src, href, label = p["itch"]
        blocks.append(f'\t\t\t\t<iframe class="itch" src="{src}" title="{e(p["name"])} na itch.io" loading="lazy"><a href="{href}">{e(label)}</a></iframe>')
    if blocks:
        title = p.get("embed", {}).get("title") or ("Zagraj tutaj" if p.get("embed") else "Pobierz")
        play = f"""		<section class="play" id="zagraj">
			<div class="wrap">
				<h2>{e(title)}</h2>
{chr(10).join(blocks)}
			</div>
		</section>
"""

    shots = "\n".join(
        f'\t\t\t\t\t<a href="/{g}" target="_blank" rel="noopener"><img src="{thumb(g, 720)}" alt="Zrzut ekranu {i + 1} z {e(p["name"])}" loading="lazy" /></a>'
        for i, g in enumerate(p["gallery"])
    )

    credits = "\n".join(
        f'\t\t\t\t<p class="credit gallery-credit"><a href="{url}" target="_blank" rel="noopener">{e(label)}</a></p>'
        for label, url in p.get("credits", [])
    )

    others = [q for q in PROJECTS if q["slug"] != p["slug"] and q["section"] == p["section"]][:3]
    if len(others) < 3:
        others += [q for q in PROJECTS if q["slug"] != p["slug"] and q not in others and q["section"] != "pro"][: 3 - len(others)]
    more = "\n".join(tile(q["name"], q["tagline"], q["cover"], f"/{q['slug']}.html", q["chip"]) for q in others)

    html = head(f"{p['name']} – Mateusz Michalik", f"{p['name']}: {p['tagline']}.", f"/{p['slug']}.html", p["cover"])
    html += topbar([("Wszystkie projekty", "/#graj", ""), ("Kontakt", "#kontakt", "")])
    html += f"""	<main id="tresc">
		<section class="project-hero">
			<div class="wrap">
				<a class="back" href="/">Wróć do wszystkich projektów</a>
				<h1>{e(p['name'])}</h1>
				<p class="tagline">{e(p['tagline'])}</p>
				<div class="project-actions">
{actions}
				</div>
			</div>
		</section>
		<section>
			<div class="wrap project-body">
				<div class="project-text">
{body}
				</div>
				<div class="project-cover{' project-cover--portrait' if portrait else ''}"><img src="{thumb(p['cover'], 960)}" alt="" /></div>
			</div>
		</section>
{play}		<section class="gallery">
			<div class="wrap">
				<h2>Zrzuty ekranu</h2>
				<div class="shots{' shots--portrait' if portrait else ''}">
{shots}
				</div>
{credits}
			</div>
		</section>
		<section class="more">
			<div class="wrap">
				<h2>Zobacz też</h2>
				<div class="tiles">
{more}
				</div>
			</div>
		</section>
	</main>
"""
    html += footer()
    (ROOT / f"{p['slug']}.html").write_text(html, encoding="utf-8", newline="\n")


# ---------------------------------------------------------------------------
# /portfolio
# ---------------------------------------------------------------------------

def build_portfolio():
    timeline = "\n".join(
        f"""					<li>
						<h3>{e(x['title'])}</h3>
						<p class="when">{e(x['org'])}, {e(x['when'])}</p>
{chr(10).join(f'						<p>{e(pt)}</p>' for pt in x['points'])}
						<p class="tech">{e(x['tech'])}</p>
					</li>"""
        for x in EXPERIENCE
    )

    def card(name, url, img, where, line, tech, credit=None):
        credit_html = f'<p class="credit"><a href="{credit[1]}" target="_blank" rel="noopener">{e(credit[0])}</a></p>' if credit else ''
        return f"""					<article class="cv-project">
						{f'<img src="{thumb(img, 640)}" alt="" loading="lazy" />' if img else ''}
						<div>
							<h3>{f'<a href="{url}"{ext(url)}>{e(name)}</a>' if url else e(name)}</h3>
							<span class="where">{e(where)}</span>
							<p>{e(line)}</p>
							{f'<p class="tech">{e(tech)}</p>' if tech else ''}
							{credit_html}
						</div>
					</article>"""

    commercial = "\n".join(card(c["name"], c["url"], c["img"], c["where"], c["role"], c["tech"], c.get("credit")) for c in COMMERCIAL)
    own = "\n".join(card(o["name"], o["url"], o["img"], "Projekt własny", o["line"], o.get("tech", "")) for o in OWN_FOR_CV)
    skills = "\n".join(
        f"""				<h2>{e(group)}</h2>
				<ul class="cv-skills">{''.join(f'<li>{e(s)}</li>' for s in items)}</ul>"""
        for group, items in SKILLS
    )
    certs = "\n".join(f'\t\t\t\t\t\t<li><a href="{e(url)}" target="_blank" rel="noopener">{e(name)}</a></li>' for name, url in CERTS)

    html = head(
        "Mateusz Michalik – programista C# / Unity | portfolio",
        "Portfolio Mateusza Michalika: programista C# i Unity z ponad 8-letnią praktyką. Gry VR, multiplayer, instalacje dla parków rozrywki i projekty webowe.",
        "/portfolio/", "images/banner-new2.jpg", extra_class="cv",
    )
    html += topbar([("Doświadczenie", "#doswiadczenie", ""), ("Projekty", "#projekty", ""),
                    ("Strona z grami", "/", ' class="nav-pro"')])
    html += f"""	<main id="tresc" class="wrap cv-layout">
		<aside class="cv-side">
			<h1>Mateusz Michalik</h1>
			<p class="cv-role">Programista C# / Unity, mgr inż. informatyki</p>
			<ul class="cv-contact">
				<li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
				<li><a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a></li>
				<li><a href="{YOUTUBE}" target="_blank" rel="noopener">YouTube</a></li>
			</ul>
			<p class="small no-print">Chętnie podeślę CV w PDF – wystarczy napisać maila.</p>
		</aside>
		<aside class="cv-skillbox" aria-label="Umiejętności">
{skills}
		</aside>
		<div class="cv-main">
			<section>
				<p class="cv-summary">{e(CV_SUMMARY)}</p>
			</section>
			<section id="doswiadczenie">
				<h2>Doświadczenie</h2>
				<ol class="timeline">
{timeline}
				</ol>
			</section>
			<section id="projekty">
				<h2>Projekty komercyjne</h2>
				<div class="cv-projects">
{commercial}
				</div>
			</section>
			<section>
				<h2>Projekty własne</h2>
				<div class="cv-projects">
{own}
				</div>
				<p class="no-print" style="margin-top:20px">Więcej gier i aplikacji, w które można od razu zagrać: <a href="/">strona z projektami</a>.</p>
			</section>
			<section>
				<h2>Wykształcenie i certyfikaty</h2>
				<ul class="cv-list">
					<li><strong>Politechnika Śląska, Gliwice</strong> – mgr inż., Makrokierunek (Informatyka, Automatyka, Elektronika), specjalizacja Informatyka, studia w j. angielskim, 2019. Praca magisterska: porównanie algorytmów uczenia sieci neuronowych (PPO, GA) w Unity/Python.</li>
{certs}
				</ul>
			</section>
		</div>
	</main>
</body>
</html>
"""
    out = ROOT / "portfolio" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    build_home()
    for p in PROJECTS:
        build_project(p)
    build_portfolio()
    print("Gotowe:", 2 + len(PROJECTS), "stron")
