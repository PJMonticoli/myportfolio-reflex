import reflex as rx
from  reflexapp.components.navbar import navbar
from reflexapp.views.header import header
from reflexapp.views.projects_links import projects_links
from reflexapp.components.footer import footer
import reflexapp.styles.styles as styles
from reflexapp.styles.styles import Size
import reflexapp.utils as utils
from reflexapp.routes.routes import Route
@rx.page(
  route = Route.PROJECTS.value,  
  title= utils.projects_title,  
  description=utils.projects_descripcion,  
  image=utils.preview,  
  meta=utils.projects_meta,  
)

def projects() -> rx.Component:
    return rx.box(
            utils.lang(),
            navbar(),
            rx.center(
                rx.vstack(
                    header(),
                    projects_links(),
                    footer(),
                    max_width= styles.MAX_WIDTH,
                    width="100%",
                    align="center",
                    margin_y=Size.BIG.value,
                    padding= Size.BIG.value
                )
            ),
    )

