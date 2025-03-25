import reflex as rx
from reflexapp.styles.colors import TextColor, Colors
from reflexapp.styles.styles import Size
import reflexapp.routes.routes as router
from reflexapp.views.constants import LINKEDIN_URL
from reflexapp.styles.styles import notranslate


def header(details: bool) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.link(
                rx.avatar(
                    fallback="PM",
                    size="7", 
                    src="/avatar.webp",
                    style={
                        "border-radius": "50%",
                        "border": f"4px solid {Colors.PRIMARY.value}",
                        "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)"
                    }
                ),
                href=router.Route.INDEX.value
            ),
            rx.vstack(
                rx.heading(
                    "Pablo Javier Montícoli", 
                    size="6",
                    color=TextColor.WHITE.value,
                    style={"letter-spacing": "1px"}
                ),
                rx.link(
                    rx.badge(
                        "Open to Work",
                        variant="surface",
                        color_scheme="violet",
                        radius="large",
                        size="2",
                        class_name=notranslate['class_name'],
                        style={
                            "animation": "pulse 2s infinite",
                            "@keyframes pulse": {
                                "0%": {"transform": "scale(1)"},
                                "50%": {"transform": "scale(1.05)"},
                                "100%": {"transform": "scale(1)"}
                            }
                        }
                    ),
                    href=LINKEDIN_URL,
                    target="_blank"
                )
            ),
            spacing="6",
            align_items="center"
        ),
        rx.cond(
            details,
            rx.box(
                rx.text.strong("Hey, I'm Pablo",
                               color=TextColor.BODY.value, size="6"),
                rx.box(
                    rx.text(
                        "Over 1 year of experience as a ",
                        color=TextColor.BODY.value,
                        display="inline", size="4"
                    ),
                    rx.text(
                        " Full-Stack Developer, graduated from the National Technological University as a Programming Technician. ",
                        color=TextColor.DESCRIPTION.value,
                        display="inline", size="4"
                    ),
                    rx.box(
                        rx.text(
                            "I'm From Córdoba, Argentina 🇦🇷. Specialized in developing unique applications and continuous learning.",
                            color=TextColor.BODY.value,
                            display="inline", size="4"
                        )
                    )
                ),
            )
        ),
        align_items="start",
        width="100%"
    )
