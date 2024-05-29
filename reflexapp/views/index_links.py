import reflex as rx
from reflexapp.components.link_button import link_button
from reflexapp.components.title import title
import reflexapp.views.constants as constants
import reflexapp.routes.routes as routes
def index_links() -> rx.Component:
    return rx.vstack(
            title("Personal Projects"),
            link_button(
                "GitHub Repositories", 
                "HTML, CSS, JS, Angular, SQL, Supabase, Reflex and Python.",
                "/github.svg", 
                routes.Route.PROJECTS.value,
                is_external = False
                ),
            title("My Social Networks"),
            link_button(
                "LinkedIn",
                "There you will find my cv.",
                "/linkedin.svg", 
                constants.LINKEDIN_URL
                ),
            link_button(
                "GitHub", 
                "Some repositories that I've been working on.",
                "/github.svg", 
                constants.GITHUB_URL
                ),
            link_button(
                "Instagram", 
                "My instagram profile.",
                "/instagram.svg", 
                constants.INSTAGRAM_URL
                ),

            title("Contact"),
            link_button(
                "Linktr.ee", 
                "How to reach me.",
                "/contacto.svg", 
                constants.LINKTREE
                ),
            width="100%",
            align_items="start"
        )
