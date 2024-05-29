import reflex as rx
from reflexapp.styles.colors import TextColor as TextColor
from reflexapp.styles.colors import Colors as Colors
from reflexapp.styles.styles import Size as Size


def resume() -> rx.Component:
    return rx.vstack(
            rx.image(
            src="/resume.png",
            width="100%",  
            height="auto",  
            alt="resume"
        ),
            rx.image(
            src="/cambridge.png",
            width="100%",  
            height="auto",  
            alt="cambridge" 
            )  
    ) 

    
 

