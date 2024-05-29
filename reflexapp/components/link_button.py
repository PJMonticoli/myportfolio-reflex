import reflex as rx
import reflexapp.styles.styles as styles
from reflexapp.styles.styles import Size

def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.stack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                    alt= title
                ), 
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    margin=0
                ),
                align_items="start",  
                justify_content="start"  
            ),
            width="100%",
            justify_content="start"  
        ),
        href=url,
        is_external=True,
        width="100%"
    )
