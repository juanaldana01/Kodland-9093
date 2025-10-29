import discord
import random

# --- Configuración del bot ---
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# --- Elementos para generar contraseñas ---
elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# --- Diccionario de memes ---
meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "BACANO": "Algo que está muy chévere",
}

@client.event
async def on_ready():
    print(f'✅ Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # --- SUMAS tipo "$5 + 8" ---
    if message.content.startswith("$") and "+" in message.content:
        try:
            # Quitar el símbolo $
            texto = message.content[1:]

            # Dividir por el signo +
            partes = texto.split("+")
            if len(partes) == 2:
                num1 = int(partes[0].strip())
                num2 = int(partes[1].strip())
                resultado = num1 + num2

                if resultado > 200:
                    await message.channel.send("Esa suma es demasiado alta para mí 😅")
                else:
                    await message.channel.send(f"{num1} + {num2} = {resultado}")
            else:
                await message.channel.send("Por favor escribe la suma así: $5 + 8")
            return
        except:
            await message.channel.send("Solo puedo sumar números enteros, intenta de nuevo 🙂")
            return

    # --- Comando $hello ---
    if message.content.startswith('$hello'):
        await message.channel.send("¡Hola! 👋")

    # --- Comando $bye ---
    elif message.content.startswith('$bye'):
        await message.channel.send("😊")

    # --- Comando $pass <longitud> ---
    elif message.content.startswith('$pass'):
        try:
            parts = message.content.split()
            if len(parts) < 2:
                await message.channel.send("Por favor, indica la longitud. Ejemplo: $pass 12")
                return

            pass_length = int(parts[1])
            password = ''.join(random.choice(elements) for _ in range(pass_length))
            await message.channel.send(f"🔐 Tu contraseña generada es:\n`{password}`")
        except ValueError:
            await message.channel.send("Debes escribir un número entero. Ejemplo: $pass 10")

    # --- Comando $meme <PALABRA> ---
    elif message.content.startswith('$meme'):
        parts = message.content.split()
        if len(parts) < 2:
            await message.channel.send("Por favor, escribe una palabra. Ejemplo: $meme LOL")
            return

        word = parts[1].upper()
        if word in meme_dict.keys():
            await message.channel.send(f"📖 *{word}*: {meme_dict[word]}")
        else:
            await message.channel.send("❌ Todavía no tenemos esta palabra... Pero estamos trabajando en ello 🧠")

    else:
        # Puedes quitar esta línea si no quieres que responda a mensajes desconocidos
        await message.channel.send("Comando no reconocido. Usa $hello, $bye, $pass <n>, $meme <PALABRA> o una suma como $5 + 8")

# --- Ejecutar el bot ---
client.run("TU_TOKEN_AQUI")  # ⚠️ Reemplaza con tu token real
