import reflex as rx
from  reflexapp.components.navbar import navbar
from reflexapp.views.header import header
from reflexapp.views.index_links import index_links
from reflexapp.components.footer import footer
import reflexapp.styles.styles as styles
from reflexapp.styles.styles import Size
import reflexapp.utils as utils

@rx.page(
  title= utils.index_title,  
  description=utils.index_descripcion,  
  image=utils.preview,  
  meta=utils.index_meta,  
)

def index() -> rx.Component:
    return rx.box(
            utils.lang(),
            navbar(),
            rx.center(
                rx.vstack(
                    header(details=True),
                    index_links(),
                    footer(),
                    max_width= styles.MAX_WIDTH,
                    width="100%",
                    align="center",
                    margin_y=Size.BIG.value,
                    padding= Size.BIG.value
                )
            ),
    )

