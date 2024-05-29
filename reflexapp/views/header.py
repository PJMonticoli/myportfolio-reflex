import reflex as rx
from reflexapp.styles.colors import TextColor as TextColor
from reflexapp.styles.colors import Colors as Colors
from reflexapp.styles.styles import Size as Size

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback="PM", 
                size="6",
                src="/avatar.png",
                style={
                    "border-radius": "50%",
                    "padding": "2px",
                    "border": "3px solid " + Colors.PRIMARY.value
                }
            ),
            rx.vstack(
                rx.heading("Pablo Javier Montícoli", size="6", color=TextColor.WHITE.value),
                rx.text("@PJMonticoli", color=TextColor.WHITE.value)
            ),
            spacing="6",
            align_items="start"
        ),
        rx.text.strong("About me", color=TextColor.BODY.value),
        rx.text("I'm a Full-Stack Programmer, graduated from the National Technological University with experience in:",
                color=TextColor.BODY.value,
                font_size=Size.MEDIUM.value),
        rx.unordered_list(
            rx.list_item("Front-End: HTML, CSS, JavaScript, Angular, Node.js, Reflex.", color=TextColor.BODY.value, font_size=Size.MEDIUM.value),
            rx.list_item(".NET, C#, Java, Python, Supabase, Reflex.", color=TextColor.BODY.value, font_size=Size.MEDIUM.value),
            rx.list_item("Database Management: SQLServer, MySQL, PostgreSQL, MongoDB.", color=TextColor.BODY.value, font_size=Size.MEDIUM.value),
            rx.list_item("SCRUM Methodology (Jira Software).", color=TextColor.BODY.value, font_size=Size.MEDIUM.value),
        ),
        align_items="start",
    )
 

