import reflex as rx
import reflexapp.styles.styles as Styles
import reflexapp.routes.routes as router
from reflexapp.styles.styles import Size as Size
from reflexapp.styles.colors import TextColor as TextColor
from reflexapp.styles.colors import Colors as Colors


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.flex(
                rx.image(src="/logo.jpg", width="30px",
                         height="30px", border_radius="50%", margin_right="5px"),
                rx.text.strong("pmonticoli", color=Colors.PRIMARY.value,
                               style=Styles.navbar_title_style)
            ),
            href=router.Route.INDEX.value),
        position="sticky",
        bg=Colors.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )
