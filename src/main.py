"""
Main running file for our game. # TODO: Improve header documentation

Status: Not Finished
"""
import asyncio
import numpy as np
import sounddevice as sd
import pygame
from game import *


shared_state = {"decibel": 50, "running": True}

# --- Microphone Reader ---
async def mic_reader():
    samplerate = 44100
    blocksize = 1024

    def audio_callback(indata, frames, time, status):
        volume_norm = np.linalg.norm(indata) * 10
        decibel = np.clip(volume_norm, 0, 100)
        shared_state["decibel"] = decibel

    # sounddevice stream runs in background threads
    with sd.InputStream(callback=audio_callback, channels=1, samplerate=samplerate, blocksize=blocksize):
        while shared_state["running"]:
            await asyncio.sleep(0.1)  # Just keep yielding control


WIDTH = 1280
HEIGHT = 720

# --- Pygame Loop ---
async def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    player = Player(player_pos, 3, 25, (0, 255, 0))
    #player.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while shared_state["running"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                shared_state["running"] = False
                return

        tick_speed = max(10, min(120, 1.5 * int(shared_state["decibel"])))

        screen.fill((0, 0, 0))

        pygame.draw.circle(screen, "red", player.pos, 20)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.pos.y -= 10
        if keys[pygame.K_s]:
            player.pos.y += 10
        if keys[pygame.K_a]:
            player.pos.x -= 10
        if keys[pygame.K_d]:
            player.pos.x += 10
        if keys[pygame.K_SPACE]:
            tick_speed = 100

        decibelText = font.render(f"Decibel: {shared_state['decibel']:.1f}", True, (255, 255, 255))
        tickText = font.render(f"TickSpeed: {tick_speed:.1f}", True, (255, 255, 255))

        clock.tick(tick_speed)
        screen.blit(decibelText, (50, 130))
        screen.blit(tickText, (50, 80))
        pygame.display.flip()

        await asyncio.sleep(0)  # Let asyncio run other tasks

# --- Entry point ---
async def main():
    mic_task = asyncio.create_task(mic_reader())
    game_task = asyncio.create_task(run_game())
    await asyncio.gather(mic_task, game_task)

if __name__ == "__main__":
    asyncio.run(main())

pygame.quit()