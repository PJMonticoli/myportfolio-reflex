import reflex as rx
from reflexapp.components.link_button import link_button
from reflexapp.components.title import title
import reflexapp.views.constants as constants

def projects_links() -> rx.Component:
    return rx.vstack(
            title("GitHub Repositories"),
            link_button(
                "Full-Stack project", 
                "Developed with Angular and Supabase.",
                "/github.svg", 
                constants.SUPABASE_GITHUB
                ),
            link_button(
                "My portfolio website", 
                "Developed with Reflex(Python).",
                "/github.svg", 
                constants.PORTFOLIO_GITHUB
                ),
            link_button(
                "Ecommerce Front-End", 
                "Developed with Framework Angular.",
                "/github.svg", 
                constants.REPO_GITHUBFRONT
                ),
            link_button(
                "Ecommerce Back-End", 
                "Developed with NodeJs(Framework ExpressJs).",
                "/github.svg", 
                constants.REPO_GITHUBBACK
                ),
            width="100%",
            align_items="start"
        )
