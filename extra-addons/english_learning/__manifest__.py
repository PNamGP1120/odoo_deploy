{
    "name": "English Learning App",
    "version": "17.0.1.0.0",
    "category": "Education",
    "summary": "An app for learning English vocabulary and lessons",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/vocabulary_views.xml",
        "views/lesson_views.xml",
        "views/quiz_views.xml",
        "views/user_progress_views.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}