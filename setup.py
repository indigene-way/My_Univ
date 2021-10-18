"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "UnivClasser.",
    version = "1.0.0",
    description = "UnivClasser Sys permet le classement et le ttri des universités, 2020-2021 G.Halim...",
    executables = [Executable("main.py")]
)