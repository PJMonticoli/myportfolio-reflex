import reflex as rx
from reflexapp.components.link_button import link_button
from reflexapp.components.title import title
import reflexapp.views.constants as constants


def projects_links() -> rx.Component:
    return rx.vstack(
        title("GitHub Repositories"),
        link_button(
            "Chocolate Shop - Frontend",
            "E-commerce UI developed in Angular for managing a chocolate store.",
            "/angular.svg",
            constants.REPO_GITHUBFRONT
        ),
        link_button(
            "Chocolate Shop - Backend",
            "RESTful API built with Node.js and Express.js for product and order management.",
            "/node.svg",
            constants.REPO_GITHUBBACK
        ),
        link_button(
            "Pallet Management System",
            "Logistics system built in .NET Framework for managing pallet operations: movement tracking, real-time inventory, automated reports, and client/transporter management.",
            "https://cdn.simpleicons.org/dotnet",  
            constants.DOTNET_GITHUB  
        ),
        link_button(
            "Developer Portfolio",
            "Personal portfolio built with Astro to showcase projects and experience.",
            "/astro.svg",
            constants.PORTFOLIO_GITHUB
        ),
        link_button(
            "Full-Stack App with Supabase",
            "Web app combining Angular frontend and Supabase backend for real-time data.",
            "/angular.svg",
            constants.SUPABASE_GITHUB
        ),
        title("🔥 My GitHub Stats"),
        width="100%",
        align_items="start"
    )
