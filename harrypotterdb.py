import tkinter as tk
from tkinter import messagebox
import json, os
                   

C = {
    "bg_void":  "#05060f",
    "bg_deep":  "#0b0d1e",
    "bg_panel": "#0f1228",
    "bg_card":  "#141830",
    "bg_hover": "#1c2040",
    "border":   "#2a2e52",
    "gold":     "#c9a84c",
    "gold_lt":  "#f0d080",
    "gold_dim": "#7a5f20",
    "text":     "#d4cfc4",
    "text_dim": "#7a7590",
    "text_br":  "#f0ead8",
    "green":    "#4caf50",
    "red":      "#ff6b6b",
}

FONT_TITLE  = ("Georgia", 18, "bold")
FONT_CAT    = ("Helvetica", 10, "bold")
FONT_ITEM   = ("Helvetica", 10)
FONT_LABEL  = ("Helvetica", 8,  "bold")
FONT_VALUE  = ("Helvetica", 10)
FONT_STATUS = ("Helvetica", 8)

BASE = os.path.dirname(os.path.abspath(__file__))
IMG  = os.path.join(BASE, "images")

def ip(folder, filename):
    """Return absolute path: images/<folder>/<filename>"""
    return os.path.join(IMG, folder, filename)


DB = {

    # List of books
    "books": [
        {"name": "Philosopher's Stone",  "icon": "📖", "badge": "Book 1",
         "image": ip("books","book1.jpg"),
         "fields": {"Author":"J.K. Rowling","Year":"1997","Pages":"223",
                    "House Featured":"Gryffindor",
                    "Synopsis":"Harry discovers he is a wizard on his 11th birthday. He makes his first friends and faces Voldemort for the first time beneath Hogwarts."}},
        {"name": "Chamber of Secrets",   "icon": "📖", "badge": "Book 2",
         "image": ip("books","book2.jpg"),
         "fields": {"Author":"J.K. Rowling","Year":"1998","Pages":"251",
                    "House Featured":"Gryffindor / Slytherin",
                    "Synopsis":"Students are being petrified. Harry discovers he is a Parselmouth and must face the memory of the young Tom Riddle inside the Chamber."}},
        {"name": "Prisoner of Azkaban",  "icon": "📖", "badge": "Book 3",
         "image": ip("books","book3.jpg"),
         "fields": {"Author":"J.K. Rowling","Year":"1999","Pages":"317",
                    "House Featured":"Gryffindor",
                    "Synopsis":"Sirius Black escapes Azkaban. Harry learns shocking truths about his father's friends and uses a Time-Turner to change fate."}},
        {"name": "Goblet of Fire",       "icon": "📖", "badge": "Book 4",
         "image": ip("books","book4.jpg"),
         "fields": {"Author":"J.K. Rowling","Year":"2000","Pages":"636",
                    "House Featured":"All Houses",
                    "Synopsis":"Harry is mysteriously entered into the Triwizard Tournament. Voldemort rises again at the end of a deadly maze."}},
        {"name": "Order of the Phoenix", "icon": "📖", "badge": "Book 5",
         "image": ip("books","book5.jpg"),
         "fields": {"Author":"J.K. Rowling","Year":"2003","Pages":"766",
                    "House Featured":"Gryffindor / Ravenclaw",
                    "Synopsis":"Dumbledore's Army forms to resist Umbridge. Harry is haunted by Voldemort's visions and suffers a devastating personal loss."}},
        {"name": "Half-Blood Prince",    "icon": "📖", "badge": "Book 6",
         "image": ip("books","book6.jpg"),
         "fields": {"Author":"J.K. Rowling","Year":"2005","Pages":"607",
                    "House Featured":"Slytherin",
                    "Synopsis":"Dumbledore reveals Voldemort's Horcruxes. Harry discovers the secrets of the annotated potions textbook belonging to the Half-Blood Prince."}},
        {"name": "Deathly Hallows",      "icon": "📖", "badge": "Book 7",
         "image": ip("books","book7.jpg"),
         "fields": {"Author":"J.K. Rowling","Year":"2007","Pages":"607",
                    "House Featured":"All Houses",
                    "Synopsis":"Harry, Ron, and Hermione hunt Horcruxes. The Battle of Hogwarts brings the war to its climax as Harry faces his destiny."}},
    ],

    # List of characters
    "characters": [
        {"name": "Harry Potter",      "icon": "⚡", "badge": "Gryffindor",
         "image": ip("characters","Harry Potter.jpg"),
         "fields": {"House":"Gryffindor","Actor":"Daniel Radcliffe",
                    "Species":"Human-Wizard","Patronus":"Stag",
                    "Wand":"Holly & Phoenix Feather 11\"","Status":"✅ Alive",
                    "Skills":"Parseltongue, DADA, Quidditch Seeker, Occlumency (partial)"}},
        {"name": "Hermione Granger",  "icon": "📚", "badge": "Gryffindor",
         "image": ip("characters","Hermione Granger.jpg"),
         "fields": {"House":"Gryffindor","Actor":"Emma Watson",
                    "Species":"Human-Witch","Patronus":"Otter",
                    "Wand":"Vine & Dragon Heartstring 10¾\"","Status":"✅ Alive",
                    "Skills":"Top student, Charms, Potions, Time-Turner, Arithmancy"}},
        {"name": "Ron Weasley",       "icon": "♟️", "badge": "Gryffindor",
         "image": ip("characters","Ron Weasley.jpg"),
         "fields": {"House":"Gryffindor","Actor":"Rupert Grint",
                    "Species":"Human-Wizard","Patronus":"Jack Russell Terrier",
                    "Wand":"Willow & Unicorn Hair 14\"","Status":"✅ Alive",
                    "Skills":"Chess, Quidditch Keeper, Loyalty, Strategic thinking"}},
        {"name": "Albus Dumbledore",  "icon": "🌟", "badge": "Gryffindor",
         "image": ip("characters","Albus Dumbledore.jpg"),
         "fields": {"House":"Gryffindor","Actor":"Richard Harris / Michael Gambon",
                    "Species":"Human-Wizard","Patronus":"Phoenix",
                    "Wand":"Elder Wand 15\"","Status":"💀 Deceased",
                    "Skills":"Greatest wizard of his age, Transfiguration Master, Legilimency"}},
        {"name": "Draco Malfoy",      "icon": "🐍", "badge": "Slytherin",
         "image": ip("characters","Draco Malfoy.jpg"),
         "fields": {"House":"Slytherin","Actor":"Tom Felton",
                    "Species":"Human-Wizard","Patronus":"None",
                    "Wand":"Hawthorn & Unicorn Hair 10\"","Status":"✅ Alive (Redeemed)",
                    "Skills":"Occlumency, Potions, Transfiguration, Cunning"}},
        {"name": "Lord Voldemort",    "icon": "☠️", "badge": "Slytherin",
         "image": ip("characters","Lord Voldermont.jpg"),
         "fields": {"House":"Slytherin","Actor":"Ralph Fiennes",
                    "Species":"Human (Horcrux)","Patronus":"None",
                    "Wand":"Yew & Phoenix Feather 13½\"","Status":"💀 Defeated",
                    "Skills":"Legilimency, Parseltongue, Dark Magic, Flight, Horcrux creation"}},
        {"name": "Dobby",             "icon": "🧦", "badge": "Free Elf",
         "image": ip("characters","Dobby.jpg"),
         "fields": {"House":"N/A (House Elf)","Actor":"Toby Jones (voice)",
                    "Species":"House Elf","Patronus":"None",
                    "Wand":"Cannot use wand","Status":"💀 Deceased (Hero)",
                    "Skills":"Magic without wand, Apparition, Fierce loyalty to Harry"}},
    ],

    # List of houses
    "houses": [
        {"name": "Gryffindor",  "icon": "🦁", "badge": "Bravery",
         "image": ip("houses","gryffindor.jpeg"),
         "fields": {"Founder":"Godric Gryffindor","Element":"Fire",
                    "Animal":"Lion","Colours":"Scarlet & Gold",
                    "Ghost":"Nearly Headless Nick",
                    "Head of House":"Professor McGonagall",
                    "Traits":"Bravery, Courage, Nerve, Chivalry",
                    "Notable Members":"Harry Potter, Hermione Granger, Ron Weasley, Albus Dumbledore"}},
        {"name": "Hufflepuff",  "icon": "🦡", "badge": "Loyalty",
         "image": ip("houses","hufflepuff.webp"),
         "fields": {"Founder":"Helga Hufflepuff","Element":"Earth",
                    "Animal":"Badger","Colours":"Yellow & Black",
                    "Ghost":"The Fat Friar",
                    "Head of House":"Professor Sprout",
                    "Traits":"Dedication, Patience, Loyalty, Fair Play",
                    "Notable Members":"Cedric Diggory, Nymphadora Tonks, Newt Scamander"}},
        {"name": "Ravenclaw",   "icon": "🦅", "badge": "Wisdom",
         "image": ip("houses","ravenclaw.jpg"),
         "fields": {"Founder":"Rowena Ravenclaw","Element":"Air",
                    "Animal":"Eagle","Colours":"Blue & Bronze",
                    "Ghost":"The Grey Lady",
                    "Head of House":"Professor Flitwick",
                    "Traits":"Intelligence, Wit, Wisdom, Creativity",
                    "Notable Members":"Luna Lovegood, Cho Chang, Gilderoy Lockhart"}},
        {"name": "Slytherin",   "icon": "🐍", "badge": "Ambition",
         "image": ip("houses","Slytherin.webp"),
         "fields": {"Founder":"Salazar Slytherin","Element":"Water",
                    "Animal":"Serpent","Colours":"Green & Silver",
                    "Ghost":"The Bloody Baron",
                    "Head of House":"Professor Snape / Slughorn",
                    "Traits":"Ambition, Cunning, Resourcefulness, Leadership",
                    "Notable Members":"Voldemort, Draco Malfoy, Severus Snape, Merlin"}},
    ],

    #List of movies
    "movies": [
        {"name": "Philosopher's Stone",   "icon": "🎬", "badge": "2001",
         "image": ip("movies","movie1.jpg"),
         "fields": {"Director":"Chris Columbus","Year":"2001","Runtime":"152 min",
                    "Box Office":"$974 million","Rating":"PG",
                    "Synopsis":"Harry discovers he is a wizard and begins his journey at Hogwarts, facing his nemesis for the first time."}},
        {"name": "Chamber of Secrets",    "icon": "🎬", "badge": "2002",
         "image": ip("movies","movie2.jpg"),
         "fields": {"Director":"Chris Columbus","Year":"2002","Runtime":"161 min",
                    "Box Office":"$879 million","Rating":"PG",
                    "Synopsis":"The Chamber of Secrets is opened. Harry battles a Basilisk and a memory of the young Voldemort."}},
        {"name": "Prisoner of Azkaban",   "icon": "🎬", "badge": "2004",
         "image": ip("movies","movie3.jpg"),
         "fields": {"Director":"Alfonso Cuarón","Year":"2004","Runtime":"142 min",
                    "Box Office":"$797 million","Rating":"PG",
                    "Synopsis":"Sirius Black escapes Azkaban. Harry and Hermione use a Time-Turner to rescue both Sirius and Buckbeak."}},
        {"name": "Goblet of Fire",        "icon": "🎬", "badge": "2005",
         "image": ip("movies","movie4.jpg"),
         "fields": {"Director":"Mike Newell","Year":"2005","Runtime":"157 min",
                    "Box Office":"$896 million","Rating":"PG-13",
                    "Synopsis":"The Triwizard Tournament and the terrifying return of Voldemort in the flesh at a deadly graveyard."}},
        {"name": "Order of the Phoenix",  "icon": "🎬", "badge": "2007",
         "image": ip("movies","movie5.jpg"),
         "fields": {"Director":"David Yates","Year":"2007","Runtime":"138 min",
                    "Box Office":"$942 million","Rating":"PG-13",
                    "Synopsis":"Dumbledore's Army forms to fight Umbridge. The Department of Mysteries battle ends in tragic loss."}},
        {"name": "Half-Blood Prince",     "icon": "🎬", "badge": "2009",
         "image": ip("movies","movie6.jpg"),
         "fields": {"Director":"David Yates","Year":"2009","Runtime":"153 min",
                    "Box Office":"$934 million","Rating":"PG",
                    "Synopsis":"Dumbledore reveals Voldemort's Horcruxes. Snape's true identity as the Half-Blood Prince is revealed."}},
        {"name": "Deathly Hallows Pt. 1", "icon": "🎬", "badge": "2010",
         "image": ip("movies","movie7.jpg"),
         "fields": {"Director":"David Yates","Year":"2010","Runtime":"146 min",
                    "Box Office":"$976 million","Rating":"PG-13",
                    "Synopsis":"The trio hunt Horcruxes on the run. Dobby dies saving them from Malfoy Manor."}},
        {"name": "Deathly Hallows Pt. 2", "icon": "🎬", "badge": "2011",
         "image": ip("movies","movie8.jpg"),
         "fields": {"Director":"David Yates","Year":"2011","Runtime":"130 min",
                    "Box Office":"$1.34 billion","Rating":"PG-13",
                    "Synopsis":"The Battle of Hogwarts. Harry sacrifices himself, discovers Snape's true loyalty, and defeats Voldemort for the last time."}},
    ],

    # List of potions
    "potions": [
        {"name": "Ageing Potion",             "icon": "🧪", "badge": "Transformation",
         "image": ip("potions","ageingpotion.avif"),
         "fields": {"Type":"Transformation","Difficulty":"Moderate",
                    "Effect":"Ages the drinker temporarily",
                    "Known Users":"Fred & George Weasley (backfired)",
                    "Description":"Causes the drinker to age rapidly. Fred and George used it to bypass Dumbledore's Age Line around the Goblet of Fire — it spectacularly backfired, giving them long white beards."}},
        {"name": "Alihotsy Draught",           "icon": "🧪", "badge": "Mind-Affecting",
         "image": ip("potions","Alihotsy Draught.avif"),
         "fields": {"Type":"Mind-Affecting","Difficulty":"Moderate",
                    "Effect":"Induces uncontrollable laughter and hysteria",
                    "Known Users":"Studied in Potions class",
                    "Description":"Brewed from Alihotsy leaves, this draught induces uncontrollable hysterical laughter. Bezoar or antidote required to reverse the effects."}},
        {"name": "Amortentia",                 "icon": "🧪", "badge": "Love Potion",
         "image": ip("potions","Amortentia.avif"),
         "fields": {"Type":"Love Potion","Difficulty":"Advanced",
                    "Effect":"Causes powerful infatuation (not true love)",
                    "Known Users":"Merope Gaunt used on Tom Riddle Sr.",
                    "Description":"The most powerful love potion in existence. It smells different to each person — whatever attracts them most. Has a pearly sheen and distinctive spiral steam. Cannot produce true love."}},
        {"name": "Angel's Trumpet Draught",    "icon": "🧪", "badge": "Sedative",
         "image": ip("potions","Angel's Trumpet Draught.avif"),
         "fields": {"Type":"Sedative / Poisonous","Difficulty":"Advanced",
                    "Effect":"Induces deep, potentially fatal sleep",
                    "Known Users":"Dark wizards",
                    "Description":"A dangerous draught brewed from the Angel's Trumpet flower. Causes deep unconsciousness — potentially lethal in large doses. Classified as a restricted substance."}},
        {"name": "Antidote to Common Poisons", "icon": "🧪", "badge": "Antidote",
         "image": ip("potions","Antidote to Common Poisons.avif"),
         "fields": {"Type":"Antidote","Difficulty":"Beginner",
                    "Effect":"Counteracts most standard poisons",
                    "Known Users":"Taught to first-years",
                    "Description":"A standard antidote taught early at Hogwarts. Brewed using bezoar-adjacent ingredients, it neutralises common poisons and is a staple of every school's medical supply."}},
        {"name": "Bloodroot Poison",           "icon": "🧪", "badge": "Poison",
         "image": ip("potions","Bloodroot_Poison.webp"),
         "fields": {"Type":"Poison","Difficulty":"Restricted",
                    "Effect":"Causes severe internal damage",
                    "Known Users":"Dark practitioners",
                    "Description":"A restricted dark preparation brewed from bloodroot. Causes severe damage to internal organs and is classified as a Dark substance under Ministry of Magic regulations."}},
        {"name": "Bulgeye Potion",             "icon": "🧪", "badge": "Jinx Potion",
         "image": ip("potions","BulgeyeJPG.webp"),
         "fields": {"Type":"Jinx Potion","Difficulty":"Moderate",
                    "Effect":"Causes the drinker's eyes to bulge grotesquely",
                    "Known Users":"Students (pranks)",
                    "Description":"A prank potion causing eyes to swell and bulge outward. Occasionally used by mischievous students, though the effect is unpleasant and requires a reversal antidote."}},
        {"name": "Bundimum Pomade",            "icon": "🧪", "badge": "Topical",
         "image": ip("potions","Bundimum Pomade.webp"),
         "fields": {"Type":"Topical Preparation","Difficulty":"Moderate",
                    "Effect":"Applied externally for adhesive or surface effects",
                    "Known Users":"Potioneers",
                    "Description":"A topical potion derived from Bundimun secretion. When applied externally it exhibits strong adhesive or powerful cleansing properties on surfaces."}},
        {"name": "Bundimum Secretion",         "icon": "🧪", "badge": "Ingredient",
         "image": ip("potions","Bundimum Secretion.webp"),
         "fields": {"Type":"Potion Ingredient / Base","Difficulty":"N/A (raw material)",
                    "Effect":"Highly corrosive to organic matter",
                    "Known Users":"Potioneers (ingredient use)",
                    "Description":"The greenish secretion of a Bundimun — a fungus-like creature. Highly corrosive to wood and organic matter, used as a base ingredient in corrosive and cleaning potions."}},
        {"name": "Burn Healing Paste",         "icon": "🧪", "badge": "Healing",
         "image": ip("potions","Burn_Healing_Paste_HM.webp"),
         "fields": {"Type":"Healing","Difficulty":"Moderate",
                    "Effect":"Heals burns rapidly on contact",
                    "Known Users":"Healers, Hogwarts medical staff",
                    "Description":"A soothing orange paste applied directly to burns. Rapidly repairs burned tissue and alleviates pain — a standard item in Hogwarts' medical kit and St Mungo's."}},
        {"name": "Burning Bitterroot Balm",    "icon": "🧪", "badge": "Healing",
         "image": ip("potions","Burning_Bitterroot_Balm.webp"),
         "fields": {"Type":"Healing Balm","Difficulty":"Moderate",
                    "Effect":"Soothes burns and magical inflammation",
                    "Known Users":"Healers",
                    "Description":"A warming balm made from bitterroot. Applied externally to reduce inflammation and heal minor magical burns — often used after failed spell-casting accidents."}},
        {"name": "Calming Draught",            "icon": "🧪", "badge": "Sedative",
         "image": ip("potions","HM_y4_Calming_Draught.webp"),
         "fields": {"Type":"Sedative / Calming","Difficulty":"Moderate",
                    "Effect":"Calms extreme emotions and hysteria",
                    "Known Users":"Madam Pomfrey, St Mungo's Healers",
                    "Description":"A pale blue draught administered to witches and wizards in severe emotional distress. Madam Pomfrey gave it to students after particularly traumatic events at Hogwarts."}},
    ],

    # List of spells
    "spells": [
        {"name": "Age Line",                   "icon": "✨", "badge": "Charm",
         "image": ip("spells","Age Line.webp"),
         "fields": {"Category":"Charm","Difficulty":"Advanced",
                    "Incantation":"Age Line (drawn with wand tip)",
                    "Effect":"Creates a boundary repelling those below a set age",
                    "Users":"Albus Dumbledore",
                    "Description":"A thin golden line drawn by Dumbledore around the Goblet of Fire to prevent underage students from entering the Triwizard Tournament. Fred and George's Ageing Potion failed entirely to bypass it."}},
        {"name": "Altering Spell",             "icon": "✨", "badge": "Transfiguration",
         "image": ip("spells","Altering Spell.webp"),
         "fields": {"Category":"Transfiguration","Difficulty":"Advanced",
                    "Incantation":"Unknown",
                    "Effect":"Alters physical properties of a target",
                    "Users":"Skilled witches and wizards",
                    "Description":"A transfiguration spell that modifies the shape, size, or material composition of an object or creature. Requires precise wand control and clear mental intent."}},
        {"name": "Amplifying Charm",           "icon": "✨", "badge": "Charm",
         "image": ip("spells","Amplifying Charm.webp"),
         "fields": {"Category":"Charm","Difficulty":"Beginner–Moderate",
                    "Incantation":"Sonorus",
                    "Effect":"Amplifies the caster's voice to crowd-filling volume",
                    "Users":"Ludo Bagman, various commentators",
                    "Description":"Makes the caster's voice magically loud enough to address large crowds without Muggle equipment. Countered by Quietus. Used by Ludo Bagman to commentate at the Quidditch World Cup."}},
        {"name": "Anteoculatia",               "icon": "✨", "badge": "Jinx",
         "image": ip("spells","Anteoculatia.webp"),
         "fields": {"Category":"Jinx","Difficulty":"Moderate",
                    "Incantation":"Anteoculatia",
                    "Effect":"Causes antlers to sprout from the target's head",
                    "Users":"Attempted by Draco Malfoy (rebounded onto Goyle)",
                    "Description":"A jinx causing antlers to grow from the target's head. Draco Malfoy attempted it on Hermione Granger but Hermione deflected it and it struck Gregory Goyle instead."}},
        {"name": "Anti-Cheating Spell",        "icon": "✨", "badge": "Charm",
         "image": ip("spells","Anti-CheatingSpeall.webp"),
         "fields": {"Category":"Charm","Difficulty":"Moderate",
                    "Incantation":"Unknown",
                    "Effect":"Prevents cheating on examinations",
                    "Users":"Hogwarts staff (applied to quills and parchment)",
                    "Description":"Cast on exam quills and parchment during O.W.L.s and N.E.W.T.s. Forces a quill to refuse to write anything other than the student's own genuine answers."}},
        {"name": "Apparition / Disapparition", "icon": "✨", "badge": "Transportation",
         "image": ip("spells","ApparitionDisapparition.webp"),
         "fields": {"Category":"Transportation Magic","Difficulty":"Advanced (licensed)",
                    "Incantation":"N/A (willpower-based)",
                    "Effect":"Teleports the caster instantly to another location",
                    "Users":"Adult witches and wizards (age 17+, Ministry licensed)",
                    "Description":"Requires the Three D's: Destination, Determination, Deliberation. Splinching can occur if done incorrectly. Impossible within Hogwarts grounds due to ancient enchantments."}},
        {"name": "Aqua Eructo",                "icon": "✨", "badge": "Charm",
         "image": ip("spells","Aqua Eructo.webp"),
         "fields": {"Category":"Charm","Difficulty":"Moderate",
                    "Incantation":"Aqua Eructo",
                    "Effect":"Shoots a powerful jet of water from the wand",
                    "Users":"Hagrid, various witches and wizards",
                    "Description":"Produces a powerful jet or stream of water from the caster's wand tip. Useful for extinguishing fires, hydrating magical creatures, or combat situations."}},
        {"name": "Arrow Shooting Spell",       "icon": "✨", "badge": "Conjuration",
         "image": ip("spells","Arrow Shooting Spell.webp"),
         "fields": {"Category":"Conjuration","Difficulty":"Moderate",
                    "Incantation":"Sagitta",
                    "Effect":"Fires conjured magical arrows from the wand",
                    "Users":"Various dark wizards and duelists",
                    "Description":"Conjures a volley of magical arrows that fly from the wand tip toward a target. A combat conjuration favoured by skilled duelists who prefer projectile-based offensive spells."}},
        {"name": "Avifors Spell",              "icon": "✨", "badge": "Transfiguration",
         "image": ip("spells","Avifors Spell.webp"),
         "fields": {"Category":"Transfiguration","Difficulty":"Moderate",
                    "Incantation":"Avifors",
                    "Effect":"Transforms small objects or creatures into birds",
                    "Users":"Taught in Transfiguration class at Hogwarts",
                    "Description":"Transforms the target into a bird. One of the transfiguration spells taught at Hogwarts, requiring clear mental visualisation of the specific target bird species desired."}},
    ],
}

# Sidebar category button definitions
CAT_BTNS = [
    ("📖  Books",       "books",      "#1a3a5c"),
    ("🧙  Characters",  "characters", "#6b0000"),
    ("🏰  Houses",      "houses",     "#5c3a1a"),
    ("🎬  Movies",      "movies",     "#1a1a5c"),
    ("🧪  Potions",     "potions",    "#1a472a"),
    ("✨  Spells",      "spells",     "#4a0060"),
]
TITLES = {
    "books":      "📖  BOOKS",
    "characters": "🧙  CHARACTERS",
    "houses":     "🏰  HOUSES",
    "movies":     "🎬  MOVIES",
    "potions":    "🧪  POTIONS",
    "spells":     "✨  SPELLS",
}
SUBS = {
    "books":      lambda i: i["fields"].get("Author",""),
    "characters": lambda i: i["fields"].get("House",""),
    "houses":     lambda i: i["fields"].get("Traits","")[:30]+"…",
    "movies":     lambda i: i["fields"].get("Year","") + "  ·  " + i["fields"].get("Runtime",""),
    "potions":    lambda i: i["fields"].get("Type",""),
    "spells":     lambda i: i["fields"].get("Category",""),
}


# ─────────────────────────────────────────────────────────────────────────────
class HarryPotterExplorer:

    IMG_W = 270
    IMG_H = 230

    def __init__(self, root):
        self.root = root
        self.root.title("⚡  Harry Potter Explorer")
        self.root.geometry("1400x840")
        self.root.minsize(1100, 680)
        self.root.configure(bg=C["bg_void"])

        self.current_cat    = None
        self.current_data   = []
        self.current_item   = None
        self._search_map    = []   # [(cat, item), …] for search results
        self.favourites     = []
        self._img_cache     = {}   # path → PhotoImage  (keep refs alive!)

        self._load_favs()
        self._build_ui()


    def _build_ui(self):
        self._mk_header()
        self._mk_main()
        self._mk_statusbar()
        self._refresh_fav_list()

    def _mk_header(self):
        h = tk.Frame(self.root, bg=C["bg_panel"])
        h.pack(fill=tk.X)

        tk.Frame(h, bg=C["gold_dim"], height=1).pack(fill=tk.X, side=tk.BOTTOM)

        left = tk.Frame(h, bg=C["bg_panel"], pady=8)
        left.pack(side=tk.LEFT, padx=16)
        tk.Label(left, text="⚡  HARRY POTTER EXPLORER",
                 font=("Georgia", 18, "bold"), fg=C["gold"],
                 bg=C["bg_panel"]).pack(anchor="w")
        tk.Label(left, text="W I Z A R D I N G   W O R L D   D A T A B A S E",
                 font=("Helvetica", 7), fg=C["text_dim"],
                 bg=C["bg_panel"]).pack(anchor="w")

        right = tk.Frame(h, bg=C["bg_panel"], pady=8)
        right.pack(side=tk.RIGHT, padx=16)

        self.search_var = tk.StringVar()
        e = tk.Entry(right, textvariable=self.search_var,
                     font=FONT_ITEM, bg=C["bg_card"], fg=C["text_br"],
                     insertbackground=C["gold"], relief="flat",
                     highlightthickness=1, highlightcolor=C["gold_dim"],
                     width=24)
        e.pack(side=tk.LEFT, ipady=5, padx=(0, 6))
        e.bind("<Return>", lambda _: self._do_search())

        self._btn(right, "🔍  Search", self._do_search).pack(side=tk.LEFT)

    def _mk_main(self):
        main = tk.Frame(self.root, bg=C["bg_deep"])
        main.pack(fill=tk.BOTH, expand=True)

        self._mk_sidebar(main)
        self._mk_item_panel(main)
        self._mk_detail_panel(main)

    # Sidebar 
    def _mk_sidebar(self, parent):
        sb = tk.Frame(parent, bg=C["bg_panel"], width=192)
        sb.pack(side=tk.LEFT, fill=tk.Y)
        sb.pack_propagate(False)
        tk.Frame(sb, bg=C["border"], width=1).place(relx=1, rely=0, relheight=1)

        self._label(sb, "BROWSE").pack(anchor="w", padx=14, pady=(14, 4))

        self._cat_btns = {}
        for label, key, accent in CAT_BTNS:
            btn = tk.Button(sb, text=label,
                            font=FONT_CAT,
                            bg=C["bg_panel"], fg=C["text"],
                            activebackground=C["bg_hover"],
                            activeforeground=C["gold"],
                            relief="flat", anchor="w",
                            padx=14, pady=10,
                            cursor="hand2",
                            command=lambda k=key: self._show_cat(k))
            btn.pack(fill=tk.X)
            self._hover(btn, key)
            self._cat_btns[key] = btn

        tk.Frame(sb, bg=C["border"], height=1).pack(fill=tk.X, padx=10, pady=10)
        self._label(sb, "⭐  FAVOURITES").pack(anchor="w", padx=14, pady=(0, 4))

        ff = tk.Frame(sb, bg=C["bg_panel"])
        ff.pack(fill=tk.BOTH, expand=True)
        fsb = tk.Scrollbar(ff, width=5, bg=C["bg_panel"])
        fsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.fav_box = tk.Listbox(ff, font=("Helvetica", 9),
                                   bg=C["bg_panel"], fg=C["text_dim"],
                                   selectbackground=C["bg_hover"],
                                   selectforeground=C["text_br"],
                                   relief="flat", borderwidth=0,
                                   activestyle="none",
                                   yscrollcommand=fsb.set)
        self.fav_box.pack(fill=tk.BOTH, expand=True)
        fsb.config(command=self.fav_box.yview)
        self.fav_box.bind("<Double-Button-1>", self._view_fav)

        fb = tk.Frame(sb, bg=C["bg_panel"])
        fb.pack(fill=tk.X, padx=10, pady=(2, 10))
        self._btn(fb, "View",   self._view_fav,   w=6).pack(side=tk.LEFT, padx=2)
        self._btn(fb, "Remove", self._remove_fav, w=8,
                  bg="#3a1010").pack(side=tk.LEFT, padx=2)

    # Item list panel 
    def _mk_item_panel(self, parent):
        panel = tk.Frame(parent, bg=C["bg_deep"], width=268)
        panel.pack(side=tk.LEFT, fill=tk.Y)
        panel.pack_propagate(False)
        tk.Frame(panel, bg=C["border"], width=1).place(relx=1, rely=0, relheight=1)

        # Header strip
        hdr = tk.Frame(panel, bg=C["bg_panel"], pady=10)
        hdr.pack(fill=tk.X)
        self.ip_title = tk.Label(hdr, text="SELECT A CATEGORY",
                                  font=FONT_CAT, fg=C["gold"],
                                  bg=C["bg_panel"], padx=14)
        self.ip_title.pack(anchor="w")
        self.ip_count = tk.Label(hdr, text="—",
                                  font=FONT_STATUS, fg=C["text_dim"],
                                  bg=C["bg_panel"], padx=14)
        self.ip_count.pack(anchor="w")
        tk.Frame(hdr, bg=C["border"], height=1).pack(fill=tk.X, pady=(8, 0))

        # Scrollable list
        lf = tk.Frame(panel, bg=C["bg_deep"])
        lf.pack(fill=tk.BOTH, expand=True)
        isb = tk.Scrollbar(lf, width=5)
        isb.pack(side=tk.RIGHT, fill=tk.Y)
        self.item_box = tk.Listbox(lf, font=FONT_ITEM,
                                    bg=C["bg_deep"], fg=C["text_br"],
                                    selectbackground=C["bg_card"],
                                    selectforeground=C["gold"],
                                    relief="flat", borderwidth=0,
                                    activestyle="none",
                                    yscrollcommand=isb.set)
        self.item_box.pack(fill=tk.BOTH, expand=True)
        isb.config(command=self.item_box.yview)
        self.item_box.bind("<<ListboxSelect>>", self._on_select)

    # Detail panel 
    def _mk_detail_panel(self, parent):
        panel = tk.Frame(parent, bg=C["bg_deep"])
        panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Welcome screen 
        self.welcome_frame = tk.Frame(panel, bg=C["bg_deep"])
        self.welcome_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        tk.Label(self.welcome_frame, text="⚡",
                 font=("Georgia", 64), fg=C["gold_dim"],
                 bg=C["bg_deep"]).pack(pady=(120, 8))
        tk.Label(self.welcome_frame, text="Welcome, Wizard",
                 font=("Georgia", 16, "bold"), fg=C["gold_dim"],
                 bg=C["bg_deep"]).pack()
        tk.Label(self.welcome_frame,
                 text="Choose a category on the left, then click any item.",
                 font=FONT_ITEM, fg=C["text_dim"],
                 bg=C["bg_deep"]).pack(pady=6)

        # Actual detail content (hidden until selection)
        self.detail_frame = tk.Frame(panel, bg=C["bg_deep"])
        # placed on first selection

        # Detail header 
        dh = tk.Frame(self.detail_frame, bg=C["bg_panel"])
        dh.pack(fill=tk.X)
        tk.Frame(dh, bg=C["gold_dim"], height=1).pack(fill=tk.X, side=tk.BOTTOM)

        left_dh = tk.Frame(dh, bg=C["bg_panel"], pady=10)
        left_dh.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=14)

        self.det_icon = tk.Label(left_dh, text="🧙",
                                  font=("Georgia", 22), fg=C["gold"],
                                  bg=C["bg_panel"])
        self.det_icon.pack(side=tk.LEFT, padx=(0, 10))

        name_wrap = tk.Frame(left_dh, bg=C["bg_panel"])
        name_wrap.pack(side=tk.LEFT)
        self.det_name = tk.Label(name_wrap, text="—",
                                  font=("Georgia", 14, "bold"),
                                  fg=C["gold_lt"], bg=C["bg_panel"], anchor="w")
        self.det_name.pack(anchor="w")
        self.det_badge = tk.Label(name_wrap, text="—",
                                   font=("Helvetica", 8, "bold"),
                                   fg=C["text_dim"], bg=C["bg_panel"], anchor="w")
        self.det_badge.pack(anchor="w")

        right_dh = tk.Frame(dh, bg=C["bg_panel"], pady=10)
        right_dh.pack(side=tk.RIGHT, padx=14)
        self.fav_btn = self._btn(right_dh, "☆ Save", self._toggle_fav)
        self.fav_btn.pack(side=tk.LEFT, padx=4)

        # Image 
        body = tk.Frame(self.detail_frame, bg=C["bg_deep"])
        body.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        # Image pane
        img_pane = tk.Frame(body, bg=C["bg_card"],
                             width=self.IMG_W + 18)
        img_pane.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 8))
        img_pane.pack_propagate(False)

        self.img_lbl = tk.Label(img_pane, text="📷\n\nNo Image",
                                 font=("Helvetica", 10),
                                 bg=C["bg_card"], fg=C["text_dim"],
                                 justify=tk.CENTER)
        self.img_lbl.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

        # Right side: scrollable fields  +  AI panel
        right_side = tk.Frame(body, bg=C["bg_deep"])
        right_side.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Fields (scrollable canvas)
        fields_wrap = tk.Frame(right_side, bg=C["bg_deep"])
        fields_wrap.pack(fill=tk.BOTH, expand=True)

        fc_sb = tk.Scrollbar(fields_wrap, width=5)
        fc_sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.fields_canvas = tk.Canvas(fields_wrap, bg=C["bg_deep"],
                                        yscrollcommand=fc_sb.set,
                                        highlightthickness=0)
        self.fields_canvas.pack(fill=tk.BOTH, expand=True)
        fc_sb.config(command=self.fields_canvas.yview)

        self.fields_inner = tk.Frame(self.fields_canvas, bg=C["bg_deep"])
        self._fc_win = self.fields_canvas.create_window(
            (0, 0), window=self.fields_inner, anchor="nw")
        self.fields_inner.bind("<Configure>",
            lambda _: self.fields_canvas.configure(
                scrollregion=self.fields_canvas.bbox("all")))
        self.fields_canvas.bind("<Configure>",
            lambda e: self.fields_canvas.itemconfig(
                self._fc_win, width=e.width))
        # Mousewheel on fields
        self.fields_canvas.bind("<MouseWheel>",
            lambda e: self.fields_canvas.yview_scroll(
                int(-1*(e.delta/120)), "units"))

    def _mk_statusbar(self):
        bar = tk.Frame(self.root, bg=C["bg_panel"], pady=4)
        bar.pack(fill=tk.X, side=tk.BOTTOM)
        tk.Frame(bar, bg=C["border"], height=1).place(relx=0, rely=0, relwidth=1)
        self.status_lbl = tk.Label(bar, text="⚡  Ready",
                                    font=FONT_STATUS, fg=C["green"],
                                    bg=C["bg_panel"], padx=10)
        self.status_lbl.pack(side=tk.LEFT)
        tk.Label(bar, text="Harry Potter Explorer",
                 font=FONT_STATUS, fg=C["text_dim"],
                 bg=C["bg_panel"]).pack(side=tk.RIGHT, padx=10)

    def _btn(self, parent, text, cmd, w=None, bg=None):
        b = tk.Button(parent, text=text, command=cmd,
                      font=("Helvetica", 8, "bold"),
                      bg=bg or C["bg_hover"], fg=C["gold"],
                      activebackground=C["bg_card"],
                      activeforeground=C["gold_lt"],
                      relief="flat", padx=10, pady=5,
                      cursor="hand2", width=w)
        return b

    def _label(self, parent, text):
        return tk.Label(parent, text=text, font=FONT_LABEL,
                        fg=C["text_dim"], bg=C["bg_panel"])

    def _hover(self, btn, key):
        btn.bind("<Enter>",
                 lambda _, b=btn: b.config(bg=C["bg_hover"], fg=C["gold"]))
        btn.bind("<Leave>",
                 lambda _, b=btn, k=key:
                     b.config(bg=C["bg_hover"] if self.current_cat == k
                              else C["bg_panel"],
                              fg=C["gold"] if self.current_cat == k
                              else C["text"]))

    def _set_status(self, msg):
        self.status_lbl.config(text=f"⚡  {msg}")

    # Display the categories
    def _show_cat(self, key):
        self.current_cat  = key
        self.current_data = DB[key]
        self._search_map  = []

        # Sidebar highlight
        for k, b in self._cat_btns.items():
            b.config(bg=C["bg_hover"] if k == key else C["bg_panel"],
                     fg=C["gold"]    if k == key else C["text"])

        self.ip_title.config(text=TITLES[key])
        self.ip_count.config(text=f"{len(self.current_data)} entries")

        self.item_box.delete(0, tk.END)
        sub_fn = SUBS.get(key, lambda i: "")
        for item in self.current_data:
            sub = sub_fn(item)
            line = f"  {item['icon']}  {item['name']}"
            if sub:
                line += f"  —  {sub}"
            self.item_box.insert(tk.END, line)

        # Restore normal selection handler
        self.item_box.bind("<<ListboxSelect>>", self._on_select)

        self._hide_detail()
        self._set_status(f"Showing {len(self.current_data)} {key}")

    # Selection of items
    def _on_select(self, _e=None):
        sel = self.item_box.curselection()
        if not sel or not self.current_data:
            return
        if self._search_map:
            cat, item = self._search_map[sel[0]]
            self.current_cat  = cat
            self.current_item = item
        else:
            self.current_item = self.current_data[sel[0]]
        self._render_detail(self.current_item)

    def _render_detail(self, item):
        # Show detail pane
        self.welcome_frame.place_forget()
        self.detail_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Header
        self.det_icon.config(text=item["icon"])
        self.det_name.config(text=item["name"])
        self.det_badge.config(text=item["badge"])

        in_fav = any(f["name"] == item["name"] for f in self.favourites)
        self.fav_btn.config(text="★ Saved" if in_fav else "☆ Save",
                             fg=C["gold"] if in_fav else C["text_dim"])

        # Image
        self._show_image(item.get("image", ""))

        # Fields grid
        for w in self.fields_inner.winfo_children():
            w.destroy()

        col = 0
        row = 0
        for k, v in item["fields"].items():
            is_long = (len(str(v)) > 55 or
                       k in ("Synopsis","Description","Skills","Notable Members",
                             "Traits","Users","Known Users","Effect","Notable"))
            cs = 2 if is_long else 1

            card = tk.Frame(self.fields_inner, bg=C["bg_card"],
                             padx=10, pady=8)
            card.grid(row=row, column=0 if is_long else col,
                      columnspan=cs, sticky="nsew", padx=3, pady=3)

            tk.Label(card, text=k.upper(), font=FONT_LABEL,
                     fg=C["text_dim"], bg=C["bg_card"],
                     anchor="w").pack(anchor="w")
            tk.Label(card, text=v, font=FONT_VALUE,
                     fg=C["text_br"], bg=C["bg_card"],
                     anchor="w", wraplength=310,
                     justify=tk.LEFT).pack(anchor="w")

            if is_long:
                col = 0
                row += 1
            else:
                col += 1
                if col >= 2:
                    col = 0
                    row += 1

        self.fields_inner.columnconfigure(0, weight=1)
        self.fields_inner.columnconfigure(1, weight=1)
        self.fields_inner.update_idletasks()
        self.fields_canvas.configure(
            scrollregion=self.fields_canvas.bbox("all"))
        self.fields_canvas.yview_moveto(0)

        self._set_status(f"Viewing: {item['name']}")

    def _hide_detail(self):
        self.current_item = None
        self.detail_frame.place_forget()
        self.welcome_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Loading the image
    def _show_image(self, path):
        if not path:
            self.img_lbl.config(image="", text="📷\n\nNo Image")
            return
        if not PIL_OK:
            self.img_lbl.config(image="",
                                 text=f"📷\n\n(Pillow not installed)\n{os.path.basename(path)}")
            return
        if not os.path.exists(path):
            self.img_lbl.config(image="",
                                 text=f"📷\n\nFile not found:\n{os.path.basename(path)}")
            return
        try:
            if path not in self._img_cache:
                img = Image.open(path)
                # Handle transparency
                if img.mode in ("RGBA","LA","P"):
                    bg = Image.new("RGBA", img.size, (20, 24, 48, 255))
                    img = img.convert("RGBA")
                    bg.paste(img, mask=img.split()[3])
                    img = bg.convert("RGB")
                else:
                    img = img.convert("RGB")

                img.thumbnail((self.IMG_W, self.IMG_H), Image.LANCZOS)
                self._img_cache[path] = ImageTk.PhotoImage(img)

            photo = self._img_cache[path]
            self.img_lbl.config(image=photo, text="")
            self.img_lbl.image = photo   # keep reference

        except Exception as exc:
            self.img_lbl.config(image="",
                                 text=f"📷  Cannot load:\n{os.path.basename(path)}\n({exc})")

    # Search bar to search for the specific item
    def _do_search(self):
        q = self.search_var.get().strip().lower()
        if not q:
            return

        results = []
        for key, items in DB.items():
            for item in items:
                if q in item["name"].lower():
                    results.append((key, item))

        self.current_cat  = "search"
        self.current_data = [r[1] for r in results]
        self._search_map  = results

        for b in self._cat_btns.values():
            b.config(bg=C["bg_panel"], fg=C["text"])

        self.ip_title.config(text=f"🔍  \"{q}\"")
        self.ip_count.config(text=f"{len(results)} result(s)")

        self.item_box.delete(0, tk.END)
        for cat, item in results:
            sub = SUBS.get(cat, lambda i: "")(item)
            line = f"  {item['icon']}  {item['name']}"
            if sub:
                line += f"  —  {sub}"
            self.item_box.insert(tk.END, line)

        # Rebind selection to use search map
        self.item_box.bind("<<ListboxSelect>>", self._on_select)

        self._hide_detail()
        self._set_status(f"Found {len(results)} result(s) for \"{q}\"")

    # Favorites section
    def _toggle_fav(self):
        if not self.current_item:
            return
        name = self.current_item["name"]
        idx  = next((i for i, f in enumerate(self.favourites)
                      if f["name"] == name), -1)
        if idx >= 0:
            self.favourites.pop(idx)
            self.fav_btn.config(text="☆ Save", fg=C["text_dim"])
            self._set_status(f"Removed '{name}' from favourites")
        else:
            self.favourites.append({
                "name": name,
                "icon": self.current_item["icon"],
                "cat":  self.current_cat,
                "item": self.current_item,
            })
            self.fav_btn.config(text="★ Saved", fg=C["gold"])
            self._set_status(f"Saved '{name}' to favourites")
        self._save_favs()
        self._refresh_fav_list()

    def _view_fav(self, _e=None):
        sel = self.fav_box.curselection()
        if not sel:
            return
        fav = self.favourites[sel[0]]
        # Switch to the right category
        if fav["cat"] in DB:
            self._show_cat(fav["cat"])
            for i, item in enumerate(self.current_data):
                if item["name"] == fav["name"]:
                    self.item_box.selection_clear(0, tk.END)
                    self.item_box.selection_set(i)
                    self.item_box.see(i)
                    break
        self.current_item = fav["item"]
        self._render_detail(fav["item"])

    def _remove_fav(self, _e=None):
        sel = self.fav_box.curselection()
        if not sel:
            return
        removed = self.favourites.pop(sel[0])
        self._save_favs()
        self._refresh_fav_list()
        self._set_status(f"Removed '{removed['name']}' from favourites")

    def _refresh_fav_list(self):
        self.fav_box.delete(0, tk.END)
        for f in self.favourites:
            self.fav_box.insert(tk.END, f"  {f['icon']}  {f['name']}")

    def _save_favs(self):
        try:
            with open("hp_favourites.json", "w") as fp:
                json.dump(self.favourites, fp, indent=2)
        except Exception:
            pass

    def _load_favs(self):
        try:
            with open("hp_favourites.json") as fp:
                self.favourites = json.load(fp)
        except Exception:
            self.favourites = []

def main():
    root = tk.Tk()
    HarryPotterExplorer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
