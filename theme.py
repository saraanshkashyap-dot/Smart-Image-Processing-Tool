# ==========================================
# Theme Module
# ==========================================

themes = {

    "Light": {

        "bg": "#f2f2f2",
        "panel": "#ffffff",
        "canvas": "#eeeeee",
        "text": "#000000",
        "status": "#dddddd"

    },


    "Dark": {

        "bg": "#202020",
        "panel": "#303030",
        "canvas": "#111111",
        "text": "#ffffff",
        "status": "#404040"

    }

}


def get_theme(name):

    return themes.get(
        name,
        themes["Light"]
    )


def get_theme_names():

    return list(
        themes.keys()
    )