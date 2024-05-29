import reflex as rx
from  reflexapp.components.navbar import navbar
from reflexapp.views.header import header
from reflexapp.views.resume import resume
from reflexapp.components.footer import footer
import reflexapp.styles.styles as styles
from reflexapp.styles.styles import Size
import reflexapp.utils as utils
from reflexapp.routes.routes import Route
@rx.page(
  route = Route.RESUME.value
)

def curriculum() -> rx.Component:
    return rx.box(
            navbar(),
            rx.center(
                rx.vstack(
                    header(),
                    resume(),
                    footer(),
                    max_width= styles.MAX_WIDTH,
                    width="100%",
                    align="center",
                    margin_y=Size.BIG.value,
                    padding= Size.BIG.value
                )
            ),
    )

