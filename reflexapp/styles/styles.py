from enum import Enum
import reflex as rx
from .colors import Colors as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
# Constantes
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    SMALL= "0.5em"
    MEDIUM= "0.95em"
    DEFAULT= "1.2em"
    LARGE = "1.5em"
    BIG= "2em"

# Styles

BASE_STYLE = {
    "font_family" : Font.DEFAULT.value,
    "background_color" : Color.BACKGROUND.value,
    rx.button : {
        "width" : "100%",
        "height" : "100%",
        "padding" : Size.SMALL.value,
        "border_radius" : Size.DEFAULT.value,
        "color" : TextColor.HEADER.value,
        "background_color" : Color.CONTENT.value,
        "cursor" : "pointer", 
        "white_space":"normal", 
        "text_align" : "start",
        "_hover" : {
          "background_color" : Color.SECONDARY.value,
          "cursor" : "pointer"  
        }
    },
    rx.link: {
        "text_decoration" : "none",
        "_hover" : {}
    }
}

button_title_style = dict(
    font_size = Size.DEFAULT.value,
    font_family = Font.TITLE.value
)
navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size = Size.DEFAULT.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value,
    font_family = Font.DEFAULT.value,
)

title_styles = dict(
    size="lg",
    width ="100%",
    font_family = Font.DEFAULT.value,
    padding_top = Size.DEFAULT.value,
    color= TextColor.WHITE.value,
)

STYLESSHEETS = [
    "https://fonts.googleapis.com/css?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css?family=Comfortaa:wght@500&display=swap"
]