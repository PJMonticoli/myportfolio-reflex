import reflex as rx
from reflexapp.components.link_button import link_button
from reflexapp.components.title import title
import reflexapp.views.constants as constants
import reflexapp.routes.routes as routes
def index_links() -> rx.Component:
    return rx.vstack(
            title("My Social Networks"),
            link_button(
                "LinkedIn",
                "There you will find my cv.",
                "linkedin.svg", 
                constants.LINKEDIN_URL
                ),
            link_button(
                "GitHub", 
                "My GitHub profile and some repositories that I've been working on.",
                "github.svg", 
                constants.GITHUB_URL
                ),
            link_button(
                "Instagram", 
                "My instagram profile.",
                "instagram.svg", 
                constants.INSTAGRAM_URL
                ),
            title("Personal Projects"),
            link_button(
                "Full-Stack project", 
                "Developed with Angular and Supabase.",
                "github.svg", 
                routes.Route.PROJECTS.value,
                is_external = False
                ),
            link_button(
                "Front-End portfolio", 
                "Developed with Reflex(Python).",
                "github.svg", 
                constants.PORTFOLIO_GITHUB
                ),
            link_button(
                "Front-End Ecommerce", 
                "Developed with Angular.",
                "github.svg", 
                constants.REPO_GITHUBFRONT
                ),
            link_button(
                "Back-End Ecommerce", 
                "Developed with NodeJs(Framework ExpressJs).",
                "github.svg", 
                constants.REPO_GITHUBBACK
                ),
            title("Contact"),
            link_button(
                "Linktr.ee", 
                "How to reach me",
                "contacto.svg", 
                constants.LINKTREE
                ),
            width="100%",
            align_items="start"
        )
