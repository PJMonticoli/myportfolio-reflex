import reflex as rx
from reflexapp.components.link_button import link_button
from reflexapp.components.title import title
import reflexapp.views.constants as constants
import reflexapp.routes.routes as routes


def index_links() -> rx.Component:
    return rx.vstack(
        title("Resume"),
        link_button(
            "Take a look at my resume",
            "Includes programming education and English certifications.",
            "/resume.svg",
            routes.Route.RESUME.value,
            is_external=False
        ),
        
        title("Projects"),
        link_button(
            "GitHub Repositories",
            "Projects developed with Angular, Node.js, Supabase, Reflex, Python, and more.",
            "/github.svg",
            routes.Route.PROJECTS.value,
            is_external=False
        ),

        title("My Social Networks"),
        link_button(
            "LinkedIn",
            "Connect with me on LinkedIn for more details about my work.",
            "/linkedin.svg",
            constants.LINKEDIN_URL
        ),
        link_button(
            "GitHub",
            "Explore all my repositories and GitHub activity.",
            "/github.svg",
            constants.GITHUB_URL
        ),

        title("Contact"),
        link_button(
            "Contact me",
            "Feel free to reach out via email.",
            "/contacto.svg",
            constants.CONTACT
        ),
        width="100%",
        align_items="start"
    )
