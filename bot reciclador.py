import discord 
import os, random
from discord.ext import commands 
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

# Lista de materiales reciclables (basado en la conversación anterior)
materiales = [
    "Papel",
    "Cartón",
    "Plástico (como botellas PET)",
    "Vidrio",
    "Aluminio (latas)",
    "Acero",
    "Cobre",
    "Baterías",
    "Neumáticos",
    "Aceite usado",
    "Ropa y textiles",
    "Madera",
    "Aparatos electrónicos",
    "Pilas",
    "Latas de conserva",
    "Botellas de vidrio",
    "Periódicos",
    "Revistas",
    "Envases de tetrapak",
    "Metales ferrosos"
]

# Lista de ideas ecológicas usando los materiales (basado en la conversación anterior)
ideas = [
    "**Lámpara decorativa**: Usa botellas de vidrio y botellas PET para crear una lámpara colgante, agregando luces LED recicladas de aparatos electrónicos viejos.",
    "**Organizador de escritorio**: Con cartón y envases de tetrapak, arma un organizador para lápices y papeles, reforzándolo con latas de aluminio como base.",
    "**Juguete para niños**: Transforma neumáticos viejos en un columpio o un laberinto, combinándolos con madera reciclada para mayor estabilidad.",
    "**Arte mural**: Crea un collage con periódicos, revistas y ropa vieja (textiles), pegándolos sobre una base de cartón para un cuadro decorativo.",
    "**Maceta ecológica**: Utiliza latas de conserva y botellas PET cortadas para hacer macetas, llenándolas con tierra y plantando semillas.",
    "**Bolsa reutilizable**: Confecciona una bolsa de tela a partir de ropa y textiles viejos, agregando asas de cobre o metales ferrosos reciclados.",
    "**Escultura metálica**: Ensambla una figura artística usando aluminio de latas, acero y metales ferrosos, soldándolos con herramientas básicas.",
    "**Filtro de aceite**: Diseña un sistema simple para reutilizar aceite usado en proyectos de jardinería, combinado con pilas y baterías para un experimento de energía.",
    "**Mueble rústico**: Construye una estantería con madera reciclada y aparatos electrónicos desarmados para agregar detalles como cables de cobre.",
    "**Juego de mesa**: Crea un tablero con cartón, vidrio reciclado como fichas y revistas para decorar, incorporando elementos de pilas para un toque interactivo."
]

@bot.command()
async def eco(ctx):
    # Elegir aleatoriamente si enviar un material o una idea
    if random.choice([True, False]):
        # Enviar un material reciclable aleatorio
        material = random.choice(materiales)
        await ctx.send(f"**Material reciclable sugerido:** {material}")
    else:
        # Enviar una idea ecológica aleatoria
        idea = random.choice(ideas)
        await ctx.send(f"**Idea ecológica:** {idea}")
        bot.run("token") 