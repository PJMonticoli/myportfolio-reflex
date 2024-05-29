import reflex as rx
import reflexapp.styles.styles as styles


def title(text : str) -> rx.Component:
    return rx.heading(text,size="6",style=styles.title_styles)