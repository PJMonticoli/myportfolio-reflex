import reflex as rx
import datetime
from reflexapp.styles.colors import TextColor as TextColor
from reflexapp.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png", 
            width="80px", 
            height="80px", 
            alt="logotipo olbapdev",
            border_radius="50%"),
            rx.text(f"© 2024-{datetime.date.today().year} Web-Site Developed by Pablo Monticoli", 
                width="100%", 
                text_align="center"),
        color=TextColor.FOOTER.value,
        margin=Size.SMALL.value,
        padding=Size.SMALL.value,
        align_items="center",  
        width="100%" 
    )
