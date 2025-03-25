from enum import Enum
import reflex as rx
from .colors import Colors as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
# Constantes
MAX_WIDTH = "800px"
MOBILE_MAX_WIDTH = "95%"

def responsive_container(*children, **kwargs):
    return rx.box(
        rx.center(
            rx.vstack(
                *children,
                max_width=MAX_WIDTH,
                width=["100%", "100%", "100%"],
                spacing="4",
                align="center",
                **kwargs
            ),
            width="100%"
        ),
        padding_x=["1em", "2em", "3em"]
    )

# Sizes


class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.95em"
    DEFAULT = "1.2em"
    LARGE = "1.5em"
    BIG = "2em"

# Styles


BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": "12px",
        "color": TextColor.WHITE.value,
        "background_color": Color.CONTENT.value,
        "transition": "all 0.3s ease",
        "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
        "cursor": "pointer",
        "white_space": "normal",
        "text_align": "start",
        "position": "relative",
        "overflow": "hidden",
        "_hover": {
            "background_color": Color.SECONDARY.value,
            "transform": "translateY(-3px)",
            "box_shadow": "0 6px 8px rgba(0, 0, 0, 0.2)",
            "cursor": "pointer",
            ":before": {
                "content": '""',
                "position": "absolute",
                "top": "0",
                "left": "-100%",
                "width": "100%",
                "height": "100%",
                "background": "linear-gradient(120deg, transparent, rgba(255,255,255,0.1), transparent)",
                "transition": "all 0.5s",
            },
            ":hover:before": {
                "left": "100%",
            }
        }
    }
}

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    font_family=Font.TITLE.value
)
navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size=Size.DEFAULT.value
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    font_family=Font.DEFAULT.value,
)

title_styles = dict(
    size="lg",
    width="100%",
    font_family=Font.DEFAULT.value,
    padding_top=Size.DEFAULT.value,
    color=TextColor.WHITE.value,
)

STYLESSHEETS = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
]


notranslate = dict(class_name="notranslate")
