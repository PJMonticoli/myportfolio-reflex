import reflex as rx
from  reflexapp.components.navbar import navbar
from reflexapp.views.header import header
from reflexapp.views.links import links
from reflexapp.components.footer import footer
import reflexapp.styles.styles as styles
from reflexapp.styles.styles import Size
class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
            navbar(),
            rx.center(
                rx.vstack(
                    header(),
                    links(),
                    footer(),
                    max_width= styles.MAX_WIDTH,
                    width="100%",
                    align="center",
                    margin_y=Size.BIG.value,
                    padding= Size.BIG.value
                )
            ),
    )

app = rx.App(
    style = styles.BASE_STYLE,
    stylesheets = styles.STYLESSHEETS
) 
app.add_page(
    index,
    title="olpabdev | Programmer")
app._compile()