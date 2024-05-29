import reflex as rx

# General
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='en'")

preview = "https://pmonticoliportfolio.reflex.run/logo.png"
_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@PMonticoli"}
]


# Index
index_title="olpabdev | Programmer"
index_descripcion = "Hi, my name is Pablo Montícoli and I'm a Full-Stack Developer"

index_meta = [
    {"name" : "og:title", "content" : index_title},
    {"name" : "og:description", "content" : index_descripcion}
]
index_meta.extend(_meta)


# Projects
projects_title="olpabdev | Programmer"
projects_descripcion = "There you will find some projects that I've been working on"

projects_meta = [
    {"name" : "og:title", "content" : projects_title},
    {"name" : "og:description", "content" : projects_descripcion}
]
projects_meta.extend(_meta)