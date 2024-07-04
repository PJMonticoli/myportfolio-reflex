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
                    size="6",
                    src="/avatar.jpg",
                    style={
                        "border-radius": "50%",
                        "padding": "2px",
                        "border": f"3px solid {Colors.DESCRIPTION.value}"
                    }
                ),
                href=router.Route.INDEX.value
            ),
            rx.vstack(
                rx.heading("Pablo Javier Montícoli", size="6",
                           color=TextColor.WHITE.value),
                rx.link(
                    rx.badge(
                        "Open to Work",
                        variant="solid",
                        color_scheme="violet",
                        radius="large",
                        size="2",
                        class_name=notranslate['class_name']
                    ),
                    href=LINKEDIN_URL,
                    target="_blank"
                )
            ),
            spacing="6",
            align_items="start"
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
                # rx.unordered_list(
                #     rx.list_item(
                #         "Front-End: HTML, CSS, JavaScript, TypeScript, Angular and Reflex.",
                #         color=TextColor.BODY.value, font_size=Size.MEDIUM.value
                #     ),
                #     rx.list_item(
                #         "Back-End: .NET, C#, Java, Python, NodeJs(ExpressJs), Supabase and Reflex.",
                #         color=TextColor.BODY.value, font_size=Size.MEDIUM.value
                #     ),
                #     rx.list_item(
                #         "Database Management: SQLServer, MySQL, PostgreSQL and MongoDB.",
                #         color=TextColor.BODY.value, font_size=Size.MEDIUM.value
                #     ),
                #     rx.list_item(
                #         "Scrum Methodology (Jira Software).",
                #         color=TextColor.BODY.value, font_size=Size.MEDIUM.value
                #     ),
                # )
            )
        ),
        align_items="start",
        width="100%"
    )
