from setuptools import setup

version = __import__("src").get_version()

setup(
    name="django_xsessions",
    version="0.1",
    description="Middleware that offers session sharing across multiple domains (using the same session backend obviously). Can be used to allow single sign-on across multiple websites.",
    author="Kalinin Mitko",
    author_email="kalinin.mitko@gmail.com",
    url="https://github.com/null-none/django-xsessions",
    license="MIT",
    packages=["xsession"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires=["beautifulsoup4==4.12.3"],
)