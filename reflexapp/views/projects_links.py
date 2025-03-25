import reflex as rx
from reflexapp.components.link_button import link_button
from reflexapp.components.title import title
import reflexapp.views.constants as constants


def projects_links() -> rx.Component:
    return rx.vstack(
        title("GitHub Repositories"),

        # Chocolate Shop - Frontend
        link_button(
            "Chocolate Shop - Frontend",
            "E-commerce UI developed in Angular for managing a chocolate store.",
            "/angular.svg",
            constants.REPO_GITHUBFRONT
        ),
        rx.image(src="/ecommerce.webp", width="100%", border_radius="12px", margin_bottom="1em"),

        # Chocolate Shop - Backend
        link_button(
            "Chocolate Shop - Backend",
            "RESTful API built with Node.js and Express.js for product and order management.",
            "/node.svg",
            constants.REPO_GITHUBBACK
        ),
        rx.image(src="/backendproject.webp", width="100%", border_radius="12px", margin_bottom="1em"),

        # Pallet Management System (.NET)
        link_button(
            "Pallet Management System",
            "Logistics system built in .NET Framework for managing pallet operations: movement tracking, real-time inventory, automated reports, and client/transporter management.",
            "https://cdn.simpleicons.org/dotnet",
            constants.DOTNET_GITHUB
        ),
        rx.image(src="/netproject.webp", width="100%", border_radius="12px", margin_bottom="1em"),

        # Portfolio
        link_button(
            "Developer Portfolio",
            "Personal portfolio built with Astro to showcase projects and experience.",
            "/astro.svg",
            constants.PORTFOLIO_GITHUB
        ),
        rx.image(src="/portfolio.webp", width="100%", border_radius="12px", margin_bottom="1em"),

        # Full-Stack App with Supabase
        link_button(
            "Full-Stack App with Supabase",
            "Web app combining Angular frontend and Supabase backend for real-time data.",
            "/angular.svg",
            constants.SUPABASE_GITHUB
        ),
        rx.image(src="/fullstackproject.webp", width="100%", border_radius="12px", margin_bottom="1em"),

        title("🔥 My GitHub Stats"),
        width="100%",
        align_items="start"
    )
