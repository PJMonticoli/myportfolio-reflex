import reflex as rx
import reflexapp.views.constants as constants

def mystats():
    return rx.vstack(
        rx.image(src=constants.GITHUB_CONTRIBUTIONS, alt="Total Contributions", width="100%"),
        rx.image(src=constants.GITHUB_COMMITS, alt="GitHub Stats", width="100%"),
        rx.image(src=constants.GITHUB_LANGUAGES, alt="Top Languages", width="100%"),
    )
