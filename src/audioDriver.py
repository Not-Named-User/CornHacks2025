import asyncio
import numpy as np
import sounddevice as sd
import pygame

shared_state = {"decibel": 50}

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
        while True:
            await asyncio.sleep(0.1)  # Just keep yielding control

# --- Pygame Loop ---
async def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        tick_speed = max(10, min(120, 1.5 * int(shared_state["decibel"])))

        screen.fill((0, 0, 0))

        pygame.draw.circle(screen, "red", player_pos, 20)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 10
        if keys[pygame.K_s]:
            player_pos.y += 10
        if keys[pygame.K_a]:
            player_pos.x -= 10
        if keys[pygame.K_d]:
            player_pos.x += 10
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
